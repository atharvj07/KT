#include <bits/stdc++.h>
using namespace std;
long long n, m, k;
long long a[100005];
long long ans = 0;
signed main() {
  scanf("%lld %lld %lld", &n, &m, &k);
  for (register long long i = 0; i < m; i++) scanf("%lld", &a[i]);
  sort(a, a + m);
  register long long l = 0, r = k;
  for (register long long p = 0, s = 0; s < m;) {
    bool f = 1;
    register long long cnt = 0;
    while (a[s] >= l && a[s] <= r && s < m) s++, f = 0, cnt++;
    if (!f) ans++;
    r += cnt;
    if (a[s] > r) {
      l = r + 1;
      r = ((l + k - 1) > (n) ? (n) : (l + k - 1));
      register long long x = (a[s] - l) / k;
      l += x * k;
      r += x * k;
    }
  }
  printf("%lld", ans);
  return 0;
}
