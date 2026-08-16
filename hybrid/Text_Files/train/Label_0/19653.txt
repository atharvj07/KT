#include <bits/stdc++.h>
using namespace std;
inline int toInt(string s) {
  int v;
  istringstream sin(s);
  sin >> v;
  return v;
}
template <class T>
inline string toString(T x) {
  ostringstream sout;
  sout << x;
  return sout.str();
}
inline int readInt() {
  int x;
  scanf("%d", &x);
  return x;
}
const double EPS = 1E-8;
class UnionFind {
 public:
  vector<long long> par;
  vector<long long> siz;
  vector<long long> maxv;
  UnionFind(long long sz_) : par(sz_), siz(sz_, 1LL) {
    for (long long i = 0; i < sz_; ++i) par[i] = i;
  }
  void init(long long sz_) {
    par.resize(sz_);
    siz.assign(sz_, 1LL);
    for (long long i = 0; i < sz_; ++i) par[i] = i;
  }
  long long root(long long x) {
    while (par[x] != x) {
      x = par[x] = par[par[x]];
    }
    return x;
  }
  bool merge(long long x, long long y) {
    x = root(x);
    y = root(y);
    if (x == y) return false;
    if (siz[x] < siz[y]) swap(x, y);
    siz[x] += siz[y];
    par[y] = x;
    return true;
  }
  bool issame(long long x, long long y) { return root(x) == root(y); }
  long long size(long long x) { return siz[root(x)]; }
};
long long mod_pow(long long x, long long n, long long mod) {
  long long res = 1;
  while (n) {
    if (n & 1) res = res * x;
    res %= mod;
    x = x * x % mod;
    n >>= 1;
  }
  return res;
}
bool sieve[5000000 + 10];
void make_sieve() {
  for (int i = 0; i < 5000000 + 10; ++i) sieve[i] = true;
  sieve[0] = sieve[1] = false;
  for (int i = 2; i * i < 5000000 + 10; ++i)
    if (sieve[i])
      for (int j = 2; i * j < 5000000 + 10; ++j) sieve[i * j] = false;
}
bool isprime(long long n) {
  if (n == 0 || n == 1) return false;
  for (long long i = 2; i * i <= n; ++i)
    if (n % i == 0) return false;
  return true;
}
const int MAX = 510000;
long long fac[MAX], finv[MAX], inv[MAX];
void COMinit() {
  fac[0] = fac[1] = 1;
  finv[0] = finv[1] = 1;
  inv[1] = 1;
  for (int i = 2; i < MAX; i++) {
    fac[i] = fac[i - 1] * i % 1000000007;
    inv[i] = 1000000007 - inv[1000000007 % i] * (1000000007 / i) % 1000000007;
    finv[i] = finv[i - 1] * inv[i] % 1000000007;
  }
}
long long COM(int n, int k) {
  if (n < k) return 0;
  if (n < 0 || k < 0) return 0;
  return fac[n] * (finv[k] * finv[n - k] % 1000000007) % 1000000007;
}
long long extGCD(long long a, long long b, long long &x, long long &y) {
  if (b == 0) {
    x = 1;
    y = 0;
    return a;
  }
  long long d = extGCD(b, a % b, y, x);
  y -= a / b * x;
  return d;
}
inline long long mod(long long a, long long m) { return (a % m + m) % m; }
long long modinv(long long a, long long m) {
  long long x, y;
  extGCD(a, m, x, y);
  return mod(x, m);
}
long long GCD(long long a, long long b) {
  if (b == 0) return a;
  return GCD(b, a % b);
}
struct LazySegmentTree {
 private:
  int n;
  vector<long long> node, lazy;

 public:
  LazySegmentTree(vector<long long> v) {
    int sz = (int)v.size();
    n = 1;
    while (n < sz) n *= 2;
    node.resize(2 * n - 1);
    lazy.resize(2 * n - 1, 0);
    for (int i = 0; i < sz; i++) node[i + n - 1] = v[i];
    for (int i = n - 2; i >= 0; i--)
      node[i] = node[i * 2 + 1] + node[i * 2 + 2];
  }
  void eval(int k, int l, int r) {
    if (lazy[k] != 0) {
      node[k] += lazy[k];
      if (r - l > 1) {
        lazy[2 * k + 1] += lazy[k] / 2;
        lazy[2 * k + 2] += lazy[k] / 2;
      }
      lazy[k] = 0;
    }
  }
  void add(int a, int b, long long x, int k = 0, int l = 0, int r = -1) {
    if (r < 0) r = n;
    eval(k, l, r);
    if (b <= l || r <= a) return;
    if (a <= l && r <= b) {
      lazy[k] += (r - l) * x;
      eval(k, l, r);
    } else {
      add(a, b, x, 2 * k + 1, l, (l + r) / 2);
      add(a, b, x, 2 * k + 2, (l + r) / 2, r);
      node[k] = node[2 * k + 1] + node[2 * k + 2];
    }
  }
  long long getsum(int a, int b, int k = 0, int l = 0, int r = -1) {
    if (r < 0) r = n;
    eval(k, l, r);
    if (b <= l || r <= a) return 0;
    if (a <= l && r <= b) return node[k];
    long long vl = getsum(a, b, 2 * k + 1, l, (l + r) / 2);
    long long vr = getsum(a, b, 2 * k + 2, (l + r) / 2, r);
    return vl + vr;
  }
};
using Weight = int;
using Flow = int;
struct Edge {
  int src, dst;
  Weight weight;
  Flow cap;
  Edge() : src(0), dst(0), weight(0) {}
  Edge(int s, int d, Weight w) : src(s), dst(d), weight(w) {}
};
using Edges = std::vector<Edge>;
using Graph = std::vector<Edges>;
using Array = std::vector<Weight>;
using Matrix = std::vector<Array>;
void add_edge(Graph &g, int a, int b, Weight w = 1) {
  g[a].emplace_back(a, b, w);
  g[b].emplace_back(b, a, w);
}
void add_arc(Graph &g, int a, int b, Weight w = 1) {
  g[a].emplace_back(a, b, w);
}
int n;
int a[10];
long long dp[101][11];
long long coef[101][101];
long long rec(int n, int c) {
  if (!n) {
    bool ok = false;
    for (int i = c; i < 10; i++) ok |= !!a[i];
    return !ok;
  }
  if (c == 10) return 0;
  if (~dp[n][c]) return dp[n][c];
  dp[n][c] = 0;
  for (int i = a[c]; i <= n; i++) {
    dp[n][c] = (dp[n][c] + coef[n][i] * rec(n - i, c + 1)) % 1000000007;
  }
  return dp[n][c];
}
int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  cin >> n;
  int sum = 0;
  for (int i = 0; i < (int)10; ++i) {
    cin >> a[i];
    sum += a[i];
  }
  coef[0][0] = 1;
  for (int i = 1; i <= 100; i++) {
    coef[i][0] = coef[i][i] = 1;
    for (int j = 1; j < i; j++)
      coef[i][j] = (coef[i - 1][j] + coef[i - 1][j - 1]) % 1000000007;
  }
  long long ans = 0;
  for (int dig = 1; dig <= n; dig++) {
    for (int i = 1; i < 10; i++) {
      memset(dp, -1, sizeof(dp));
      bool u = !!a[i];
      a[i] -= u;
      ans = (ans + rec(dig - 1, 0)) % 1000000007;
      a[i] += u;
    }
  }
  cout << ans << endl;
  return 0;
}
