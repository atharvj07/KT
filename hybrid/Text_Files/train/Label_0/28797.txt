#include <bits/stdc++.h>
const int maxn = 15;
int num[maxn];
int main() {
  int n, m, i, j, count, book, temp;
  while (scanf("%d%d", &n, &m) == 2) {
    memset(num, 0, sizeof(num));
    for (i = 0; i < n; ++i) {
      scanf("%d", &book);
      num[book]++;
    }
    count = 0;
    for (i = 1; i < m; ++i) {
      for (j = i + 1; j <= m; ++j) count += num[i] * num[j];
    }
    printf("%d\n", count);
  }
  return 0;
}
