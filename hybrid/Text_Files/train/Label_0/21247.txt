#include <bits/stdc++.h>
using namespace std;
int main() {
  int vp, vd, t, f, c;
  scanf("%d %d %d %d %d", &vp, &vd, &t, &f, &c);
  int kol = 0;
  if (vp < vd) {
    double t0 = c;
    t0 /= vp;
    double T = vp * t;
    T /= vd - vp;
    double x = t;
    while (x + T < t0) {
      kol++;
      x = x + 2 * T + f;
      T = vp * x;
      T /= vd - vp;
    }
  }
  printf("%d", kol);
  return 0;
}
