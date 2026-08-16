#include <bits/stdc++.h>
using namespace std;
const int MOD = (int)1e9 + 7;
const int INF = (int)1e9;
const long long LINF = (long long)1e18;
const long double PI = acos((long double)-1);
const long double EPS = 1e-9;
inline long long gcd(long long a, long long b) {
  long long r;
  while (b) {
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}
inline long long lcm(long long a, long long b) { return a / gcd(a, b) * b; }
inline long long fpow(long long n, long long k, int p = MOD) {
  long long r = 1;
  for (; k; k >>= 1) {
    if (k & 1) r = r * n % p;
    n = n * n % p;
  }
  return r;
}
template <class T>
inline int chkmin(T& a, const T& val) {
  return val < a ? a = val, 1 : 0;
}
template <class T>
inline int chkmax(T& a, const T& val) {
  return a < val ? a = val, 1 : 0;
}
template <class T>
inline T isqrt(T k) {
  T r = sqrt(k) + 1;
  while (r * r > k) r--;
  return r;
}
template <class T>
inline T icbrt(T k) {
  T r = cbrt(k) + 1;
  while (r * r * r > k) r--;
  return r;
}
inline void addmod(int& a, int val, int p = MOD) {
  if ((a = (a + val)) >= p) a -= p;
}
inline void submod(int& a, int val, int p = MOD) {
  if ((a = (a - val)) < 0) a += p;
}
inline int mult(int a, int b, int p = MOD) { return (long long)a * b % p; }
inline int inv(int a, int p = MOD) { return fpow(a, p - 2, p); }
inline int sign(long double x) { return x < -EPS ? -1 : x > +EPS; }
inline int sign(long double x, long double y) { return sign(x - y); }
const int maxn = 1000000 + 5;
const int mod = (int)1e8 + 7;
int n;
vector<int> adj[maxn];
map<pair<int, int>, int> hs;
int f[maxn];
int g[maxn];
int cnt[maxn];
int tot;
inline int query(pair<int, int> val) {
  if (hs.count(val)) return hs[val];
  int res = int((hs).size());
  return hs[val] = res;
}
void add(int val) {
  if (!(cnt[val]++)) {
    tot++;
  }
}
void rem(int val) {
  if (!(--cnt[val])) {
    tot--;
  }
}
void dfs(int u, int p = -1) {
  pair<int, int> r;
  for (int i = (0); i < (int((adj[u]).size())); i++) {
    int v = adj[u][i];
    if (v != p) {
      dfs(v, u);
      addmod(r.first, fpow(3, f[v]));
      addmod(r.second, fpow(5, f[v], mod), mod);
    }
  }
  add(f[u] = query(r));
}
void dfs2(int u, int p = -1, int pv = -1) {
  pair<int, int> r;
  if (pv != -1) {
    addmod(r.first, fpow(3, pv));
    addmod(r.second, fpow(5, pv, mod), mod);
    add(pv);
  }
  for (int i = (0); i < (int((adj[u]).size())); i++) {
    int v = adj[u][i];
    if (v != p) {
      addmod(r.first, fpow(3, f[v]));
      addmod(r.second, fpow(5, f[v], mod), mod);
    }
  }
  rem(f[u]);
  g[u] = tot;
  for (int i = (0); i < (int((adj[u]).size())); i++) {
    int v = adj[u][i];
    if (v != p) {
      submod(r.first, fpow(3, f[v]));
      submod(r.second, fpow(5, f[v], mod), mod);
      dfs2(v, u, query(r));
      addmod(r.first, fpow(3, f[v]));
      addmod(r.second, fpow(5, f[v], mod), mod);
    }
  }
  if (pv != -1) {
    rem(pv);
  }
  add(f[u]);
}
void solve() {
  cin >> n;
  for (int i = (0); i < (n - 1); i++) {
    int u, v;
    cin >> u >> v;
    u--, v--;
    adj[u].push_back(v), adj[v].push_back(u);
  }
  dfs(0), dfs2(0);
  pair<int, int> best;
  for (int i = (0); i < (n); i++) chkmax(best, make_pair(g[i], i));
  cout << best.second + 1 << "\n";
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  solve();
  return 0;
}
