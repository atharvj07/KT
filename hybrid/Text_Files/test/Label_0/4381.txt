#include <bits/stdc++.h>
using namespace std;
const double pi = acos(-1);
const double eps = 1e-10;
const int inf = 0x3f3f3f3f;
const long long infLL = 0x3f3f3f3f3f3f3f3fLL;
const int maxn = 2000 + 5;
const long long mod = 1000000007;
long long fac[maxn], ifac[maxn];
void gcd(long long a, long long b, long long &d, long long &x0, long long &y0) {
  if (!b) {
    d = a;
    x0 = 1;
    y0 = 0;
  } else {
    gcd(b, a % b, d, y0, x0);
    y0 -= x0 * (a / b);
  }
}
long long inv(long long a, long long m = mod) {
  long long d, x, y;
  gcd(a, m, d, x, y);
  return d == 1 ? (x + m) % m : -1;
}
void mk_fac() {
  fac[0] = 1;
  for (int i = 1; i < maxn; ++i) fac[i] = fac[i - 1] * i % mod;
  for (int i = 0; i < maxn; ++i) ifac[i] = inv(fac[i]);
}
long long A(int n, int m) {
  if (!fac[0]) mk_fac();
  return fac[n] * ifac[n - m] % mod;
}
long long C(int n, int m) {
  if (!fac[0]) mk_fac();
  return fac[n] * ifac[n - m] % mod * ifac[m] % mod;
}
long long s[maxn];
long long f[maxn][maxn];
void init() {
  s[0] = 0;
  for (int i = 1; i < maxn; ++i) s[i] = s[i - 1] + i;
  for (int i = 1; i < maxn; ++i) f[i][1] = 1;
  for (int j = 2; j < maxn; ++j) {
    if (s[j] >= maxn) break;
    f[s[j]][j] = fac[j];
    for (int i = s[j] + 1; i < maxn; ++i) {
      f[i][j] += f[i - j][j] + f[i - j][j - 1] * j % mod;
      f[i][j] %= mod;
    }
  }
}
int main() {
  ios::sync_with_stdio(false);
  mk_fac();
  init();
  int T;
  cin >> T;
  while (T--) {
    int n, k;
    cin >> n >> k;
    --n;
    long long res = 0;
    for (int i = s[k - 1]; i <= n; ++i) {
      int t = n - i - (k - 1);
      if (t < 0) break;
      res += f[i + k][k] * C(k + t, t) % mod;
      res %= mod;
    }
    cout << res << endl;
  }
  return 0;
}
