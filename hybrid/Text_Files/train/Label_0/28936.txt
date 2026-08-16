#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const int mod1 = 998244353;
const int N = 1 << 17;
int weight[N], in[N], parent[N];
vector<pair<int, int> > edge[N];
int a[N], b[N], c[N], d[N];
long long qpow(long long a, long long b, long long mod) {
  long long res = 1;
  while (b) {
    if (b & 1) {
      res = res * a % mod;
    }
    b >>= 1;
    a = a * a % mod;
  }
  return res;
}
struct FWT {
  int mod = 1e9 + 7;
  int rev = qpow(2, mod - 2, mod);
  int add(int a, int b) {
    if (a + b >= mod) return a + b - mod;
    if (a + b < 0) return a + b + mod;
    return a + b;
  }
  int mul(int a, int b) { return (long long)a * b % mod; }
  void fwt(int a[], int n, int op) {
    for (int d = 1; d < n; d <<= 1) {
      for (int m = d << 1, i = 0; i < n; i += m) {
        for (int j = 0; j < d; j++) {
          int x = a[i + j], y = a[i + j + d];
          if (op == 0)
            a[i + j] = add(x, y), a[i + j + d] = add(x, -y);
          else
            a[i + j] = mul(add(x, y), rev), a[i + j + d] = mul(add(x, -y), rev);
        }
      }
    }
  }
  void solve(int a[], int b[], int n) {
    fwt(a, n, 0);
    fwt(b, n, 0);
    for (int i = (0); i < (n); i++) a[i] = mul(a[i], b[i]);
    fwt(a, n, 1);
  }
} Fwt;
int dfn = 0;
vector<int> sum;
int T = 0;
void dfs(int u) {
  in[u] = dfn++;
  for (auto i : edge[u]) {
    int v = i.first;
    int w = i.second;
    if (v == parent[u]) continue;
    if (in[v] == -1) {
      parent[v] = u;
      weight[v] = w;
      dfs(v);
    } else if (in[v] < in[u]) {
      int tot = w;
      for (int i = u; i != v; i = parent[i]) {
        tot ^= weight[i];
      }
      T ^= tot;
      memset(b, 0, sizeof(b));
      memset(d, 0, sizeof(d));
      for (int i = u; i != v; i = parent[i]) {
        b[tot ^ weight[i]] += 1;
        d[tot ^ weight[i]] += 1;
      }
      b[tot ^ w] += 1;
      d[tot ^ w] += 1;
      Fwt.mod = 1e9 + 7;
      Fwt.fwt(b, N, 0);
      Fwt.mod = mod1;
      Fwt.fwt(d, N, 0);
      for (int i = (0); i < (N); i++) a[i] = (long long)a[i] * b[i] % mod;
      for (int i = (0); i < (N); i++) c[i] = (long long)c[i] * d[i] % mod1;
    }
  }
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int n, m;
  cin >> n >> m;
  memset(in, -1, sizeof(in));
  for (int i = (1); i < (m + 1); i++) {
    int u, v, w;
    cin >> u >> v >> w;
    edge[u].push_back(make_pair(v, w));
    edge[v].push_back(make_pair(u, w));
    T ^= w;
  }
  a[0] = 1;
  c[0] = 1;
  Fwt.mod = 1e9 + 7;
  Fwt.fwt(a, N, 0);
  Fwt.mod = mod1;
  Fwt.fwt(c, N, 0);
  dfs(1);
  memset(b, 0, sizeof(b));
  memset(d, 0, sizeof(d));
  b[T] = 1;
  d[T] = 1;
  Fwt.mod = 1e9 + 7;
  Fwt.fwt(b, N, 0);
  for (int i = (0); i < (N); i++) a[i] = (long long)a[i] * b[i] % mod;
  Fwt.mod = mod1;
  Fwt.fwt(d, N, 0);
  for (int i = (0); i < (N); i++) c[i] = (long long)c[i] * d[i] % mod1;
  Fwt.mod = 1e9 + 7;
  Fwt.fwt(a, N, 1);
  Fwt.mod = mod1;
  Fwt.fwt(c, N, 1);
  for (int i = (0); i < (N); i++) {
    if (a[i] || c[i]) {
      cout << i << " " << a[i] << "\n";
      return 0;
    }
  }
  return 0;
}
