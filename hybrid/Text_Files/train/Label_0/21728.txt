#include <bits/stdc++.h>
using namespace std;
const int LMT = 202;
const int zero = 200;
int rest[LMT];
double dp[LMT][LMT][LMT << 1], p[LMT];
int main() {
  int n, l, k, x;
  double ans = 0;
  scanf("%d%d%d", &n, &l, &k);
  ;
  for (int i = 1; i <= n; i++) {
    scanf("%d", &x);
    p[i] = x / 100.0;
  }
  for (int i = 1; i <= n; i++) {
    scanf("%d", &rest[i]);
  }
  const int end = zero + 200;
  dp[0][0][zero + k] = 1;
  for (int i = 1; i <= n; i++)
    for (int j = 0; j < i; j++)
      for (int k = 0; k <= end; k++) {
        int x = min(end, k + rest[i]);
        dp[i][j + 1][x] += dp[i - 1][j][k] * p[i];
        dp[i][j][k] += dp[i - 1][j][k] * (1 - p[i]);
      }
  for (int i = l; i <= n; i++)
    for (int j = zero; j <= end; j++) ans += dp[n][i][j];
  printf("%.12lf\n", ans);
  return 0;
}
