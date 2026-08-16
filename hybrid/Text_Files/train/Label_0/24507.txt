#include <bits/stdc++.h>
#pragma GCC optimize("O3")
using namespace std;
long long int mod = 998244353LL;
long long int factmod[1000100];
unsigned long long powmod(long long z, long long a) {
  if (a == 0) return 1;
  if (a == 1) return z;
  long long x = powmod(z, a / 2);
  x = (x * x) % mod;
  if (a % 2 == 1) x = (x * z) % mod;
  return x;
}
unsigned long long invmod(long long z) { return powmod(z, mod - 2); }
int main() {
  long long int n;
  scanf("%lld", &n);
  factmod[0] = 1;
  factmod[1] = 1;
  for (int x = 2; x <= n + 10; x += 1) {
    factmod[x] = factmod[x - 1] * x % mod;
  }
  long long int b = 0;
  for (long long k = 1; k < n; k++) {
    long long int a = (k * k) % mod;
    a *= (factmod[n] * invmod(factmod[k + 1]) % mod);
    a %= mod;
    a *= invmod(factmod[n - k - 1]);
    a %= mod;
    a *= factmod[n - k - 1];
    b += a;
    b %= mod;
  }
  long long int c = factmod[n] * n - n + 1;
  long long int ans = c - b + mod;
  ans %= mod;
  printf("%lld\n", ans);
  return 0;
}
