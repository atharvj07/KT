#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, a, b, c, d, k, t, l;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a >> b >> c >> d >> k;
    if (a % c == 0)
      t = a / c;
    else
      t = (a / c) + 1;
    if (b % d == 0)
      l = b / d;
    else
      l = (b / d) + 1;
    if (l + t <= k)
      cout << t << " " << l << endl;
    else
      cout << -1 << endl;
  }
}
