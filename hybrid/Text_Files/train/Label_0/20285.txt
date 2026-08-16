#include <bits/stdc++.h>
using namespace std;
const int sigma_size = 26;
const int N = 100 + 50;
const int MAXN = 100000 + 50;
const int inf = 0x3fffffff;
const double eps = 1e-8;
const int mod = 1000000000 + 7;
int n, k;
int a[N];
double dp[N][N], res[N][N];
int main() {
  while (~scanf("%d%d", &n, &k)) {
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= n; i++)
      for (int j = i + 1; j <= n; j++) dp[i][j] = 1;
    while (k--) {
      memcpy(res, dp, sizeof(dp));
      memset(dp, 0, sizeof(dp));
      for (int l = 1; l <= n; l++)
        for (int r = l; r <= n; r++) {
          for (int i = 1; i <= n; i++)
            for (int j = i + 1; j <= n; j++) {
              int x = i, y = j;
              if (l <= x && x <= r) x = l + r - x;
              if (l <= y && y <= r) y = l + r - y;
              if (x > y) swap(x, y);
              if (l <= x && y <= r)
                dp[x][y] += (1 - res[i][j]) * 2.0 / (n + 1) / n;
              else
                dp[x][y] += res[i][j] * 2.0 / (n + 1) / n;
            }
        }
    }
    double ans = 0;
    for (int i = 1; i <= n; i++)
      for (int j = i + 1; j <= n; j++)
        if (a[i] > a[j])
          ans += dp[i][j];
        else
          ans += 1.0 - dp[i][j];
    printf("%.10f\n", ans);
  }
  return 0;
}
