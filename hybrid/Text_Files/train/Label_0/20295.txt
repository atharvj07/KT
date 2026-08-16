#include <bits/stdc++.h>
using namespace std;
long long fact[200001];
long long invFact[200001];
long long mod = 1000 * 1000 * 1000 + 7;
long long binpow(long long x, long long n) {
  if (n == 0)
    return 1;
  else if (n & 1)
    return (binpow(x, n - 1) * x) % mod;
  else
    return binpow((x * x) % mod, n >> 1);
}
long long inv(long long x) { return binpow(x, mod - 2); }
long long calcC(int n, int k) {
  long long ans = (fact[n] * invFact[k]) % mod;
  return (ans * invFact[n - k]) % mod;
}
int main() {
  ios_base::sync_with_stdio(0);
  fact[0] = 1;
  for (int i = 1; i <= 200000; i++) {
    fact[i] = (fact[i - 1] * i) % mod;
  }
  invFact[0] = 1;
  for (int i = 1; i <= 200000; i++) {
    invFact[i] = (invFact[i - 1] * inv(i)) % mod;
  }
  int n;
  cin >> n;
  long long ans = 0;
  for (int i = 1; i < n; i++) {
    ans = (ans + calcC(n - 2 + i, i) * 2 * (n - i)) % mod;
  }
  cout << (ans + n) % mod;
  return 0;
}
