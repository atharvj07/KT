#include <bits/stdc++.h>
int main() {
  int a, b, c, d, e, f, i, j, k, p, q, sum = 0, flag = 0, ct1 = -1, ct2 = 0;
  char x[110][110];
  int y[110];
  scanf("%d %d", &a, &b);
  for (i = 0; i < a; i++) {
    scanf("%s", x[i]);
  }
  for (j = 0; j < b; j++) {
    flag = 0;
    ct2 = 0;
    for (i = 1; i < a; i++) {
      if (x[i][j] < x[i - 1][j] && ct1 < 0) {
        flag = 1;
      } else if (x[i][j] < x[i - 1][j] && ct1 >= 0) {
        for (k = 0; k <= ct1; k++) {
          if (x[i - 1][y[k]] >= x[i][y[k]]) {
            ct2 = 1;
          } else if (x[i - 1][y[k]] < x[i][y[k]]) {
            ct2 = 0;
            break;
          }
        }
      }
      if (ct2 == 1) flag = 1;
    }
    if (flag == 1) {
      sum++;
    } else {
      ct1++;
      y[ct1] = j;
    }
  }
  printf("%d", sum);
  return 0;
}
