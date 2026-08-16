#include <bits/stdc++.h>
using namespace std;
const int INF = 2147483647;
const long long LLINF = 9223372036854775807LL;
int main() {
  int n, m, k;
  scanf("%d%d%d", &n, &m, &k);
  double ans = 1;
  for (int i = 0; i <= k; ++i) ans *= (m - i + .0) / (n + i + 1.);
  ans = 1 - ans;
  ans = max(0., ans);
  printf("%.15lf\n", ans);
  return 0;
}
