#include <bits/stdc++.h>
using namespace std;
int n, len, v1, v2, k;
double solve(double l, double r) {
  for (int i = 0; i < (100); i++) {
    double mid = (l + r) / 2;
    double t2 = (len * 1.0 - v1 * 1.0 * mid) / (v2 - v1);
    double d = t2 * v2;
    int cnt = (n - 1) / k + 1;
    double tback = (v2 - v1 * 1.0) / (v1 + v2) * t2;
    if (cnt * d - (cnt - 1) * tback * v2 <= len)
      r = mid;
    else
      l = mid;
  }
  return l;
}
int main() {
  scanf("%d%d%d%d%d", &n, &len, &v1, &v2, &k);
  printf("%.10f\n", solve(len * 1.0 / v2, len * 1.0 / v1));
  return 0;
}
