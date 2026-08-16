#include <bits/stdc++.h>
using namespace std;
const long long N = 1e5 + 10;
const long long mod = 1e9 + 7;
long long self[N], eq[N];
vector<pair<long long, long long> > a[N];
long long tav(long long n, long long k) {
  n %= mod;
  long long ans = 1;
  while (k > 0) {
    if (k % 2) ans = (ans * n) % mod;
    n = (n * n) % mod;
    k >>= 1;
  }
  return ans;
}
long long rev(long long x) { return tav(x, mod - 2); }
bool dfs(long long v, long long p = -1) {
  {
    long long u, c;
    bool flag;
    for (auto P : a[v]) {
      u = P.first;
      c = P.second;
      if (u != p) {
        flag = dfs(u, v);
        if (!flag) continue;
        long long f = (rev(a[v].size()) * rev(self[u])) % mod;
        self[v] -= (f * rev(a[u].size())) % mod;
        self[v] = (self[v] + mod) % mod;
        eq[v] += (eq[u] * f) % mod;
        eq[v] %= mod;
      }
    }
  }
  if (a[v].size() == 1) return false;
  return true;
}
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  long long n;
  cin >> n;
  for (long long i = 0, u, v, c; i < n - 1; i++) {
    cin >> u >> v >> c;
    a[u].push_back(make_pair(v, c));
    a[v].push_back(make_pair(u, c));
  }
  fill(self, self + N, 1);
  for (long long v = 0, u, c; v < n; v++) {
    for (auto P : a[v]) {
      u = P.first;
      c = P.second;
      eq[v] += (c * rev(a[v].size())) % mod;
      eq[v] %= mod;
    }
    if (a[v].size() == 1) eq[v] = 0;
  }
  dfs(0);
  cout << (eq[0] * rev(self[0])) % mod << "\n";
  return 0;
}
