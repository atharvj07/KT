#include <bits/stdc++.h>
static const long double eps = 1e-18;
using namespace std;
long double cross(long double x1, long double y1, long double x2,
                  long double y2) {
  return x1 * y2 - x2 * y1;
}
bool canCross(long double x1, long double y1, long double x2, long double y2,
              long double qx, long double qy) {
  long double c1 = cross(x1, y1, qx, qy);
  long double c2 = cross(x2, y2, qx, qy);
  return abs(c1) < eps || abs(c2) < eps || ((c1 < 0) ^ (c2 < 0));
}
int main() {
  int a, b;
  scanf("%d%d", &a, &b);
  int c, d;
  scanf("%d%d", &c, &d);
  if (a > c) {
    swap(a, c);
    swap(b, d);
  }
  long double l = 0, r = max(abs(a - c), abs(b - d)) / 2.0;
  for (int it = 0; it < 1e5; it++) {
    bool can = false;
    long double m = (l + r) / 2;
    for (int i = 0; i < 2; i++) {
      swap(a, c);
      swap(b, d);
      long double x1 = a + m;
      long double y1 = b - m;
      long double x2 = a - m;
      long double y2 = b + m;
      can |= canCross(x1, y1, x2, y2, c + m, d - m) ||
             canCross(x1, y1, x2, y2, c - m, d - m) ||
             canCross(x1, y1, x2, y2, c - m, d + m) ||
             canCross(x1, y1, x2, y2, c + m, d + m) ||
             canCross(x1, y1, x2, y2, c, d);
      x1 = a + m;
      y1 = b + m;
      x2 = a - m;
      y2 = b - m;
      can |= canCross(x1, y1, x2, y2, c + m, d - m) ||
             canCross(x1, y1, x2, y2, c - m, d - m) ||
             canCross(x1, y1, x2, y2, c - m, d + m) ||
             canCross(x1, y1, x2, y2, c + m, d + m) ||
             canCross(x1, y1, x2, y2, c, d);
    }
    if (can) {
      r = m;
    } else {
      l = m;
    }
  }
  printf("%.11f", (double)l);
  return 0;
}
