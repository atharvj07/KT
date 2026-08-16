#include <bits/stdc++.h>
using namespace std;
int x, y, a, b, n;
void init() {
  scanf("%d", &n);
  puts("YES");
  for (int i = 1; i <= n; i++) {
    scanf("%d%d%d%d", &x, &y, &a, &b);
    printf("%d\n", 2 * abs(x % 2) + abs(y % 2) + 1);
  }
}
int main() {
  init();
  return 0;
}
