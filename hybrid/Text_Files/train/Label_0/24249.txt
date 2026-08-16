#include <bits/stdc++.h>
signed main() {
  long long n, m, c1 = 0, c2 = 0, t1, t2, i;
  scanf("%lld%lld", &n, &m);
  for (i = 1; i <= m; i++) {
    scanf("%lld%lld", &t1, &t2);
    c1 += t1 * t2;
    c2 += t2;
  }
  if (c2 > n)
    printf("-1\n");
  else if (c2 == n) {
    if (((1 + n) * n / 2) % n != c1 % n)
      printf("-1\n");
    else
      printf("1\n");
  } else
    printf("1\n");
  return 0;
}
