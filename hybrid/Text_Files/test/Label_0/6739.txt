#include <bits/stdc++.h>
using namespace std;
int dx[] = {0, 0, +1, -1};
int dy[] = {+1, -1, 0, 0};
double value(double n) { return (n * (3.1416 / 180.00)); }
int main() {
  int tc;
  cin >> tc;
  while (tc--) {
    double n, kona, angle, b, x, ans = 1.0, a;
    cin >> n;
    kona = int(n - 1) / 2;
    angle = (180.0 / n) * kona;
    b = sqrt(1.0 / (2.0 * (1.0 - cos(value(180.0 / n)))));
    x = sqrt(2.00 * b * b * (1 - cos(value(angle))));
    a = sqrt((x * x) / 2.00);
    ans += (2.0 * a);
    printf("%.15lf\n", ans);
  }
  return 0;
}
