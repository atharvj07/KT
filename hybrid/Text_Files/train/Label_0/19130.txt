#include <bits/stdc++.h>
int n, k, d, tot, a[1010], ans[1010][1010];
void tr(int x) {
  if (x > d) {
    ++tot;
    for (int i = 1; i <= d; ++i) ans[i][tot] = a[i];
    return;
  }
  for (int i = 1; i <= k; ++i) {
    a[x] = i;
    tr(x + 1);
    if (tot >= n) return;
  }
}
int main() {
  scanf("%d%d%d", &n, &k, &d);
  tr(1);
  if (tot < n)
    printf("-1\n");
  else {
    for (int i = 1; i <= d; ++i) {
      for (int j = 1; j <= n; ++j) {
        printf("%d", ans[i][j]);
        if (j == n)
          printf("\n");
        else
          printf(" ");
      }
    }
  }
  return 0;
}
