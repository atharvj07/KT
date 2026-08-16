#include <bits/stdc++.h>
int vis[111];
int a[111];
int main() {
  int i, j, n;
  int v;
  while (scanf("%d", &n) != EOF) {
    memset(vis, -1, sizeof(vis));
    int flag = 0;
    int tt = 0;
    for (i = 1; i <= n; i++) {
      scanf("%d", &v);
      if (v == 100)
        vis[1] = 100;
      else if (v == 0)
        vis[4] = 0;
      else if (v < 10)
        vis[3] = v;
      else {
        if (!flag) {
          if (v % 10 == 0) {
            vis[2] = v;
            flag = 1;
          } else
            vis[2] = v;
        }
      }
    }
    int tot = 0;
    if (vis[1] != -1) {
      a[++tt] = 100;
    }
    if (vis[4] != -1) {
      a[++tt] = 0;
    }
    if (vis[3] != -1 && vis[2] != -1) {
      if (vis[2] % 10 == 0) {
        tot = 1;
        a[++tt] = vis[3];
        a[++tt] = vis[2];
      }
    }
    if (!tot) {
      if (vis[3] != -1)
        a[++tt] = vis[3];
      else if (vis[2] != -1)
        a[++tt] = vis[2];
    }
    printf("%d\n", tt);
    for (i = 1; i <= tt; i++) printf("%d ", a[i]);
    if (tt > 0) printf("\n");
  }
  return 0;
}
