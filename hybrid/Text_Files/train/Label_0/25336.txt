#include <bits/stdc++.h>
using namespace std;
double a[int(1e6)];
int n;
double sum(double x) {
  double res = -1e15, max_sum = 0, min_sum = 0, s = 0;
  for (int i = 1; i <= n; i++) {
    s += a[i] - x;
    res = max(res, fabs(s - min_sum));
    res = max(res, fabs(s - max_sum));
    max_sum = max(max_sum, s);
    min_sum = min(min_sum, s);
  }
  return res;
}
void sinus() {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
  }
  double l = -1e5, r = 1e5;
  for (int i = 1; i <= 100; i++) {
    double m1 = l + (r - l) / 3;
    double m2 = r - (r - l) / 3;
    if (sum(m1) < sum(m2))
      r = m2;
    else
      l = m1;
  }
  printf("%.6f", sum(l));
}
int main() {
  ios::sync_with_stdio(false);
  sinus();
}
