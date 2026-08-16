#include <bits/stdc++.h>
using namespace std;
int cnt[2], num[105], dp[105][105][105][2];
int main() {
  int n, t1;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &t1), num[i] = t1;
    if (t1) cnt[t1 & 1]++;
  }
  cnt[0] = n / 2 - cnt[0];
  cnt[1] = (n / 2 + n % 2) - cnt[1];
  for (int i = 0; i <= n; i++) {
    for (int j = 0; j <= n + 1; j++)
      for (int k = 0; k <= n + 1; k++)
        for (int h = 0; h < 2; h++) dp[i][j][k][h] = 1e9;
  }
  dp[0][cnt[0]][cnt[1]][0] = dp[0][cnt[0]][cnt[1]][1] = 0;
  for (int i = 1; i <= n; i++) {
    if (num[i] == 0) {
      for (int j = 0; j <= cnt[0]; j++)
        for (int k = 0; k <= cnt[1]; k++) {
          dp[i][j][k][0] =
              min(dp[i - 1][j + 1][k][0], dp[i - 1][j + 1][k][1] + 1);
          dp[i][j][k][1] =
              min(dp[i - 1][j][k + 1][1], dp[i - 1][j][k + 1][0] + 1);
        }
    } else {
      for (int j = 0; j <= cnt[0]; j++)
        for (int k = 0; k <= cnt[1]; k++) {
          int t1 = num[i] & 1;
          dp[i][j][k][t1] =
              min(dp[i - 1][j][k][t1], dp[i - 1][j][k][t1 ^ 1] + 1);
        }
    }
  }
  cout << min(dp[n][0][0][0], dp[n][0][0][1]) << endl;
}
