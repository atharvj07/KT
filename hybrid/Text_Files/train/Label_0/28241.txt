#include <bits/stdc++.h>
using namespace std;
int n, a[510];
int dp[510][510];
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) dp[i][j] = 1e9;
  }
  for (int i = 1; i <= n; i++) dp[i][i] = 1;
  for (int len = 2; len <= n; len++) {
    for (int i = 1; i <= n; i++) {
      if (i + len - 1 > n) break;
      int j = i + len - 1;
      if (a[i] == a[j]) {
        if (len == 2) {
          dp[i][j] = 1;
        } else {
          dp[i][j] = dp[i + 1][j - 1];
        }
      }
      for (int k = i; k < j; k++) {
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j]);
      }
    }
  }
  printf("%d\n", dp[1][n]);
}
