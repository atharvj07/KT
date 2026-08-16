#include <bits/stdc++.h>
using namespace std;
const int N = 68, inf = 1e9 + 8;
int dp[N][N][N], d[N][N][N], n, m, r, s, t, q, x, e;
int main() {
  cin >> n >> m >> r;
  e = max(n, m);
  for (int i = 0; i <= e; i++)
    for (int j = 0; j <= e; j++)
      for (int k = 0; k <= e; k++) d[i][j][k] = inf, dp[i][j][k] = inf;
  for (int i = 0; i < m; i++) {
    for (int j = 1; j <= n; j++)
      for (int k = 1; k <= n; k++) {
        cin >> x;
        d[i][j][k] = x;
      }
    for (int w = 1; w <= n; w++)
      for (int j = 1; j <= n; j++)
        for (int k = 1; k <= n; k++)
          d[i][j][k] = min(d[i][j][k], d[i][j][w] + d[i][w][k]);
  }
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      for (int k = 0; k < m; k++) dp[i][j][0] = min(dp[i][j][0], d[k][i][j]);
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      for (int k = 1; k <= n; k++)
        for (int w = 1; w <= n; w++)
          dp[j][k][i] = min(dp[j][k][i], dp[j][w][i - 1] + dp[w][k][0]);
  while (r--) {
    cin >> s >> t >> q;
    int mn = min(q, n);
    cout << dp[s][t][mn] << endl;
  }
}
