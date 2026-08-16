#include <bits/stdc++.h>
using namespace std;
const int MAXM = 100005;
const long double eps = 1e-9;
int n, m, c = 0;
long double ax[MAXM], ay[MAXM], gx[MAXM], gy[MAXM], sx = 0, sy = 0;
bool check(long double a, long double b, long double c, long double d) {
  if (b * d > 0) return 0;
  return a + b * (c - a) / (b - d) > 0;
}
long double dist(pair<long double, long double> p) {
  return sqrt(p.first * p.first + p.second * p.second);
}
long double dot(pair<long double, long double> u,
                pair<long double, long double> v) {
  return u.first * v.first + u.second * v.second;
}
pair<long double, long double> cl(long double a, long double b, long double c,
                                  long double d) {
  pair<long double, long double> s(a, b), e(c, d), r;
  pair<long double, long double> v(c - a, d - b);
  double dv = dist(v);
  long double len = -dot(s, v) / dv;
  long double x = a + len / dv * (c - a);
  if (x > min(a, c) && x < max(a, c)) {
    long double y = b + len / dv * (d - b);
    return pair<long double, long double>(x, y);
  }
  if (dist(s) > dist(e))
    r = e;
  else
    r = s;
  return r;
}
int main() {
  ios::sync_with_stdio(false);
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> gx[i] >> gy[i];
    sx += gx[i], sy += gy[i];
  }
  sx /= n, sy /= n;
  sx += eps, sy += eps;
  cin >> m;
  for (int i = 0; i < m; i++) {
    cin >> ax[i] >> ay[i];
    ax[i] -= sx, ay[i] -= sy;
  }
  for (int i = 0; i < m; i++) {
    c += check(ax[i], ay[i], ax[(i + 1) % m], ay[(i + 1) % m]);
  }
  if (c % 2 == 0) {
    pair<long double, long double> p(10000000, 10000000);
    for (int i = 0; i < m; i++) {
      pair<long double, long double> q =
          cl(ax[i], ay[i], ax[(i + 1) % m], ay[(i + 1) % m]);
      if (dist(p) > dist(q)) p = q;
    }
    sx += p.first, sy += p.second;
  }
  long double res = 0;
  for (int i = 0; i < n; i++) {
    gx[i] -= sx, gy[i] -= sy;
    res += gx[i] * gx[i] + gy[i] * gy[i];
  }
  cout << fixed << setprecision(9) << res << endl;
}
