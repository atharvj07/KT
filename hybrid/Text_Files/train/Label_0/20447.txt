#include <bits/stdc++.h>
int vx[50007], vy[50007], vl[50007];
int hx[50007], hy[50007], hl[50007];
int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) {
    scanf("%d %d %d", vx + i, vy + i, vl + i);
  }
  int ans = 0;
  for (int i = 0; i < m; i++) {
    scanf("%d %d %d", hx + i, hy + i, hl + i);
    for (int j = 0; j < n; j++) {
      if (vx[j] >= hx[i] && vx[j] <= hx[i] + hl[i] && hy[i] >= vy[j] &&
          hy[i] <= vy[j] + vl[j]) {
        const int r =
            std::min(std::min(std::min(hy[i] - vy[j], vy[j] + vl[j] - hy[i]),
                              vx[j] - hx[i]),
                     hx[i] + hl[i] - vx[j]);
        if (r > ans) {
          ans = r;
        }
      }
    }
  }
  printf("%d", ans);
  return 0;
}
