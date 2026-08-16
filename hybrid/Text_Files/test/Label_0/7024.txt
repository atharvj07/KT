#include <bits/stdc++.h>
using namespace std;
int cmp(unsigned long long z1, unsigned long long k1, unsigned long long z2,
        unsigned long long k2) {
  unsigned long long r1 = z1 * k2;
  unsigned long long r2 = z2 * k1;
  if (r1 < r2) return -1;
  if (r1 > r2) return 1;
  return 0;
}
int cmp(unsigned long long t1, unsigned long long t2, unsigned long long a1,
        unsigned long long b1, unsigned long long a2, unsigned long long b2) {
  return cmp((a1 * t1 + b1 * t2), (a1 + b1), (a2 * t1 + b2 * t2), (a2 + b2));
}
unsigned long long r1, r2;
unsigned long long t1, t2;
unsigned long long x1, x2;
unsigned long long t0;
void chk(unsigned long long I1, unsigned long long I2) {
  if (I1 > x1 || I2 > x2) return;
  if (I1 + I2 == 0) return;
  if (cmp(I1 * t1 + I2 * t2, I1 + I2, t0, 1) == -1) return;
  if (r1 == 0 && r2 == 0) {
    r1 = I1;
    r2 = I2;
    return;
  }
  int ans = cmp(t1, t2, I1, I2, r1, r2);
  if (ans == 0) {
    if (r1 + r2 < I1 + I2) r1 = I1, r2 = I2;
  }
  if (ans == -1) {
    r1 = I1;
    r2 = I2;
  }
}
int main() {
  cin >> t1 >> t2 >> x1 >> x2 >> t0;
  if (t2 == t0 || t1 == t0) {
    int r1 = x1 * (t1 == t0);
    int r2 = x2 * (t2 == t0);
    cout << r1 << ' ' << r2 << endl;
    return 0;
  }
  for (int i1 = (0); i1 < int(x1 + 1); i1 += 1) {
    for (int i = (0); i < int(10); i += 1)
      chk(i1, (t0 * i1 - i1 * t1) / (t2 - t0) + i);
  }
  cout << r1 << ' ' << r2 << endl;
  return 0;
}
