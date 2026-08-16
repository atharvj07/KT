#include <bits/stdc++.h>
using namespace std;
const long long N = 3e6 + 5;
long long n, x, y;
char a[N];
int32_t main() {
  scanf("%I64d%I64d%I64d%s", &n, &x, &y, a + 1);
  long long p = 1, cnt = 0;
  while (1) {
    while (a[p] == '1' && p <= n) p++;
    if (p > n) break;
    while (a[p] == '0' && p <= n) p++;
    ++cnt;
    if (p > n) break;
  }
  if (cnt == 0) {
    cout << 0 << endl;
  } else if (cnt == 1) {
    cout << y << endl;
  } else {
    long long mn = 2e18;
    mn = min((cnt - 1) * y + x, cnt * y);
    mn = min(mn, (cnt - 1) * x + y);
    cout << mn << endl;
  }
  return 0;
}
