#include <bits/stdc++.h>
using namespace std;
long long f[2][55][55], c[55][55];
int n, p;
int main() {
  int i, j, k, x;
  for (i = 1; i <= 50; i++) {
    c[i][0] = c[i][i] = 1;
    for (j = 1; j < i; j++) {
      c[i][j] = c[i - 1][j] + c[i - 1][j - 1];
    }
  }
  int pre = 0, cur = 1;
  f[0][0][0] = 1;
  scanf("%d", &n);
  for (i = 0; i < n; i++) {
    scanf("%d", &x);
    for (j = 0; j <= 50; j++)
      for (k = 0; k <= 50; k++) {
        if (k + x <= 50) f[cur][j + 1][k + x] += f[pre][j][k];
        f[cur][j][k] += f[pre][j][k];
      }
    pre ^= 1;
    cur ^= 1;
    memset(f[cur], 0, sizeof(f[cur]));
  }
  for (i = 0; i <= 50; i++)
    for (j = 1; j <= 50; j++) {
      f[pre][i][j] += f[pre][i][j - 1];
    }
  scanf("%d", &p);
  double ans = 0;
  for (i = 1; i <= n; i++) ans += f[pre][i][p] * 1.0 / c[n][i];
  printf("%.7lf\n", ans);
  return 0;
}
