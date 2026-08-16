#include <bits/stdc++.h>
using namespace std;
int n, m, fa[500005][21], l, r;
int main() {
  scanf("%d%d", &n, &m);
  while (n--) scanf("%d%d", &l, &r), fa[l][0] = max(fa[l][0], r);
  for (int i = 1; i < 500005; i++) fa[i][0] = max(fa[i][0], fa[i - 1][0]);
  for (int j = 1; j <= 20; j++)
    for (int i = 0; i < 500005; i++) fa[i][j] = fa[fa[i][j - 1]][j - 1];
  while (m--) {
    int x, y, ans = 1;
    scanf("%d%d", &x, &y);
    for (int i = 20; i >= 0; i--)
      if (fa[x][i] < y) ans += (1 << i), x = fa[x][i];
    if (fa[x][0] < y) ans = -1;
    printf("%d\n", ans);
  }
  return 0;
}
