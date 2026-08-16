#include <bits/stdc++.h>
using namespace std;
const int N = 55;
int n, m, a[N], sum;
double dp[N][N], C[N][N], ans;
double qpow(double x, int y) {
  double res = 1;
  for (int i = (1), iE = (y); i <= iE; i++) res = res * x;
  return res;
}
double solve(int x) {
  double res = 1;
  int qz = 0;
  memset(dp, 0, sizeof(dp));
  dp[0][0] = 1;
  for (int i = (1), iE = (m); i <= iE; i++)
    for (int j = (0), jE = (n); j <= jE; j++)
      for (int k = (0), kE = (min(a[i] * x, j)); k <= kE; k++)
        dp[i][j] += dp[i - 1][j - k] * C[j][k];
  return 1 - dp[m][n] / qpow(m, n);
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = (0), iE = (n); i <= iE; i++) C[i][0] = 1;
  for (int i = (1), iE = (n); i <= iE; i++)
    for (int j = (1), jE = (i); j <= jE; j++)
      C[i][j] = C[i - 1][j] + C[i - 1][j - 1];
  for (int i = (1), iE = (m); i <= iE; i++) scanf("%d", &a[i]), sum += a[i];
  for (int i = (0), iE = (n); i <= iE; i++) ans += solve(i);
  printf("%.12lf\n", ans);
  return 0;
}
