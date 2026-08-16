#include <bits/stdc++.h>
int main() {
  int a, b, i, j, count, n;
  scanf("%d %d", &a, &b);
  for (i = a, count = 0; i <= b; i++) {
    for (n = i; n != 0;) {
      j = n % 10;
      if (j == 0 || j == 6 || j == 9) {
        count = count + 6;
      } else if (j == 1) {
        count = count + 2;
      } else if (j == 2 || j == 3 || j == 5) {
        count = count + 5;
      } else if (j == 4) {
        count = count + 4;
      } else if (j == 7) {
        count = count + 3;
      } else {
        count = count + 7;
      }
      n = (n - j) / 10;
    }
  }
  printf("%d", count);
}
