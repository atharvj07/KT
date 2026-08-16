#include <bits/stdc++.h>
using namespace std;
long long int mod;
long long int a[550];
long long int dp[2][501][501];
int main() {
  long long int n, m, i, j, ans, b, z, k;
  memset(dp, 0, sizeof(dp));
  scanf("%lld", &n);
  scanf("%lld", &m);
  scanf("%lld", &b);
  scanf("%lld", &mod);
  dp[0][0][0] = 1;
  for (i = 1; i <= n; i++) scanf("%lld", &a[i]);
  for (i = 1; i <= n; i++) {
    z = i & 1;
    for (j = 0; j <= m; j++) {
      for (k = 0; k <= b; k++) {
        dp[z][j][k] = dp[z ^ 1][j][k];
        if (a[i] <= k && j)
          dp[z][j][k] = (dp[z][j][k] + dp[z][j - 1][k - a[i]]) % mod;
      }
    }
  }
  ans = 0;
  z = n % 2;
  for (i = 0; i <= b; i++) ans = (ans + dp[z][m][i]) % mod;
  printf("%lld\n", ans);
  return 0;
}
