#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, max = -1000000000, cur, pl, min, a, b, c, d, e;
  char s[25], maxs[25];
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%s", s);
    scanf("%d%d%d%d%d%d%d", &pl, &min, &a, &b, &c, &d, &e);
    cur = pl * 100 - min * 50 + a + b + c + d + e;
    if (cur > max) {
      memcpy(maxs, s, sizeof(s));
      max = cur;
    }
  }
  printf("%s\n", maxs);
  return 0;
}
