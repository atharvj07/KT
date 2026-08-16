#include <bits/stdc++.h>
const int N = 2010;
const double pi = acos(-1), zero = 1e-6;
int n, sum, lx, ly, f[N][N], w[N][N];
bool vis[N][N];
void work(int x, int y) {
  if (!w[x][y] || vis[x][y]) return;
  sum++;
  vis[x][y] = true;
  if (x > lx || (x == lx && y > ly)) {
    lx = x;
    ly = y;
  }
  work(x - 1, y);
  work(x, y - 1);
  work(x + 1, y);
  work(x, y + 1);
}
int main() {
  int i, j, k, l, s, ans1 = 0, ans2 = 0;
  double d, delta1, delta2;
  scanf("%d", &n);
  for (i = 1; i <= n; i++)
    for (j = 1; j <= n; j++) scanf("%d", &f[i][j]);
  memset(w, 0, sizeof(w));
  for (i = 3; i <= n - 2; i++)
    for (j = 3; j <= n - 2; j++) {
      s = 0;
      for (k = i - 2; k <= i + 2; k++)
        for (l = j - 2; l <= j + 2; l++) s += f[k][l];
      if (s >= 15) w[i - 2][j - 2] = 1;
    }
  memset(vis, false, sizeof(vis));
  for (i = 1; i <= n - 4; i++)
    for (j = 1; j <= n - 4; j++)
      if (w[i][j] && !vis[i][j]) {
        lx = i;
        ly = j;
        sum = 0;
        work(i, j);
        d = sqrt((lx - i) * (lx - i) + (ly - j) * (ly - j));
        if (d >= 10) {
          delta1 = fabs(d * d * 0.25 * pi - sum);
          delta2 = fabs(d * d * 0.5 - sum);
          if (delta1 < delta2 + zero)
            ans1++;
          else
            ans2++;
        }
      }
  printf("%d %d", ans1, ans2);
}
