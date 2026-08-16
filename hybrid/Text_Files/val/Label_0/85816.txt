#include <bits/stdc++.h>
int n, m;
const long long MOD = 1000000007;
long long dp[3000][3000];
long long sum1[3000][3000];
long long sum2[3000][3000];
long long ans = 0;
void compute_dp() {
  memset(dp, 0, sizeof(dp));
  memset(sum1, 0, sizeof(sum1));
  memset(sum2, 0, sizeof(sum2));
  for (int i = 2; i <= m; i++) {
    dp[1][i] = 1;
    sum1[1][i] = sum1[1][i - 1] + 1;
    sum2[1][i] = i + sum2[1][i - 1];
  }
  for (int h = 2; h <= n; h++) {
    for (int i = 2; i <= m; i++) {
      dp[h][i] = 1;
      dp[h][i] += (i + 1) * sum1[h - 1][i] - sum2[h - 1][i];
      dp[h][i] %= MOD;
      dp[h][i] += MOD;
      dp[h][i] %= MOD;
      sum1[h][i] = (sum1[h][i - 1] + dp[h][i]) % MOD;
      sum2[h][i] = (sum2[h][i - 1] + dp[h][i] * i) % MOD;
    }
  }
}
void compute_ans() {
  for (int t = 1; t <= n; t++) {
    for (int w = 2; w <= m; w++) {
      long long val = (dp[t][w] - dp[t - 1][w]) * dp[n - t + 1][w];
      val %= MOD;
      val += MOD;
      val %= MOD;
      val *= (m - w + 1);
      ans += val;
      ans %= MOD;
    }
  }
}
int main() {
  scanf("%d %d", &n, &m);
  compute_dp();
  compute_ans();
  printf("%I64d\n", ans);
}
