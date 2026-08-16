#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  vector<int> arr(10);
  for (int i = 0; i < 10; i++) cin >> arr[i];
  vector<vector<long long> > c(n + 8, vector<long long>(n + 8)),
      dp(n + 8, vector<long long>(n + 8));
  for (int i = 0; i < n + 1; i++) c[0][i] = 0, c[i][0] = 1;
  for (int i = 1; i < n + 1; i++) {
    for (int j = 1; j < i + 1; j++) {
      c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % 1000000007;
    }
  }
  for (int i = 0; i < n + 1; i++) {
    for (int j = 9; j >= 0; j--) {
      if (j == 0) {
        for (int k = arr[0]; k < n + 1; k++)
          if (!i)
            dp[i][0] = 0;
          else if (i >= k)
            dp[i][0] = (dp[i][0] + (dp[i - k][1] * c[i - 1][k]) % 1000000007) %
                       1000000007;
      } else if (j < 9) {
        for (int k = arr[j]; k < n + 1; k++)
          if (i >= k)
            dp[i][j] = (dp[i][j] + (dp[i - k][j + 1] * c[i][k]) % 1000000007) %
                       1000000007;
      } else {
        if (i >= arr[9])
          dp[i][9] = 1;
        else
          dp[i][9] = 0;
      }
    }
  }
  long long ans = 0;
  for (int i = 1; i < n + 1; i++) ans = (ans + dp[i][0]) % 1000000007;
  cout << ans << endl;
}
