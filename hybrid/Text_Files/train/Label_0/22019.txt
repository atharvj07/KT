#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 10, mod = 1e9 + 7;
int n, k, f[N], sum[N], fac[N], ifac[N];
int power(int a, int b) {
  int ret = 1;
  while (b) {
    if (b & 1) ret = 1ll * ret * a % mod;
    a = 1ll * a * a % mod;
    b >>= 1;
  }
  return ret;
}
int main() {
  scanf("%d%d", &n, &k);
  fac[0] = 1;
  for (int i = 1; i <= n; i++) fac[i] = 1ll * fac[i - 1] * i % mod;
  ifac[0] = 1;
  ifac[n] = power(fac[n], mod - 2);
  for (int i = n - 1; i >= 1; i--) ifac[i] = 1ll * ifac[i + 1] * (i + 1) % mod;
  f[0] = sum[0] = 1;
  for (int i = 1; i <= n; i++) {
    if (i >= k + 1)
      f[i] =
          1ll * ((sum[i - 1] + mod - sum[i - k - 1]) % mod) * fac[i - 1] % mod;
    else
      f[i] = 1ll * sum[i - 1] * fac[i - 1] % mod;
    sum[i] = (sum[i - 1] + 1ll * f[i] * ifac[i] % mod) % mod;
  }
  printf("%d\n", (fac[n] + mod - 1ll * fac[n - 1] * sum[n - 1] % mod) % mod);
  return 0;
}
