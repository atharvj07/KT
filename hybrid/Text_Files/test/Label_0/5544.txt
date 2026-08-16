#include <bits/stdc++.h>
double ara[11][11];
int main() {
  int n, i, j, t, x, count = 0;
  scanf("%d %d", &n, &t);
  for (x = 1; x <= t; x++) {
    ara[1][1]++;
    for (i = 1; i <= n; i++) {
      for (j = 1; j <= n; j++) {
        if (ara[i][j] > 1) {
          ara[i + 1][j] += ((ara[i][j] - 1) / 2.0);
          ara[i][j + 1] += ((ara[i][j] - 1) / 2.0);
          ara[i][j] = 1;
        }
      }
    }
  }
  for (i = 1; i <= n; i++) {
    for (j = 1; j <= n; j++) {
      if (i + j <= (n + 1)) {
        if (ara[i][j] >= 1) count++;
      }
    }
  }
  printf("%d\n", count);
  return 0;
}
