#include <bits/stdc++.h>
using namespace std;
double binPow(double x, int k) {
  double res = 1;
  while (k) {
    if (k & 1) res *= x;
    x *= x;
    k >>= 1;
  }
  return res;
}
int main() {
  int n, m;
  double ans = 0;
  cin >> m >> n;
  for (int i = 1; i <= m; i++)
    ans += i * (binPow((i + .0) / m, n) - binPow((i - 1 + .0) / m, n));
  printf("%.10lf", ans);
  return 0;
}
