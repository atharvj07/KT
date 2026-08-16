#include <bits/stdc++.h>
using namespace std;
double transformx(double r, double x, double y) {
  return (r * r * x) / (x * x + y * y);
}
double transformy(double r, double x, double y) {
  return (r * r * y) / (x * x + y * y);
}
inline double sqr(double x) { return x * x; }
double dist(double x0, double y0, double x1, double y1) {
  return sqrt(sqr(x0 - x1) + sqr(y0 - y1));
}
struct circle {
  complex<double> c;
  double r;
};
circle get_circle(complex<double> a, complex<double> b, complex<double> c) {
  complex<double> x = 1.0 / conj(b - a), y = 1.0 / conj(c - a);
  complex<double> t = (y - x) / (conj(x) * y - x * conj(y)) + a;
  return {t, abs(a - t)};
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.setf(ios_base::fixed);
  cout.precision(17);
  double R, r;
  int k;
  cin >> k;
  while (cin >> R >> r >> k) {
    double invr = 1;
    double xleft = transformx(invr, 2 * R, 0);
    double xright = transformx(invr, 2 * r, 0);
    double d = xright - xleft;
    double h = d * k;
    complex<double> p1(transformx(invr, xleft, h), transformy(invr, xleft, h));
    complex<double> p2(transformx(invr, xright, h),
                       transformy(invr, xright, h));
    complex<double> p3(transformx(invr, xleft + d / 2, h + d / 2),
                       transformy(invr, xleft + d / 2, h + d / 2));
    cout << get_circle(p1, p2, p3).r << '\n';
  }
}
