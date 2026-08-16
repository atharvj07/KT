#include <bits/stdc++.h>
using namespace std;
const int N = 2000;
int pl, pr, vl, vr, k, n;
long long a[N];
double res;
void Dfs(int u, int v, long long s) {
  if (u > v) {
    ++n;
    a[n] = s;
    return;
  }
  Dfs(u + 1, v, s * 10 + 4);
  Dfs(u + 1, v, s * 10 + 7);
}
inline long long Calc(long long x, long long y, long long xx, long long yy) {
  if (y < xx) return 0;
  if (yy < x) return 0;
  return min(y, yy) - max(x, xx) + 1;
}
int main() {
  scanf("%d%d%d%d%d", &pl, &pr, &vl, &vr, &k);
  for (int i = 1; i <= 9; i++) Dfs(1, i, 0);
  sort(a + 1, a + 1 + n);
  res = 0;
  a[0] = 0;
  a[1023] = 2147483647;
  for (int i = 1; i + k - 1 <= n; i++) {
    res += (double)(Calc(a[i - 1] + 1, a[i], pl, pr)) / (double)(pr - pl + 1) *
           (double)(Calc(a[i + k - 1], a[i + k] - 1, vl, vr)) /
           (double)(vr - vl + 1);
    res += (double)(Calc(a[i - 1] + 1, a[i], vl, vr)) / (double)(vr - vl + 1) *
           (double)(Calc(a[i + k - 1], a[i + k] - 1, pl, pr)) /
           (double)(pr - pl + 1);
    if (k == 1 && a[i] >= pl && a[i] <= pr && a[i] >= vl && a[i] <= vr)
      res -= (double)(1) / (double)(pr - pl + 1) / (double)(vr - vl + 1);
  }
  printf("%.12lf\n", res);
  return 0;
}
