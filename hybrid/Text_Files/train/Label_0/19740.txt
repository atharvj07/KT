#include <bits/stdc++.h>
using namespace std;
const long long N = 2e5 + 5, inf = 1e18, mod = 998244353;
long long n, dp[2][202][2], ps[2][202][2], a[N], PS[2][202][2];
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  dp[0][0][1] = 1;
  for (long long j = 0; j <= 200; j++) ps[0][j][1] = 1;
  cin >> n;
  for (long long i = 1; i <= n; i++) {
    cin >> a[i];
    if (a[i] != -1) {
      dp[i % 2][a[i]][0] =
          ps[(i - 1) % 2][a[i] - 1][0] + ps[(i - 1) % 2][a[i] - 1][1];
      dp[i % 2][a[i]][0] %= mod;
      dp[i % 2][a[i]][1] = dp[(i - 1) % 2][a[i]][0] + PS[(i - 1) % 2][a[i]][1];
      dp[i % 2][a[i]][1] %= mod;
    } else {
      for (long long j = 1; j <= 200; j++) {
        dp[i % 2][j][0] = ps[(i - 1) % 2][j - 1][0] + ps[(i - 1) % 2][j - 1][1];
        dp[i % 2][j][0] %= mod;
        dp[i % 2][j][1] = dp[(i - 1) % 2][j][0] + PS[(i - 1) % 2][j][1];
        dp[i % 2][j][1] %= mod;
      }
    }
    ps[0][0][1] = 0;
    for (long long j = 1; j <= 200; j++) {
      ps[i % 2][j][0] = ps[i % 2][j - 1][0] + dp[i % 2][j][0];
      ps[i % 2][j][0] %= mod;
      ps[i % 2][j][1] = ps[i % 2][j - 1][1] + dp[i % 2][j][1];
      ps[i % 2][j][1] %= mod;
    }
    for (long long j = 200; j >= 1; j--) {
      PS[i % 2][j][1] = PS[i % 2][j + 1][1] + dp[i % 2][j][1];
      PS[i % 2][j][1] %= mod;
    }
    for (long long j = 0; j <= 200; j++)
      dp[(i - 1) % 2][j][0] = dp[(i - 1) % 2][j][1] = 0;
  }
  cout << ps[n % 2][200][1];
  return 0;
}
