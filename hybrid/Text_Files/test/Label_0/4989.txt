#include <bits/stdc++.h>
using namespace std;
int n;
long long kk;
int Pow(int x, int a) {
  int ans = 1, cur = x % 998244353;
  while (a) {
    if (a & 1) ans = 1ll * ans * cur % 998244353;
    cur = 1ll * cur * cur % 998244353, a >>= 1;
  }
  return ans;
}
int Wn[2][1000006], rev[1000006];
void getwn(int len) {
  for (int mid = 1; mid < len; mid <<= 1) {
    int w0 = Pow(3, (998244353 - 1) / (mid << 1)),
        w1 = Pow(3, 998244353 - 1 - (998244353 - 1) / (mid << 1));
    Wn[0][mid] = Wn[1][mid] = 1;
    for (int i = 1; i < mid; ++i)
      Wn[0][mid + i] = 1ll * Wn[0][mid + i - 1] * w0 % 998244353,
                  Wn[1][mid + i] = 1ll * Wn[1][mid + i - 1] * w1 % 998244353;
  }
}
void getr(int len) {
  int t = __builtin_ctz(len) - 1;
  for (int i = 1; i < len; ++i) rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << t);
}
void NTT(vector<int>& A, int len, int typ) {
  for (int i = (0), iend = (len - 1); i <= iend; ++i)
    if (i < rev[i]) swap(A[i], A[rev[i]]);
  for (int mid = 1; mid < len; mid <<= 1)
    for (int i = 0; i < len; i += (mid << 1))
      for (int k = 0; k < mid; ++k) {
        int t1 = A[i + k],
            t2 = 1ll * A[i + k + mid] * Wn[typ][mid + k] % 998244353;
        A[i + k] = (t1 + t2 > 998244353 ? t1 + t2 - 998244353 : t1 + t2),
              A[i + k + mid] = (t1 - t2 < 0 ? 998244353 + t1 - t2 : t1 - t2);
      }
  if (typ == 1)
    for (int inv = Pow(len, 998244353 - 2), i = 0; i < len; ++i)
      A[i] = 1ll * A[i] * inv % 998244353;
}
vector<int> mul(vector<int> A, vector<int> B) {
  int len = 1, t = A.size() + B.size();
  while (len <= t) len <<= 1;
  getr(len), getwn(len);
  A.resize(len), B.resize(len);
  vector<int> ret(len, 0);
  NTT(A, len, 0), NTT(B, len, 0);
  for (int i = (0), iend = (len - 1); i <= iend; ++i)
    ret[i] = A[i] * 1ll * B[i] % 998244353;
  NTT(ret, len, 1);
  ret.resize(t);
  return ret;
}
vector<int> add(vector<int> A, vector<int> B) {
  int sz = max(A.size(), B.size());
  A.resize(sz), B.resize(sz);
  vector<int> ret(sz, 0);
  for (int i = (0), iend = (sz - 1); i <= iend; ++i)
    ret[i] = (A[i] + B[i] > 998244353 ? A[i] + B[i] - 998244353 : A[i] + B[i]);
  return ret;
}
vector<int> pr[1000006];
int cn;
vector<int> mult(int l, int r) {
  if (l > r) return {1};
  if (l == r) return pr[l];
  int m = l + r >> 1;
  vector<int> a = mult(l, m), b = mult(m + 1, r);
  return mul(a, b);
}
vector<int> G[1000006];
int hea[1000006], siz[1000006];
void afs(int u, int fa) {
  siz[u] = 1;
  for (int v : G[u])
    if (v != fa) {
      afs(v, u), siz[u] += siz[v];
      if (!hea[u] || siz[v] > siz[hea[u]]) hea[u] = v;
    }
}
vector<int> re[1000006];
struct fuck {
  vector<int> A, a;
};
fuck merge(fuck a, fuck b) {
  fuck tf = (fuck){add(a.A, mul(a.a, b.A)), mul(a.a, b.a)};
  return tf;
}
vector<int> fk[1000006];
int en;
fuck lsj(int l, int r) {
  if (l == r) return (fuck){fk[l], fk[l]};
  int m = l + r >> 1;
  fuck L = lsj(l, m);
  fuck R = lsj(m + 1, r);
  fuck tt = merge(L, R);
  return tt;
}
int ps[1000006];
void dfs(int u, int fa, int top) {
  for (int v : G[u])
    if (v != fa && v != hea[u]) dfs(v, u, v);
  cn = 0;
  for (int v : G[u])
    if (v != fa && v != hea[u]) pr[++cn] = re[v], ++pr[cn][0];
  vector<int> t = mult(1, cn);
  t.insert(t.begin(), 0), fk[++en] = t, ps[u] = en;
  if (hea[u])
    dfs(hea[u], u, top);
  else
    re[top] = lsj(ps[top], en).A;
  --en;
}
int J[1000006], iJ[1000006];
void solve() {
  cin >> n >> kk;
  kk %= 998244353;
  J[0] = iJ[0] = 1;
  for (int i = (1), iend = (n); i <= iend; ++i)
    J[i] = J[i - 1] * 1ll * i % 998244353, iJ[i] = Pow(J[i], 998244353 - 2);
  int u, v;
  for (int i = (2), iend = (n); i <= iend; ++i)
    scanf("%d%d", &u, &v), G[u].push_back(v), G[v].push_back(u);
  afs(1, 1);
  dfs(1, 1, 1);
  int tmp = 1, res = 0;
  for (int i = (1), iend = (n); i <= iend; ++i) {
    res = (res + tmp * 1ll * iJ[i - 1] % 998244353 * re[1][i] % 998244353) %
          998244353;
    tmp = tmp * (kk + i) % 998244353;
  }
  cout << res << endl;
}
signed main() { solve(); }
