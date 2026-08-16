#include <bits/stdc++.h>
int cmp(const void *a, const void *b) { return *(int *)b - *(int *)a; }
int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  int a[n], b[m];
  for (int i = 0; i < n; i++) scanf("%d", &a[i]);
  for (int i = 0; i < m; i++) scanf("%d", &b[i]);
  qsort(b, m, sizeof(b[0]), cmp);
  for (int i = 0; i < n; i++) {
    int k = 0;
    if (a[i] == 0) {
      a[i] = b[k];
      k++;
    }
  }
  int flag = 0;
  for (int i = 0; i < n - 1; i++) {
    if (a[i] >= a[i + 1]) flag = 1;
  }
  if (flag == 1)
    printf("YES");
  else
    printf("NO\n");
}
