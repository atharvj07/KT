#include <bits/stdc++.h>
int main() {
  int n, o = 0, x, y, v, cnt = 0, f = 0, a, p = 2;
  scanf("%d%d%d", &n, &x, &y);
  while (p <= n) {
    p = p * 2;
    f++;
  }
  if (y > x) {
    a = x;
    x = y;
    y = a;
  }
  while (1) {
    v = (n + o) / 2;
    if ((x > v && y <= v)) {
      break;
    }
    if (x <= v) {
      n = v;
    } else if (y > v) {
      o = v;
    }
    cnt++;
  }
  if (cnt == 0) {
    printf("Final!");
  } else {
    printf("%d", f - cnt);
  }
}
