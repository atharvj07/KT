#include <bits/stdc++.h>
using namespace std;
int n, m, s;
long long count(int a, int b, int c, int d) {
  long long dx = max(a, c), dy = max(b, d);
  long long ret = max(0LL, (n + 1 - (dx * 2 + 1)) * (m + 1 - (dy * 2 + 1)));
  return ret;
}
int main() {
  cin >> n >> m >> s;
  long long num = 0;
  for (int a = 0; a * 2 < n; a++)
    for (int b = 0; b * 2 < m; b++)
      for (int c = 0; c * 2 < n; c++) {
        bool countedd1 = false;
        int d1 = (s - (a * 2 + 1) * (b * 2 + 1));
        if (d1 >= 0 && a < c && d1 % ((c - a) * 2) == 0) {
          d1 = d1 / ((c - a) * 2) - 1;
          if (d1 >= 0 && d1 % 2 == 0) {
            d1 /= 2;
            if (d1 <= b) {
              num += count(a, b, c, d1);
              countedd1 = true;
            }
          }
        } else if (d1 == 0 && a >= c) {
          for (int i = 0; i <= b; i++) num += count(a, b, c, i);
        }
        if (a > c) {
          int d2 = s - (a * 2 + 1) * (b * 2 + 1) + (c * 2 + 1) * (b * 2 + 1);
          if (d2 >= 0 && d2 % (c * 2 + 1) == 0) {
            d2 = d2 / (c * 2 + 1) - 1;
            if (d2 >= 0 && d2 % 2 == 0) {
              d2 /= 2;
              if (d2 > b && d2 * 2 < m) {
                num += count(a, b, c, d2);
              }
              if (d2 == b) {
                if (!(s == (a * 2 + 1) * (b * 2 + 1))) {
                  if (!(d2 == d1 && countedd1)) {
                    num += count(a, b, c, d2);
                  }
                }
              }
            }
          }
        } else {
          if (s % (c * 2 + 1) == 0) {
            int d3 = s / (c * 2 + 1) - 1;
            if (d3 >= 0 && d3 % 2 == 0) {
              d3 /= 2;
              if (d3 >= b && d3 * 2 < m) {
                if (!(s == (a * 2 + 1) * (b * 2 + 1))) {
                  if (!(d3 == d1 && countedd1)) {
                    num += count(a, b, c, d3);
                  }
                }
              }
            }
          }
        }
      }
  cout << num << endl;
  return 0;
}
