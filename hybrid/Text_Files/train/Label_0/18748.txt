#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, a, b, i, j, p;
  scanf("%d%d%d", &a, &b, &n);
  for (p = a * 10, i = 0; i < 10; i++, p++) {
    if (p % b == 0) break;
  }
  if (i == 10) {
    printf("-1\n");
    return 0;
  }
  printf("%d", p);
  for (i = 0; i < n - 1; i++) printf("0");
  printf("\n");
  return 0;
}
