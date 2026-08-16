#include <bits/stdc++.h>
using namespace std;
template <typename T, typename TT>
ostream& operator<<(ostream& s, pair<T, TT> t) {
  return s << "(" << t.first << "," << t.second << ")";
}
template <typename T>
ostream& operator<<(ostream& s, vector<T> t) {
  for (int i = 0; i < t.size(); i++) s << t[i] << " ";
  return s;
}
double a, b, len;
const double eps = 1e-10;
double cal(double first) {
  double w;
  double p = acos(first / len), q = atan2(a, b - first), d = a / sin(q);
  w = d * sin(q + p);
  return w;
}
double check() {
  double l = 0, r = len;
  while (r - l > eps) {
    double x1 = (2. * l + r) / 3.;
    double x2 = (2. * r + l) / 3.;
    if (cal(x1) + eps > cal(x2))
      l = x1;
    else
      r = x2;
  }
  return cal((l + r + eps) / 2.);
}
int main() {
  int i, j, T, k, n;
  while (~scanf("%lf%lf%lf", &a, &b, &len)) {
    if (a > b) swap(a, b);
    if (len <= b) {
      printf("%lf\n", min(a, len));
      continue;
    }
    double ans = min(min(a, b), len);
    ans = min(ans, check());
    if (ans < 1e-8)
      puts("My poor head =(");
    else
      printf("%.12lf\n", ans);
  }
  return 0;
}
