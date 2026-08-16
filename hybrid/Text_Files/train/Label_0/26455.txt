#include <bits/stdc++.h>
using namespace std;
int n, m, x, y;
bool ok(int a, int b, int c) {
  if (a != n && a + b < c) return false;
  if (a != n && c != m && a + c + 1 < b) return false;
  if (c != m && b + c < a) return false;
  return true;
}
int main() {
  scanf("%d%d%d%d", &n, &x, &m, &y);
  x = abs(x - y);
  int l = 0, r = n;
  int64_t ans = 0;
  for (int d = 0; d <= m; ++d) {
    while (l > 0 && ok(l - 1, x, d)) --l;
    while (l < n && !ok(l, x, d)) ++l;
    while (r > 0 && !ok(r, x, d)) --r;
    while (r < n && ok(r + 1, x, d)) ++r;
    ans += max(0, r - l + 1) +
           (d > 0 && d < m ? max(0, (r - 1) - (l + 1) + 1) : 0);
  }
  cout << ans << endl;
}
