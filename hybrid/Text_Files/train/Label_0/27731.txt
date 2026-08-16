#include <bits/stdc++.h>
using namespace std;
const long long mod = 1e9 + 7;
long long qpow(long long a, long long b) {
  long long ans = 1;
  while (b) {
    if (b & 1) ans = ans * a % mod;
    a = a * a % mod;
    b >>= 1;
  }
  return ans;
}
int main() {
  long long n, m;
  scanf("%lld%lld", &n, &m);
  long long ans = qpow(2, m) * qpow(n + 1, m - 1) % mod * (n - m + 1) % mod;
  printf("%lld", ans % mod);
  return 0;
}
