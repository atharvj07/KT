#include <bits/stdc++.h>
using namespace std;
const int maxN = 101;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> a(n + 1);
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
  }
  int dp[maxN][maxN][2];
  memset(dp, 0x3f, sizeof(dp));
  dp[0][0][0] = 0;
  dp[0][0][1] = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j <= n; j++) {
      if (a[i] % 2 || a[i] == 0) {
        dp[i][j][1] = min(dp[i - 1][j][0] + 1, dp[i - 1][j][1]);
      }
      if (a[i] % 2 == 0) {
        dp[i][j][0] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1] + 1);
      }
    }
  }
  cout << min(dp[n][n / 2][0], dp[n][n / 2][1]);
  return 0;
}
