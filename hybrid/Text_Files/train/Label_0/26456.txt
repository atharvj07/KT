#include <bits/stdc++.h>
using namespace std;
int d;
bool one(int x, int y) { return (x - y == d || y - x == d || x + y == d - 1); }
int func1(int low, int high, int x) {
  high = min(high, x + d);
  low = max(low, x - d);
  low = max(low, d - 1 - x);
  if (low > high) return 0;
  int ans = (high - low + 1) * 2;
  if (one(x, low)) ans--;
  if (high != low && one(x, high)) ans--;
  return ans;
}
int func2(int low, int x) {
  if (func1(low, 100000000, x) > 0) return 1;
  return 0;
}
int main(void) {
  int N, x, M, y, i;
  cin >> N >> x >> M >> y;
  d = x - y;
  if (d < 0) d = -d;
  long long ans = 1;
  for ((i) = 0; (i) < (int)(N); (i)++) ans += func1(0, M - 1, i);
  for ((i) = 0; (i) < (int)(M); (i)++) ans += func2(N, i);
  for ((i) = 0; (i) < (int)(N); (i)++) ans += func2(M, i);
  cout << ans << endl;
  return 0;
}
