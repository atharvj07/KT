#include <bits/stdc++.h>
using namespace std;
const int iinf = 1e9 + 7;
const long long linf = 1ll << 60;
const double dinf = 1e10;
void scf(int &x) {
  bool f = 0;
  x = 0;
  char c = getchar();
  while ((c < '0' || c > '9') && c != '-') c = getchar();
  if (c == '-') {
    f = 1;
    c = getchar();
  }
  while (c >= '0' && c <= '9') {
    x = x * 10 + c - '0';
    c = getchar();
  }
  if (f) x = -x;
  return;
}
void scf(int &x, int &y) {
  scf(x);
  return scf(y);
}
void scf(int &x, int &y, int &z) {
  scf(x);
  scf(y);
  return scf(z);
}
int r1, r2, d, l1, l2;
long long ans;
inline int ABS(int i) { return i >= 0 ? i : -i; }
inline int MIN(int a, int b) { return a < b ? a : b; }
inline int MAX(int a, int b) { return a > b ? a : b; }
inline int calcv(int r, int rmin, int rmax) {
  int ret = 0, r1 = r + d, r2 = r - d;
  if (r + rmin <= d && r + rmax >= d) ret++;
  if (rmin <= r1 && r1 <= rmax) ret++;
  if (rmin <= r2 && r2 <= rmax) ret++;
  r1 = MAX(d - r, r - d) + 1;
  r2 = d + r - 1;
  (r1 > rmin) && (rmin = r1);
  (r2 < rmax) && (rmax = r2);
  if (rmax >= rmin) ret += (rmax - rmin + 1 << 1);
  return ret;
}
int main() {
  int x, y;
  scf(r1, x);
  scf(r2, y);
  d = ABS(x - y);
  if (r1 + r2 <= d) {
    printf("%d\n", r1 + r2 + 1);
    return 0;
  }
  l1 = MAX(1, d - r2);
  l2 = MAX(1, d - r1);
  ans = l1 + l2;
  int R1, R2;
  R1 = r1;
  R2 = r2;
  r1 = d + R2;
  r2 = d + R1;
  if (r1 > R1)
    r1 = R1;
  else
    ans += R1 - r1;
  if (r2 > R2)
    r2 = R2;
  else
    ans += R2 - r2;
  for (int i = l1; i <= r1; i++) ans += (long long)calcv(i, l2, r2);
  printf("%I64d\n", ans);
  return 0;
}
