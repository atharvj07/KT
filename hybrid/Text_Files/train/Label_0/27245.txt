#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 15;
long long a[N], b[N], cnta = 0, cntb = 0, c[N], ppow[N], zz[N];
int main() {
  long long x, y, xx, yy;
  ppow[0] = 1;
  for (int i = 1; i <= 60; i++) ppow[i] = ppow[i - 1] * 2;
  cin >> x >> y;
  xx = x;
  yy = y;
  if (x > y) {
    cout << "-1" << endl;
    return 0;
  }
  if (x == y) {
    if (x == 0) {
      cout << "0" << endl;
      return 0;
    }
    cout << "1" << endl;
    cout << x << endl;
    return 0;
  }
  if (x % 2 == 0 && y % 2 == 1 || x % 2 == 1 && y % 2 == 0) {
    cout << "-1" << endl;
    return 0;
  }
  while (x) {
    a[cnta++] = x % 2;
    x /= 2;
  }
  while (y) {
    b[cntb++] = y % 2;
    y /= 2;
  }
  x = xx;
  y = yy;
  long long z = y - x;
  z /= 2;
  if (z & x) {
    cout << "3" << endl;
    y -= x;
    cout << x << " " << y / 2 << " " << y / 2 << endl;
    return 0;
  } else {
    cout << "2" << endl;
    cout << x + z << " " << z << endl;
    return 0;
  }
  x = xx;
  y = yy;
  for (int i = cntb; i >= 0; i--) {
    if (b[i] == 1) {
      if (a[i] == 1)
        c[i] += 1;
      else {
        if (a[i - 1] == 1 && b[i - 1] == 0) {
          c[i - 1] = 1;
          a[i - 1] = 0;
          b[i - 1] = 1;
        } else if (a[i - 1] == 1 && b[i - 1] == 1)
          c[i - 1] = 2;
        else if (a[i - 1] == 0 && b[i - 1] == 1) {
          c[i - 1] = 2;
        } else
          c[i - 1] = 2;
      }
    }
  }
  long long maxx = 0;
  for (int i = cntb; i >= 0; i--) {
    maxx = max(maxx, c[i]);
  }
  if (maxx == 3) {
    cout << "3" << endl;
    y -= x;
    cout << x << " " << y / 2 << " " << y / 2 << endl;
    return 0;
  }
  cout << maxx << endl;
  while (1) {
    long long s = 0;
    for (int i = cntb; i >= 0; i--) {
      if (c[i]) {
        s += 1 * ppow[i];
        c[i]--;
      }
    }
    if (s)
      cout << s << " ";
    else {
      cout << endl;
      return 0;
    }
  }
  return 0;
}
