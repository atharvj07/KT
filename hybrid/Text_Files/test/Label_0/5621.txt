#include <bits/stdc++.h>
using namespace std;
double a[4444];
int n;
int main() {
  double ans = 0;
  scanf("%d", &n);
  int free = 0;
  for (int i = 0; i < 2 * n; ++i) {
    double x;
    scanf("%lf", &x);
    double xx = x - floor(x);
    ans += xx;
    if (abs(xx) < 1e-9) free++;
  }
  double ret = 1e20;
  for (int i = max(0, n - free); i <= n; ++i) ret = min(ret, abs(ans - i));
  printf("%.3lf\n", ret);
}
