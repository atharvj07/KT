#include <bits/stdc++.h>
using namespace std;
const long long N = 5e3 + 10, K = 30, MOD = 1e9 + 7;
long long fac[N + 1], inv[N + 1], dp[N][N], ps[N], R[K];
long long mul(long long a, long long b) {
  a %= MOD, b %= MOD;
  return (a * b) % MOD;
}
long long Pow(long long a, long long b) {
  long long r = 1;
  for (; b; b >>= 1, a = mul(a, a))
    if (b & 1) r = mul(r, a);
  return r;
}
long long C(long long n, long long k) {
  if (k > n || k < 0 || n < 0) return 0;
  return mul(fac[n], mul(inv[k], inv[n - k]));
}
int32_t main() {
  fac[0] = 1;
  for (long long i = 1; i <= N; i++) fac[i] = mul(fac[i - 1], i);
  inv[N] = Pow(fac[N], MOD - 2);
  for (long long i = N - 1; i >= 0; i--) inv[i] = mul(inv[i + 1], i + 1);
  long long n;
  cin >> n;
  string s;
  cin >> s;
  for (long long i = 1; i <= n; i++) {
    long long c = s[i - 1] - 'a';
    dp[i][1] = 1;
    for (long long j = 2; j <= i; j++)
      dp[i][j] = (ps[j - 1] - dp[R[c]][j - 1] + MOD) % MOD;
    for (long long j = 1; j <= i; j++)
      ps[j] = (ps[j] - dp[R[c]][j] + dp[i][j] + MOD) % MOD;
    R[c] = i;
  }
  long long ans = 0;
  for (long long i = 0; i < 26; i++)
    for (long long j = 1; j <= n; j++) {
      ans += mul(dp[R[i]][j], C(n - 1, j - 1));
      ans %= MOD;
    }
  cout << ans << "\n";
}
