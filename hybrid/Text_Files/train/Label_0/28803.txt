#include <bits/stdc++.h>
using namespace std;
long long calc(long long x1, long long y1, long long x2, long long y2) {
  if ((x2 - x1 + 1) * (y2 - y1 + 1) % 2 == 0) return 1;
  return 2;
}
int main() {
  long long t;
  cin >> t;
  while (t--) {
    long long n, m;
    cin >> n >> m;
    long long x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    long long x3, y3, x4, y4;
    cin >> x3 >> y3 >> x4 >> y4;
    long long a, b;
    long long sum_a, sum_b;
    if (calc(1, 1, m, n) == 1) {
      sum_a = sum_b = n * m / 2;
    } else {
      sum_a = n * m / 2 + 1;
      sum_b = n * m / 2;
    }
    if (calc(x1, y1, x2, y2) == 1)
      a = (x2 - x1 + 1) * (y2 - y1 + 1) / 2;
    else {
      if (x1 % 2 == y1 % 2)
        a = (x2 - x1 + 1) * (y2 - y1 + 1) / 2;
      else
        a = (x2 - x1 + 1) * (y2 - y1 + 1) / 2 + 1;
    }
    if (calc(x3, y3, x4, y4) == 1)
      b = (x4 - x3 + 1) * (y4 - y3 + 1) / 2;
    else {
      if (x3 % 2 == y3 % 2)
        b = (x4 - x3 + 1) * (y4 - y3 + 1) / 2 + 1;
      else
        b = (x4 - x3 + 1) * (y4 - y3 + 1) / 2;
    }
    sum_a += a;
    sum_a -= b;
    sum_b -= a;
    sum_b += b;
    long long tmpx = max(x1, x3);
    long long tmpy = max(y1, y3);
    long long tmpxx = min(x2, x4);
    long long tmpyy = min(y2, y4);
    if (tmpx > tmpxx || tmpy > tmpyy) {
    } else {
      long long c;
      if (calc(tmpx, tmpy, tmpxx, tmpyy) == 1)
        c = (tmpxx - tmpx + 1) * (tmpyy - tmpy + 1) / 2;
      else {
        if (tmpx % 2 == tmpy % 2)
          c = (tmpxx - tmpx + 1) * (tmpyy - tmpy + 1) / 2;
        else
          c = (tmpxx - tmpx + 1) * (tmpyy - tmpy + 1) / 2 + 1;
      }
      sum_b += c;
      sum_a -= c;
    }
    cout << sum_a << " " << sum_b << endl;
  }
}
