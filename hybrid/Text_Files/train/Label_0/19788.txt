#include <bits/stdc++.h>
using namespace std;
const int N = 111;
const double INF = 1e9;
const double eps = 0.000001;
int n;
double v[N], x[N], m[N], f[N], t;
void newV(double &v1, double m1, double &v2, double m2) {
  double tmp1 = v1, tmp2 = v2;
  v1 = 1.0 * ((m1 - m2) * tmp1 + 2 * m2 * tmp2) / (m1 + m2);
  v2 = 1.0 * ((m2 - m1) * tmp2 + 2 * m1 * tmp1) / (m1 + m2);
}
double getT(double v1, double x1, double v2, double x2) {
  if (x1 > x2) swap(x1, x2), swap(v1, v2);
  if (v1 < 0) {
    if (v2 > v1) return INF;
    return (x2 - x1) / (v1 - v2);
  } else {
    if (v2 > v1) return INF;
    return (x2 - x1) / (v1 - v2);
  }
}
bool visited[N];
void solve() {
  cin >> n >> t;
  for (int i = 1; i <= n; ++i) {
    cin >> x[i] >> v[i] >> m[i];
  }
  double Prev = 0;
  for (int i = 1; i <= 10000; ++i) {
    double minT = INF;
    for (int j = 1; j <= n; ++j) {
      for (int k = 1; k <= n; ++k) {
        if (j == k || abs(x[j] - x[k]) <= eps) continue;
        minT = min(minT, getT(v[j], x[j], v[k], x[k]));
      }
    }
    minT = min(minT, t - Prev);
    for (int j = 1; j <= n; ++j) {
      f[j] = x[j];
      x[j] = x[j] + v[j] * minT;
    }
    for (int j = 1; j <= n; ++j) visited[j] = 0;
    for (int j = 1; j <= n; ++j) {
      if (visited[j]) continue;
      for (int k = j + 1; k <= n; ++k) {
        if (visited[k] || abs(f[j] - f[k]) <= eps) continue;
        double tmp = getT(v[j], f[j], v[k], f[k]);
        if (abs(tmp - minT) <= eps) {
          newV(v[j], m[j], v[k], m[k]);
          visited[j] = visited[k] = 1;
        }
      }
    }
    Prev += minT;
  }
  for (int i = 1; i <= n; ++i) {
    cout << fixed << setprecision(9) << " " << x[i] << '\n';
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  solve();
  return 0;
}
