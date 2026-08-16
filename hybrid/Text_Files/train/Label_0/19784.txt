#include <bits/stdc++.h>
using namespace std;
int n, m[15];
double x[15], v[15], t, v1, v2, now, pre, tmp, eps = 1e-10;
int main() {
  scanf("%d%lf", &n, &t);
  for (int i = 1; i <= n; i++) scanf("%lf%lf%d", &x[i], &v[i], &m[i]);
  for (;;) {
    now = 2 * t;
    for (int i = 1; i <= n; i++)
      for (int j = i + 1; j <= n; j++) {
        if (fabs(x[i] - x[j]) < eps || fabs(v[i] - v[j]) < eps) continue;
        tmp = (x[j] - x[i]) / (v[i] - v[j]);
        if (tmp < eps) continue;
        now = min(now, tmp);
      }
    if (now + pre > t) break;
    pre += now;
    for (int i = 1; i <= n; i++) x[i] += now * v[i];
    for (int i = 1; i <= n; i++)
      for (int j = i + 1; j <= n; j++)
        if (fabs(x[i] - x[j]) < eps) {
          v1 = v[i], v2 = v[j];
          v[i] = ((m[i] - m[j]) * v1 + 2 * m[j] * v2) / (m[i] + m[j]);
          v[j] = ((m[j] - m[i]) * v2 + 2 * m[i] * v1) / (m[i] + m[j]);
        }
  }
  now = t - pre;
  for (int i = 1; i <= n; i++) printf("%.12lf\n", x[i] + v[i] * now);
}
