#include <bits/stdc++.h>
double ans;
int n, i, j;
double p;
char a[220000], b[220000], k;
double sqr(double x) { return x * x; }
int main() {
  scanf("%d", &n);
  ans = 0;
  scanf("%s", &a);
  scanf("%s", &b);
  for (k = 'A'; k <= 'Z'; k++) {
    j = n - 1;
    p = 0;
    for (i = n - 1; i >= 0; i--) {
      if (a[i] != k) continue;
      while (j >= i) {
        if (b[j] == k) p += n - j;
        j--;
      }
      ans += p * (i + 1);
    }
    j = n - 1;
    p = 0;
    for (i = n - 1; i >= 0; i--) {
      if (b[i] != k) continue;
      while (j > i) {
        if (a[j] == k) p += n - j;
        j--;
      }
      ans += p * (i + 1);
    }
  }
  ans = ans / (n * 1.0 * (n + 1) * (2.0 * n + 1) / 6.0);
  printf("%.10f\n", ans);
  return 0;
}
