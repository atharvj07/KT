#include <bits/stdc++.h>
using namespace std;
const int maxn = 16;
const int maxm = 1e4 + 5;
const int inf = 1e9 + 5;
int n, m, a[maxn][maxm], cost[maxn][maxn];
void enter() {
  cin >> n >> m;
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j) cin >> a[i][j];
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < i; ++j) {
      int res = inf;
      for (int t = 0; t < m; ++t) res = min(res, abs(a[i][t] - a[j][t]));
      cost[i][j] = cost[j][i] = res;
    }
  }
}
int f[1 << 16][16];
void solve() {
  int res = 0;
  for (int i = 0; i < n; ++i) {
    fill_n(&f[0][0], (1 << 16) * 16, -1);
    f[(1 << i)][i] = inf;
    for (int mask = (1 << i); mask < (1 << n); ++mask) {
      for (int j = 0; j < n; ++j) {
        if (!((mask >> j) & 1)) continue;
        for (int t = 0; t < n; ++t) {
          if (j == t || (!((mask >> t) & 1))) continue;
          f[mask][j] = max(f[mask][j], min(f[mask ^ (1 << j)][t], cost[t][j]));
        }
      }
    }
    for (int j = 0; j < n; ++j) {
      int ans = f[(1 << n) - 1][j];
      for (int t = 1; t < m; ++t) ans = min(ans, abs(a[i][t] - a[j][t - 1]));
      res = max(res, ans);
    }
  }
  cout << res;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  if (fopen("TEST"
            ".INP",
            "r"))
    freopen(
        "TEST"
        ".INP",
        "r", stdin),
        freopen(
            "TEST"
            ".OUT",
            "w", stdout);
  enter();
  solve();
}
