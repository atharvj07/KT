#include <bits/stdc++.h>
using namespace std;
int main() {
  long double x1, y1, r1, x2, y2, r2;
  cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
  long double x = abs(x1 - x2);
  long double y = abs(y1 - y2);
  long double d = sqrt(x * x + y * y) - (r1 + r2);
  if (d > 0)
    cout << setprecision(15) << (d / 2);
  else {
    d += (r1 + r2);
    if (d < max(r1, r2) - min(r1, r2)) {
      cout << setprecision(15) << (max(r1, r2) - d - min(r1, r2)) / 2;
    } else
      cout << 0 << endl;
  }
}
