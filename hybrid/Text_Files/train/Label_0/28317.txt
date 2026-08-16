#include <bits/stdc++.h>
using namespace std;
const int MAX_N = 200000;
pair<double, double> lrs[MAX_N];
int fss[MAX_N + 1];
int main() {
  int sy, a, b, n;
  scanf("%d%d%d%d", &sy, &a, &b, &n);
  for (int i = 0; i < n; i++) {
    int l, r;
    scanf("%d%d", &l, &r);
    lrs[i] = pair<double, double>(l, r);
    fss[i + 1] = fss[i] + (r - l);
  }
  int q;
  scanf("%d", &q);
  while (q--) {
    int x, y;
    scanf("%d%d", &x, &y);
    double xa = x + (double)(a - x) * y / (y - sy);
    double xb = x + (double)(b - x) * y / (y - sy);
    int ka = lower_bound(lrs, lrs + n, pair<double, double>(xa, xa)) - lrs;
    int kb = lower_bound(lrs, lrs + n, pair<double, double>(xb, xb)) - lrs;
    double sum = fss[kb] - fss[ka];
    if (kb > 0 && xb < lrs[kb - 1].second) sum -= (lrs[kb - 1].second - xb);
    if (ka > 0 && xa < lrs[ka - 1].second) sum += (lrs[ka - 1].second - xa);
    double t = sum * (b - a) / (xb - xa);
    printf("%.10lf\n", t);
  }
  return 0;
}
