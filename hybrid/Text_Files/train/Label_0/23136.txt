#include <bits/stdc++.h>
using namespace std;
const long long M = 998244353, N = 300005;
long long n, a[N];
long long ksm(long long x, long long y) {
  long long ans = 1;
  for (; y; y /= 2, x = x * x % M)
    if (y & 1) (ans *= x) %= M;
  return ans;
}
signed main() {
  scanf("%lld", &n);
  for (long long i = 1; i <= n; i++) scanf("%lld", &a[i]);
  sort(a + 1, a + n + 1);
  for (long long i = 1; i <= n; i++) a[i] = (a[i] + a[i - 1]) % M;
  for (long long i = 1; i <= n; i++) {
    long long l = n - 2 * i + 1, r = n - i, d = 1, s = 0;
    for (; r > 0; l -= i, r -= i, d++)
      l = max(l, 1ll), (s += d * (a[r] - a[l - 1] + M)) %= M;
    printf("%lld ", s * ksm(n, M - 2) % M);
  }
}
