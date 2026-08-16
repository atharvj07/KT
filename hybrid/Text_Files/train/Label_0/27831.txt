#include <bits/stdc++.h>
using namespace std;
int main() {
  long q, x, y;
  cin >> q;
  for (long i = 0; i < q; i++) {
    cin >> x >> y;
    if (x == y) {
      if (x % 2 == 1)
        cout << -x;
      else
        cout << x;
      cout << endl;
    } else {
      long a = x + 1 - x % 2;
      long b = y + 1 - y % 2;
      if (b > y) b = y;
      long s1;
      if (a == b)
        s1 = -a;
      else
        s1 = -(a + (b - a) / 2) * ((b - a) / 2 + 1);
      a = x + x % 2;
      b = y - y % 2;
      long s2;
      if (a == b)
        s2 = a;
      else
        s2 = (a + (b - a) / 2) * ((b - a) / 2 + 1);
      cout << s1 + s2 << endl;
    }
  }
  return 0;
}
