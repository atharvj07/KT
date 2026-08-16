#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e+4;
const int MAXM = 1e+5;
const int INF = numeric_limits<int>::max();
const long long LL_INF = numeric_limits<long long>::max();
int main() {
  double n, l, v1, v2, k;
  while (~scanf("%lf%lf%lf%lf%lf", &n, &l, &v1, &v2, &k)) {
    double c = ceil(n / k);
    double bl = l * (v1 + v2) / (v1 + v2 + 2 * (c - 1) * v1);
    double t = bl / v2 + (l - bl) / v1;
    printf("%.6lf\n", t);
  }
  return 0;
}
