#include <bits/stdc++.h>
using namespace std;
const int N = 6e4 + 10;
int n;
double x[N], v[N];
double l = 0, r = 1e9;
int pd(double t) {
  double l = 0, r = 1e9;
  for (int i = 1; i <= n; i++) {
    double ll = x[i] - v[i] * t, rr = x[i] + v[i] * t;
    if (ll <= r)
      l = max(l, ll);
    else
      return 0;
    if (rr >= l)
      r = min(r, rr);
    else
      return 0;
  }
  return 1;
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%lf", &x[i]);
  for (int i = 1; i <= n; i++) scanf("%lf", &v[i]);
  while (r - l > 1e-6) {
    double mid = (l + r) / 2.0;
    int flag = pd(mid);
    if (flag)
      r = mid;
    else
      l = mid;
  }
  printf("%.12lf", l);
  return 0;
}
