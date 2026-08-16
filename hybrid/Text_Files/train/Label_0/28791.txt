#include <bits/stdc++.h>
using namespace std;
const int maxn = 200000 + 10;
long long n, T, a[maxn], x, y, t1, t2, k;
long long b[maxn];
long long cmp(long long x, long long y) { return x > y; }
long long cmp1(long long x, long long y) { return x > y; }
long long check(long long len) {
  for (long long i = 1; i <= len; i++) {
    if (i % t1 == 0 && i % t2 == 0)
      b[i] = x + y;
    else if (i % t1 == 0)
      b[i] = x;
    else if (i % t2 == 0)
      b[i] = y;
  }
  sort(b + 1, b + 1 + len, cmp1);
  long long ans = 0;
  for (long long i = 1; i <= len; i++) {
    ans += b[i] * a[i];
  }
  if (ans >= k) return 1;
  return 0;
}
int main() {
  cin >> T;
  while (T--) {
    cin >> n;
    for (long long i = 1; i <= n; i++) cin >> a[i];
    sort(a + 1, a + 1 + n, cmp);
    cin >> x >> t1 >> y >> t2 >> k;
    k *= 100;
    long long l = 0, r = n, ans = 0x7f7f7f7f;
    while (l <= r) {
      long long mid = (l + r) / 2;
      memset(b, 0, sizeof(b));
      if (check(mid)) {
        r = mid - 1;
        ans = mid;
      } else {
        l = mid + 1;
      }
    }
    if (ans == 0x7f7f7f7f)
      cout << "-1" << endl;
    else
      cout << ans << endl;
  }
}
