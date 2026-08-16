#include <bits/stdc++.h>
using namespace std;
long long t, n, dp[300002][3], a[300002], b[300002];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> t;
  while (t--) {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i] >> b[i];
    for (int i = 2; i <= n; i++)
      dp[i][0] = dp[i][1] = dp[i][2] = (long long)(1e18);
    dp[1][0] = 0;
    dp[1][1] = b[1];
    dp[1][2] = b[1] + b[1];
    for (int i = 1; i < n; i++) {
      for (int x = 0; x <= 2; x++)
        for (int y = 0; y <= 2; y++)
          if (a[i] + x != a[i + 1] + y)
            dp[i + 1][y] = min(dp[i + 1][y], dp[i][x] + 1ll * b[i + 1] * y);
    }
    cout << min(dp[n][0], min(dp[n][1], dp[n][2])) << "\n";
  }
  return 0;
}
