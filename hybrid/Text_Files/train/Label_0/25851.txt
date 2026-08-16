#include <bits/stdc++.h>
using namespace std;
const int inf = 1e9;
const int MOD = 1e9 + 7;
const int N = 0, BAR = 1e6, LIM = 5e6;
int x, y, n;
int main() {
  scanf("%d", &n);
  int xa = inf, xb = -inf, ya = inf, yb = -inf;
  while (n--) {
    scanf("%d%d", &x, &y);
    x += BAR, y += BAR;
    xa = min(xa, x - y - 1), xb = max(xb, x + y + 1);
    ya = min(ya, x - (LIM - y + 1)), yb = max(yb, x + (LIM - y + 1));
  }
  int ans = 0;
  int rya = (LIM - (yb - ya) / 2);
  ans += (yb - ya) % 2;
  int ryb = (xb - xa) / 2;
  ans += (xb - xa) % 2;
  ans += 2 * (ryb - rya);
  cout << ans;
}
