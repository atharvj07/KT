#include <bits/stdc++.h>
using namespace std;
const int N = 82;
int dp[N][N][N][N];
int n, k, m, g[N][N];
int DP(int l, int r, int cur, int k) {
  if (dp[l][r][cur][k] != -1) return dp[l][r][cur][k];
  if (k == 1) {
    dp[l][r][cur][k] = 0;
    return 0;
  }
  int res = 1e8;
  for (int i = 1; i <= n; i++) {
    if (g[cur][i]) {
      if (i > l && i < r) {
        int s = l, t = r;
        if (cur < i)
          s = cur;
        else
          t = cur;
        res = min(res, g[cur][i] + DP(s, t, i, k - 1));
      }
    }
  }
  dp[l][r][cur][k] = res;
  return dp[l][r][cur][k];
}
int main() {
  while (cin >> n >> k >> m) {
    int u, v, w;
    for (int i = 1; i <= n; i++)
      for (int j = 1; j <= n; j++) g[i][j] = 1e8;
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < m; i++) {
      scanf("%d%d%d", &u, &v, &w);
      g[u][v] = min(g[u][v], w);
    }
    int ans = 1e8;
    for (int i = 1; i <= n; i++) ans = min(ans, DP(0, n + 1, i, k));
    if (ans >= 1e8) ans = -1;
    cout << ans << endl;
  }
  return 0;
}
