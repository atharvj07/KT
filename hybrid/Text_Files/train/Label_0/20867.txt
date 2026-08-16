#include <bits/stdc++.h>
using namespace std;
int n, c, a[200500], b[200500], dp[2][200500];
int main() {
  scanf("%d %d", &n, &c);
  for (int i = 1; i <= n - 1; ++i) {
    scanf("%d", &a[i]);
  }
  for (int i = 1; i <= n - 1; ++i) {
    scanf("%d", &b[i]);
  }
  dp[1][1] = c;
  for (int i = 2; i <= n; ++i) {
    dp[0][i] = a[i - 1] + min(dp[0][i - 1], dp[1][i - 1]);
    dp[1][i] = b[i - 1] + min(dp[0][i - 1] + c, dp[1][i - 1]);
  }
  for (int i = 1; i <= n; ++i) {
    printf("%d ", min(dp[0][i], dp[1][i]));
  }
}
