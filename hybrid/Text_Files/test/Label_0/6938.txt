#include <bits/stdc++.h>
using namespace std;
const int N = 5e3 + 5;
const int MOD = 1e9 + 7;
int dp[N][N];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  ;
  int n, i, j;
  cin >> n;
  n++;
  n = n + n;
  dp[1][1] = 1;
  for (i = 2; i <= n; i++) {
    for (j = 0; j <= n; j++) {
      dp[i][j] = dp[i - 1][j + 1];
      if (j > 0) dp[i][j] += dp[i - 1][j - 1];
      if (dp[i][j] >= MOD) dp[i][j] -= MOD;
    }
  }
  int ans = 0;
  for (i = n - 1; i > 0; i -= 2) {
    for (j = 0; j < n - i; j++)
      if ((n - (i + j)) % 2 == 0) {
        ans += dp[i][j];
        if (ans >= MOD) ans -= MOD;
      }
  }
  cout << ans << '\n';
  return 0;
}
