#include <bits/stdc++.h>
using namespace std;
const double eps = 1e-9;
int main() {
  int n, i, j, camp;
  double t, tmin, x[11], v[11], w[11], temp, vi, vj;
  cin >> n >> t;
  for (i = 0; i < n; i++) cin >> x[i] >> v[i] >> w[i];
  camp = 1;
  while (camp) {
    tmin = 100000;
    for (i = 0; i < n; i++)
      for (j = 0; j < n; j++) {
        if (abs(x[i] - x[j]) > eps && abs(v[i] - v[j]) > eps) {
          temp = (x[i] - x[j]) / (v[j] - v[i]);
          if ((temp < tmin) && (temp > 0)) tmin = temp;
        }
      }
    if (tmin >= t)
      camp = 0;
    else {
      t -= tmin;
      for (i = 0; i < n; i++) x[i] += v[i] * tmin;
      for (i = 0; i < n; i++)
        for (j = 0; j < i; j++)
          if (abs(x[i] - x[j]) < eps) {
            vi = ((w[i] - w[j]) * v[i] + 2 * w[j] * v[j]) / (w[i] + w[j]);
            vj = ((w[j] - w[i]) * v[j] + 2 * w[i] * v[i]) / (w[i] + w[j]);
            v[i] = vi;
            v[j] = vj;
          }
    }
  }
  for (i = 0; i < n; i++) x[i] += v[i] * t;
  for (j = 0; j < n; j++) printf("%.9lf\n", x[j]);
  return 0;
}
