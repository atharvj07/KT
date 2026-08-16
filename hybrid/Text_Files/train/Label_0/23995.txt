#include <bits/stdc++.h>
using namespace std;
const int mod = 1000000007ll;
int r, g;
long long dp[2][300000];
int main() {
  scanf("%d %d", &r, &g);
  int h = 1;
  while (((h + 1) * (h + 2)) / 2 <= r + g) h++;
  int N = min(r, g);
  dp[0][0] = 1;
  for (int k = 1; k <= h; k++) {
    for (int n = 0; n <= N; n++) {
      dp[k % 2][n] =
          (n - k >= 0 ? dp[(k + 1) % 2][n - k] : 0) + dp[(k + 1) % 2][n];
      dp[k % 2][n] %= mod;
    }
  }
  long long ans = 0;
  for (int i = 0; i <= N; i++) {
    if ((h * (h + 1)) / 2 - i <= max(r, g)) {
      ans += dp[h % 2][i];
      ans %= mod;
    }
  }
  printf("%lld\n", ans);
}
