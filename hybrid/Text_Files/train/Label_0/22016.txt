#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e6 + 50, mod = 1e9 + 7;
int n, k, s, ans, inv[maxn], fac[maxn], f[maxn];
int read() {
  int x = 0;
  char c = getchar();
  while (c < '0' || c > '9') c = getchar();
  while (c >= '0' && c <= '9') x = x * 10 + (c ^ 48), c = getchar();
  return x;
}
int qpow(int x, int k) {
  long long d = 1, t = x;
  while (k) {
    if (k & 1) d = d * t % mod;
    t = t * t % mod, k >>= 1;
  }
  return d;
}
int main() {
  n = read(), k = read();
  fac[0] = 1;
  for (int i = 1; i <= n; i++) fac[i] = 1ll * fac[i - 1] * i % mod;
  inv[n] = qpow(fac[n], mod - 2);
  for (int i = n - 1; i >= 0; i--) inv[i] = 1ll * inv[i + 1] * (i + 1) % mod;
  f[0] = 1;
  for (int i = 1; i <= n; i++) {
    s = (s + 1ll * f[i - 1] * inv[i - 1]) % mod;
    if (i > k) s = (s - 1ll * f[i - k - 1] * inv[i - k - 1] % mod + mod) % mod;
    f[i] = 1ll * s * fac[i - 1] % mod;
  }
  ans = fac[n];
  for (int i = 0; i < n; i++)
    ans = (ans - 1ll * f[i] * inv[i] % mod * fac[n - 1] % mod + mod) % mod;
  printf("%d\n", ans);
  return 0;
}
