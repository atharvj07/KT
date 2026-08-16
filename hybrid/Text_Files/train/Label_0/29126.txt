#include <bits/stdc++.h>
using namespace std;
int main() {
  double l, q, p, t1;
  cin >> l >> p >> q;
  t1 = l / (q + p);
  cout << 3 * l / (q + p) * p - 2 * t1 * p << "\n";
  return 0;
}
