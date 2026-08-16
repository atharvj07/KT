#include <bits/stdc++.h>
int main() {
  long int num = 0, n, a = 0, b = 0, i;
  scanf("%ld%ld", &a, &b);
  while (b--) {
    if (a % 10 == 0) {
      a = a / 10;
    } else if (a % 10 != 0) {
      a--;
    }
  }
  printf("%ld\n", a);
  return 0;
}
