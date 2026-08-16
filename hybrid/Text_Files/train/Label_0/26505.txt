#include <bits/stdc++.h>
using namespace std;
double PI = acos(-1.0);
template <class T>
inline void checkmin(T &a, T b) {
  if (b < a) a = b;
}
template <class T>
inline void checkmax(T &a, T b) {
  if (b > a) a = b;
}
template <class T>
inline T gcd(T a, T b) {
  if (!b) return a;
  return gcd(b, a % b);
}
int main() {
  int a, b, m, vx, vy, vz;
  double tz0;
  while (~scanf("%d%d%d%d%d%d", &a, &b, &m, &vx, &vy, &vz)) {
    double x, z, t;
    t = -(double)m / vy;
    if (vz == 0)
      z = 0.0;
    else {
      double tz = 2.0 * b / vz;
      tz0 = t;
      while (tz0 >= tz) tz0 -= tz;
      if (tz0 < (double)b / vz)
        z = tz0 * vz;
      else {
        tz0 -= (double)b / vz;
        z = (double)b - tz0 * vz;
      }
    }
    if (vx == 0) {
      x = a / 2.0;
    } else {
      double tx = 2.0 * a / fabs(vx + 0.0);
      if (t <= a / 2.0 / fabs(vx + 0.0)) {
        x = a / 2.0 + t * vx;
      } else {
        double tx0 = t - a / 2.0 / fabs(vx + 0.0);
        while (tx0 >= tx) tx0 -= tx;
        if (tx0 < (double)a / fabs(vx + 0.0))
          if (vx > 0)
            x = a - tx0 * vx;
          else
            x = -vx * tx0;
        else {
          tx0 -= (double)a / fabs(vx + 0.0);
          if (vx > 0)
            x = vx * tx0;
          else
            x = a + vx * tx0;
        }
      }
    }
    printf("%f %f\n", x, z);
  }
}
