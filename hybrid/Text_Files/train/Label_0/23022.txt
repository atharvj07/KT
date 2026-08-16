#include <bits/stdc++.h>
using namespace std;
const int mod = 998244353;
int pw[1000005], fac[1000005], inv[1000005];
int ksm(int a, int p) {
  int ans = 1;
  while (p) {
    if (p & 1) ans = 1ll * ans * a % mod;
    a = 1ll * a * a % mod;
    p >>= 1;
  }
  return ans;
}
int C(int n, int m) {
  if (n < m) return 0;
  return 1ll * fac[n] * inv[m] % mod * inv[n - m] % mod;
}
int mo(int x) {
  if (x < 0) x += mod;
  if (x >= mod) x -= mod;
  return x;
}
int main() {
  fac[0] = 1;
  for (int i = 1; i <= 1000000; i++) fac[i] = 1ll * fac[i - 1] * i % mod;
  inv[1000000] = ksm(fac[1000000], mod - 2);
  for (int i = 999999; i >= 0; i--) inv[i] = 1ll * inv[i + 1] * (i + 1) % mod;
  pw[0] = 1;
  for (int i = 1; i <= 1000000; i++) pw[i] = 1ll * pw[i - 1] * 3 % mod;
  int n, ans = 0;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    int tmp = ksm(1 - ksm(pw[n - i], mod - 2), n);
    tmp = mo(tmp - 1);
    tmp = 1ll * tmp * C(n, i) % mod;
    tmp = 1ll * tmp * ksm(ksm(pw[n], i), mod - 2) % mod;
    if (i & 1) tmp = -tmp;
    ans = mo(ans + tmp);
  }
  ans = mo(-ans);
  ans = 1ll * ans * 3 % mod * ksm(pw[n], n) % mod;
  int anss = 0;
  for (int i = 1; i <= n; i++) {
    int tmp = 1ll * pw[i] * ksm(pw[n], n - i) % mod;
    tmp = 1ll * tmp * C(n, i) % mod;
    if (i % 2 == 0) tmp = mo(-tmp);
    anss = mo(anss + tmp);
  }
  anss = mo(anss + anss);
  ans = mo(ans + anss);
  cout << ans;
}
