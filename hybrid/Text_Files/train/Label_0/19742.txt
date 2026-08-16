#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
const int K = 200;
const int mod = 998244353;
int power(int a, int b) {
  int res = 1;
  while (b) {
    if (b & 1) {
      res = 1LL * res * a % mod;
    }
    a = 1LL * a * a % mod;
    b >>= 1;
  }
  return res;
}
int main() {
  int n, a[N], b = 0, dp[2][K + 5][2] = {0}, sum[2][K + 5][2] = {0};
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &a[i]);
  }
  if (a[1] != -1) {
    dp[b][a[1]][1] = 1;
  } else {
    for (int i = 1; i <= K; i++) {
      dp[b][i][1] = 1;
    }
  }
  for (int i = 1; i <= K; i++) {
    sum[b][i][1] = (dp[b][i][1] + sum[b][i - 1][1]) % mod;
    sum[b][i][0] = (dp[b][i][0] + sum[b][i - 1][0]) % mod;
  }
  b = 1;
  for (int i = 2; i <= n; i++) {
    for (int j = 1; j <= K; j++) {
      dp[b][j][1] = dp[b][j][0] = 0;
      if (a[i] == -1 || a[i] == j) {
        if (i != 2) {
          dp[b][j][1] += (sum[b ^ 1][K][1] + mod - sum[b ^ 1][j][1]) % mod;
          dp[b][j][1] %= mod;
        }
        dp[b][j][1] += (dp[b ^ 1][j][0] + dp[b ^ 1][j][1]) % mod;
        dp[b][j][1] %= mod;
        dp[b][j][0] += (sum[b ^ 1][j - 1][0] + sum[b ^ 1][j - 1][1]) % mod;
        dp[b][j][0] %= mod;
      }
    }
    for (int j = 1; j <= K; j++) {
      sum[b][j][1] = (dp[b][j][1] + sum[b][j - 1][1]) % mod;
      sum[b][j][0] = (dp[b][j][0] + sum[b][j - 1][0]) % mod;
    }
    b ^= 1;
  }
  printf("%d\n", sum[b ^ 1][K][1]);
  return 0;
}
