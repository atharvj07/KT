#include <bits/stdc++.h>
using namespace std;
int main() {
  long long a, b, count = 0;
  cin >> a >> b;
  if (a == b) {
    cout << 0;
    return 0;
  }
  bool flag = true;
  long long a1 = 0, b1 = 0, c1 = 0, a2 = 0, b2 = 0, c2 = 0, x = 1, y = 1;
  while (flag) {
    if (a % 2 == 0) {
      a1++;
      a /= 2;
    } else if (a % 3 == 0) {
      b1++;
      a /= 3;
    } else if (a % 5 == 0) {
      c1++;
      a /= 5;
    } else {
      x = a;
      flag = false;
    }
  }
  bool f = true;
  while (f) {
    if (b % 2 == 0) {
      a2++;
      b /= 2;
    } else if (b % 3 == 0) {
      b2++;
      b /= 3;
    } else if (b % 5 == 0) {
      c2++;
      b /= 5;
    } else {
      y = b;
      f = false;
    }
  }
  if (x != y) {
    cout << -1;
  } else {
    cout << abs(a1 - a2) + abs(b1 - b2) + abs(c1 - c2);
  }
  return 0;
}
