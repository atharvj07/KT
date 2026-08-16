#include <bits/stdc++.h>
using namespace std;
const int N = 200005;
const int mod = 1e9 + 7;
long long h[N + 5], g[N + 5];
long long modpow(long long a, long long pn) {
  long long res = 1;
  while (pn) {
    if (pn & 1) res = res * a % mod;
    a = a * a % mod;
    pn >>= 1;
  }
  return res;
}
long long C(long long a, long long b) {
  if (a < b)
    return 0;
  else
    return h[a] * g[a - b] % mod * g[b] % mod;
}
void init() {
  int i;
  h[0] = h[1] = 1;
  for (i = 2; i < N; i++) h[i] = h[i - 1] * i % mod;
  g[N - 1] = modpow(h[N - 1], mod - 2);
  for (i = N - 2; i >= 0; i--) g[i] = g[i + 1] * (i + 1) % mod;
}
long long a[N];
int main() {
  init();
  int n, i, j;
  scanf("%d", &n);
  for (i = 1; i <= n; i++) scanf("%d", a + i);
  if (n == 1) {
    printf("%d\n", a[n]);
    return 0;
  }
  if (n & 1) {
    int fl = 0;
    for (i = 1; i < n; i++) {
      if (!fl)
        a[i] = a[i] + a[i + 1];
      else
        a[i] = a[i] - a[i + 1];
      a[i] = (a[i] + 2 * mod) % mod;
      fl ^= 1;
    }
    --n;
  }
  long long ans = 0;
  for (i = 1; i <= n; i += 2) {
    ans = (ans + C(n / 2 - 1, i / 2) * a[i] % mod) % mod;
  }
  long long res = 0;
  for (i = 2; i <= n; i += 2) {
    res = (res + C(n / 2 - 1, (i - 1) / 2) * a[i] % mod) % mod;
  }
  if (n / 2 & 1)
    ans = ans + res;
  else
    ans = (ans - res + mod) % mod;
  printf("%lld\n", ans % mod);
}
