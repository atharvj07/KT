#include <bits/stdc++.h>
int main() {
  long long p, q, i, j, I, J;
  scanf("%I64d", &q);
  I = sqrt(q);
  for (i = 2LL; i <= I; ++i) {
    if (q % i == 0LL) {
      p = q / i;
      J = sqrt(p);
      for (j = 2LL; j <= J; ++j) {
        if (p % j == 0LL) {
          printf("1\n%I64d\n", i * j);
          return 0;
        }
      }
      puts("2");
      return 0;
    }
  }
  puts("1\n0\n");
  return 0;
}
