#include <bits/stdc++.h>
const int maxn = 2010;
const int inf = 0x3f3f3f3f;
int a[maxn];
int min(int a, int b) { return a > b ? b : a; }
int gcd(int a, int b) { return a == 0 ? b : gcd(b % a, a); }
int main() {
  int n, l, r, i, j, tmp;
  while (~scanf("%d", &n)) {
    int cnt = 0;
    for (i = 0; i < n; i++) {
      scanf("%d", &a[i]);
      if (a[i] == 1) cnt++;
    }
    if (cnt) {
      printf("%d\n", n - cnt);
      continue;
    }
    int mina = inf;
    for (i = 0; i < n; i++) {
      tmp = a[i];
      for (j = i + 1; j < n; j++) {
        tmp = gcd(tmp, a[j]);
        if (tmp == 1) {
          l = i;
          r = j;
          mina = min(mina, r - l);
          break;
        }
      }
    }
    if (mina != inf)
      printf("%d\n", mina + n - 1);
    else
      printf("-1\n");
  }
  return 0;
}
