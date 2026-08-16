#include <bits/stdc++.h>
#pragma GCC optimize(3, "Ofast", "inline")
#pragma GCC target("avx,avx2")
using namespace std;
template <class t>
inline t read(t &x) {
  char c = getchar();
  bool f = 0;
  x = 0;
  while (!isdigit(c)) f |= c == '-', c = getchar();
  while (isdigit(c)) x = (x << 1) + (x << 3) + (c ^ 48), c = getchar();
  if (f) x = -x;
  return x;
}
template <class t, class... A>
inline void read(t &x, A &...a) {
  read(x);
  read(a...);
}
template <class t>
inline void write(t x) {
  if (x < 0)
    putchar('-'), write(-x);
  else {
    if (x > 9) write(x / 10);
    putchar('0' + x % 10);
  }
}
const int mod = 1e9 + 7, N = 2e5 + 5;
pair<int, int> a[N];
int fac[N << 1], inv[N << 1], n, m, nm, ans, s, f[N][23];
int fpow(int first, int second) {
  int res = 1;
  for (; second; second >>= 1, first = 1ll * first * first % mod)
    if (second & 1) res = 1ll * res * first % mod;
  return res;
}
int C(int n, int m) { return 1ll * fac[n] * inv[m] % mod * inv[n - m] % mod; }
int calc(int first, int second) {
  return C(
      a[second].first - a[first].first + a[second].second - a[first].second,
      a[second].first - a[first].first);
}
signed main() {
  read(n, m, nm, s);
  s <<= 1;
  fac[0] = 1;
  for (int i = 1; i <= n + m; i++) fac[i] = 1ll * fac[i - 1] * i % mod;
  inv[n + m] = fpow(fac[n + m], mod - 2);
  for (int i = n + m - 1; ~i; i--) inv[i] = 1ll * inv[i + 1] * (i + 1) % mod;
  for (int i = 1; i <= nm; i++) read(a[i].first, a[i].second);
  a[++nm] = pair<int, int>(1, 1);
  a[++nm] = pair<int, int>(n, m);
  sort(a + 1, a + 1 + nm);
  f[1][0] = 1;
  for (int i = 2; i <= nm; i++) {
    f[i][1] = calc(1, i);
    for (int j = 2; j < 22; j++)
      for (int k = 1; k < i; k++)
        if (a[i].second >= a[k].second)
          f[i][j] = (f[i][j] +
                     ((1ll * (f[k][j - 1] - f[k][j]) * calc(k, i) % mod + mod) %
                      mod)) %
                    mod;
  }
  for (int i = 1; i < 22; i++) {
    s = s + 1 >> 1;
    ans = (ans + (1ll * (f[nm][i] - f[nm][i + 1]) * s % mod + mod) % mod) % mod;
  }
  write(1ll * ans * fpow(calc(1, nm), mod - 2) % mod);
}
