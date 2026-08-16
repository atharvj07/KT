#include <bits/stdc++.h>
using namespace std;
int32_t main() {
  long long n;
  cin >> n;
  long long dp[n + 1][n + 1];
  for (long long i = 1; i <= n; i++) {
    for (long long j = 1; j <= n; j++) {
      cin >> dp[i][j];
    }
  }
  long long q;
  cin >> q;
  for (long long k = 0; k < q; k++) {
    long long u, v, w;
    cin >> u >> v >> w;
    long long sum = 0;
    for (long long i = 1; i <= n; i++) {
      for (long long j = 1; j <= n; j++) {
        dp[i][j] = min(dp[i][j],
                       min(dp[i][u] + dp[v][j] + w, dp[i][v] + dp[u][j] + w));
        sum += dp[i][j];
      }
    }
    cout << sum / 2 << ' ';
  }
}
