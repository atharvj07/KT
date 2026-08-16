#include <bits/stdc++.h>
using namespace std;
const long long mod = 1e9 + 7;
const double eps = 1e-5;
const int maxn = 2e6 + 5;
const int inf = 0x3f3f3f3f;
const long long linf = 0x3f3f3f3f3f3f3f3f;
const double PI = acos(-1);
const int Times = 11;
long long qpow_mod(long long a, long long b, long long c) {
  long long ans = 1;
  while (b) {
    if (b & 1) {
      ans *= a;
      ans %= c;
    }
    a *= a;
    a %= c;
    b >>= 1;
  }
  return ans;
}
inline int read() {
  int ret = 0, sgn = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') sgn = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    ret = ret * 10 + ch - '0';
    ch = getchar();
  }
  return ret * sgn;
}
long long extended_gcd(long long a, long long b, long long &x, long long &y) {
  long long r, t;
  if (!b) {
    x = 1;
    y = 0;
    return a;
  }
  r = extended_gcd(b, a % b, x, y);
  t = x;
  x = y;
  y = t - a / b * y;
  return r;
}
long long num_pow(long long a, long long k) {
  long long res = 1, tem = a;
  for (; k; k >>= 1) {
    if (k & 1) res = (res * tem) % mod;
    tem = (tem * tem) % mod;
  }
  return res;
}
long long fac[maxn];
long long comb(long long n, long long m) {
  return (fac[n] * num_pow(fac[m], mod - 2)) % mod *
         num_pow(fac[n - m], mod - 2) % mod;
}
int main() {
  int t;
  scanf("%d", &t);
  fac[0] = 1;
  for (int i = 1; i < 2e6; i++) {
    fac[i] = (fac[i - 1] * i) % mod;
  }
  while (t--) {
    long long n, y;
    scanf("%lld%lld", &n, &y);
    long long ans = num_pow(2, y - 1);
    for (long long i = 2; i * i <= n; i++) {
      int cnt = 0;
      if (n % i == 0) {
        while (n % i == 0) {
          cnt++;
          n /= i;
        }
        ans = ans * comb(cnt + y - 1, y - 1) % mod;
      }
    }
    if (n > 1) ans = (ans * y) % mod;
    printf("%lld\n", ans);
  }
  return 0;
}
