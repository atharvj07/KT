#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int aa, bb;
  int sm = 0;
  cin >> aa >> bb;
  int a = min(aa, bb), b = max(aa, bb);
  int ca = 1;
  int cb = 1;
  while (a < b) {
    int ax = 1e9;
    int bx = 1e9;
    if (a + 1 == b)
      ax = ca;
    else if (b - 1 == a)
      bx = cb;
    if (a + 1 == b || b - 1 == a) {
      if (ax < bx) {
        sm += ca;
        ++ca;
        ++a;
      } else {
        sm += cb;
        ++cb;
        --b;
      }
    } else {
      sm += ca;
      ++ca;
      ++a;
      sm += cb;
      ++cb;
      --b;
    }
  }
  cout << sm << '\n';
  return 0;
}
