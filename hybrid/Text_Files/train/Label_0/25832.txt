#include <bits/stdc++.h>
using namespace std;
double A[128][128], dp[7][128], P[7][128];
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < int((1 << n)); i++)
    for (int j = 0; j < int((1 << n)); j++) {
      cin >> A[i][j];
      A[i][j] /= 100.0;
    }
  for (int i = 0; i < int((1 << n)); i++) P[0][i] = 1.0;
  for (int d = 1; d < int(n + 1); d++)
    for (int i = 0; i < (1 << n); i += (1 << d)) {
      for (int j = i; j < int(i + (1 << (d - 1))); j++)
        for (int k = i + (1 << (d - 1)); k < int(i + (1 << d)); k++)
          P[d][j] += P[d - 1][j] * P[d - 1][k] * A[j][k];
      for (int j = i + (1 << (d - 1)); j < int(i + (1 << d)); j++)
        for (int k = i; k < int(i + (1 << (d - 1))); k++)
          P[d][j] += P[d - 1][j] * P[d - 1][k] * A[j][k];
    }
  for (int d = 1; d < int(n + 1); d++)
    for (int i = 0; i < (1 << n); i += (1 << d)) {
      for (int j = i; j < int(i + (1 << (d - 1))); j++)
        for (int k = i + (1 << (d - 1)); k < int(i + (1 << d)); k++)
          dp[d][j] = max(
              dp[d][j], P[d][j] * (1 << (d - 1)) + dp[d - 1][j] + dp[d - 1][k]);
      for (int j = i + (1 << (d - 1)); j < int(i + (1 << d)); j++)
        for (int k = i; k < int(i + (1 << (d - 1))); k++)
          dp[d][j] = max(
              dp[d][j], P[d][j] * (1 << (d - 1)) + dp[d - 1][j] + dp[d - 1][k]);
    }
  double ans = 0.0;
  for (int i = 0; i < int((1 << n)); i++) ans = max(ans, dp[n][i]);
  printf("%.10lf\n", ans);
  return 0;
}
