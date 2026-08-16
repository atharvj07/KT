#include <bits/stdc++.h>
int main() {
  long long int n, m, a, b, ans1, ans2, i, p;
  scanf("%I64d%I64d%I64d%I64d", &n, &m, &a, &b);
  if (n % m == 0) {
    printf("");
  }
  if (n < m) {
    ans1 = ((m - n) * a);
    ans2 = n * b;
  } else {
    ans1 = (n % m) * b;
    ans2 = ((((n / m) + 1) * m) - n) * a;
  }
  if (ans1 < ans2)
    printf("%I64d", ans1);
  else
    printf("%I64d", ans2);
  return 0;
}
