#include <bits/stdc++.h>
using namespace std;
int Q, r, v, x, y;
const double eps = 1e-7;
bool check(double x, double L) {
  double tmp = x / r;
  return (x + 2 * r * fabs(sin(tmp / 2)) - L > eps);
}
int main() {
  scanf("%d%d%d", &Q, &r, &v);
  while (Q--) {
    scanf("%d%d", &x, &y);
    double L = 0, R = y - x, ans = 0;
    for (int i = 1; i <= 200; ++i) {
      double mid = (L + R) / 2;
      if (check(mid, y - x))
        ans = mid, R = mid;
      else
        L = mid;
    }
    printf("%.7lf\n", ans / v);
  }
}
