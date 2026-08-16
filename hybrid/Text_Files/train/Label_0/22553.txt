#include <bits/stdc++.h>
int main() {
  unsigned long long n, i, c = 0;
  scanf("%llu", &n);
  if (n < 2520) {
    printf("0\n");
  } else {
    printf("%llu\n", n / 2520);
  }
  return 0;
}
