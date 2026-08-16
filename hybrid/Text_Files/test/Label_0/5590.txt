#include <bits/stdc++.h>
using namespace std;
long long n, m, ans = 0;
long long a, b, x, y, z;
int main() {
  cin >> a >> b;
  cin >> x >> y >> z;
  n = x * 2 + y;
  m = y + z * 3;
  if (n - a > 0) ans += n - a;
  if (m - b > 0) ans += m - b;
  cout << ans;
}
