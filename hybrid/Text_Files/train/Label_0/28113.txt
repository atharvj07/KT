#include <bits/stdc++.h>
int main() {
  int n, count = 0, i;
  scanf("%d", &n);
  for (i = 1; i < n; i++) {
    if ((n - i) % i == 0) {
      count++;
    }
  }
  printf("%d\n", count);
  return 0;
}
