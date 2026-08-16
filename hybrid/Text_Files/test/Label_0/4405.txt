#include <bits/stdc++.h>
using namespace std;
const int oo = 0x3f3f3f3f;
const long long OO = 1LL << 61;
const int MOD = 1000000007;
long long dp[1005][20005];
int a[1005];
int main() {
  int n;
  while (scanf("%d", &n) != EOF) {
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    memset(dp, 0, sizeof dp);
    for (int i = 0; i <= n; i++) dp[i][10000] = 1;
    for (int i = 1; i <= n; i++) {
      for (int j = 0; j <= 20000; j++) {
        if (j + a[i] <= 20000)
          dp[i][j + a[i]] = (dp[i][j + a[i]] + dp[i - 1][j] + MOD) % MOD;
        if (j - a[i] >= 0)
          dp[i][j - a[i]] = (dp[i][j - a[i]] + dp[i - 1][j] + MOD) % MOD;
      }
    }
    long long ans = 0;
    for (int i = 1; i <= n; i++) ans = (ans + dp[i][10000] - 1 + MOD) % MOD;
    cout << ans << endl;
  }
  return 0;
}
