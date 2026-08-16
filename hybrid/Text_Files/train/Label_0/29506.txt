#include <bits/stdc++.h>
const int N = 405, inf = 1000000007;
using namespace std;
int g[N], f[N][N][2], n, a[N], v[N];
void dp() {
  for (int i = 1; i <= n; ++i) {
    f[i][i][0] = 0;
    f[i][i][1] = v[1];
  }
  for (int L = 2; L <= n; ++L)
    for (int l = 1; l <= n - L + 1; ++l) {
      int r = l + L - 1;
      f[l][r][0] = -inf;
      if (a[l] != a[r]) {
        int st = (a[l] < a[r] ? 1 : -1);
        for (int k = l + 1; k <= r; ++k)
          if (a[k] == a[l] + st)
            f[l][r][0] = max(f[l][r][0], f[l + 1][k - 1][1] + f[k][r][0]);
      }
      f[l][r][1] = -inf;
      for (int k = l; k <= r - 1; ++k)
        f[l][r][1] = max(f[l][r][1], f[l][k][1] + f[k + 1][r][1]);
      for (int k = l; k <= r; ++k)
        if (a[l] <= a[k] && a[r] <= a[k] && a[k] - a[l] + a[k] - a[r] + 1 <= n)
          f[l][r][1] = max(f[l][r][1], f[l][k][0] + f[k][r][0] +
                                           v[a[k] - a[l] + a[k] - a[r] + 1]);
    }
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &v[i]);
  }
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &a[i]);
  }
  dp();
  g[0] = 0;
  for (int i = 1; i <= n; ++i) {
    g[i] = g[i - 1];
    for (int j = 0; j <= i - 1; ++j) g[i] = max(g[i], g[j] + f[j + 1][i][1]);
  }
  printf("%d\n", g[n]);
  return 0;
}
