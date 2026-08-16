#include <bits/stdc++.h>
using namespace std;
const int inf = 2e9;
const long long INF = 8e18;
const int maxn = 5e3 + 5;
const int mod = 998244353;
int n;
long long dp[maxn][maxn], fac[maxn], inv[maxn];
inline long long powmod(long long a, long long b) {
  long long res = 1;
  for (; b; b >>= 1) {
    if (b & 1) res = res * a % mod;
    a = a * a % mod;
  }
  return res;
}
inline void init() {
  dp[0][0] = fac[0] = inv[0] = 1;
  for (int i = 1; i <= n; ++i) fac[i] = fac[i - 1] * i % mod;
  inv[n] = powmod(fac[n], mod - 2);
  for (int i = n - 1; i >= 1; --i) inv[i] = inv[i + 1] * (i + 1) % mod;
  for (int i = 1; i <= n; ++i) {
    dp[i][0] = 1;
    for (int j = 1; j <= i - 1; ++j) {
      dp[i][j] =
          dp[i - 1][j] * (j + 1) % mod + dp[i - 1][j - 1] * (i - j) % mod;
      dp[i][j] %= mod;
    }
  }
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n;
  init();
  for (int i = 1; i <= n; ++i) {
    long long ans = 0;
    for (int j = i; j <= n; ++j) {
      ans += dp[j][i - 1] * inv[j] % mod;
    }
    ans %= mod;
    ans *= fac[n];
    ans %= mod;
    cout << ans << ' ';
  }
  return 0;
}
