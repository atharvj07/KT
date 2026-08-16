#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, d, h;
  scanf("%d %d %d", &n, &d, &h);
  if (2 * h < d || (n > 2 && d == 1)) {
    printf("-1");
    return 0;
  }
  for (int i = 1; i < h + 1; i++) printf("%d %d\n", i, i + 1);
  if (d > h) {
    printf("%d %d\n", 1, h + 2);
  }
  for (int i = h + 3; i < d + 2; i++) printf("%d %d\n", i - 1, i);
  for (int i = d + 2; i < n + 1; i++) printf("%d %d\n", h, i);
  return 0;
}
