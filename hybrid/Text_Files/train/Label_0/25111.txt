#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 10;
long long n, a, b;
int k, sig[maxn];
const long long mod = 1e9 + 9;
char s[maxn];
long long qpow(long long x, long long a) {
  long long ret = 1;
  while (a) {
    if (a & 1) ret = ret * x % mod;
    x = x * x % mod;
    a >>= 1;
  }
  return ret;
}
long long inv(long long x) { return qpow(x, mod - 2); }
long long Sub(long long x, long long y) {
  long long t = (x - y) % mod;
  if (t < 0) t += mod;
  return t;
}
long long Add(long long x, long long y) {
  long long t = (x + y) % mod;
  if (t < 0) t += mod;
  return t;
}
long long getSum(long long a1, long long q, long long n) {
  if (q == 1LL) return a1 * n % mod;
  return a1 * Sub(1LL, qpow(q, n)) % mod * inv(Sub(1, q)) % mod;
}
int main() {
  scanf("%lld%lld%lld%d", &n, &a, &b, &k);
  scanf("%s", s);
  for (long long i = 0; i < k; i++) {
    if (s[i] == '+')
      sig[i] = 1;
    else
      sig[i] = -1;
  }
  long long res = 0, ans = 0, invA = inv(qpow(a, k)), B = qpow(b, k);
  for (int i = 0; i < k; i++)
    res = Add(res, (long long)sig[i] * qpow(a, n - i) % mod * qpow(b, i));
  printf("%lld\n", getSum(res, B * invA % mod, ((long long)n + 1) / k));
}
