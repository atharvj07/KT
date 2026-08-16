#include <bits/stdc++.h>
using namespace std;
bool debug = 1;
int n, m, k;
int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};
long long ln, lk, lm;
int main() {
  scanf("%d%d", &m, &n);
  double pre = 0, ans = 0;
  for (int i = m; i >= 2; i--) {
    double cur = 1.0 - pow(1.0 * (i - 1) / m, n) - pre;
    ans += cur * i;
    pre += cur;
  }
  ans += pow(1.0 / m, n);
  printf("%.10lf\n", ans);
  return 0;
}
