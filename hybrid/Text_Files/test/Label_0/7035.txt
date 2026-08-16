#include <bits/stdc++.h>
using namespace std;
const int maxn = 100010;
const long long mod = 1000000007;
map<int, int> mp;
map<int, int>::iterator it;
long long fv[maxn], f[maxn];
long long cnt, tot;
long long b[maxn];
long long dp[2100][2100];
long long quick_power(long long x, long long y) {
  long long ans = 1;
  for (; y; y >>= 1) {
    if (y & 1) ans = ans * x % mod;
    x = x * x % mod;
  }
  return ans;
}
void init() {
  f[0] = 1;
  for (long long i = 1; i < maxn; i++) f[i] = (f[i - 1] * i) % mod;
  fv[maxn - 1] = quick_power(f[maxn - 1], mod - 2);
  for (long long i = maxn - 1; i > 0; i--) {
    fv[i - 1] = fv[i] * i % mod;
  }
}
long long C(long long n, long long m) {
  if (n < 0 || m < 0 || n < m) return 0;
  return f[n] * (fv[m]) % mod * fv[n - m] % mod;
}
int main() {
  init();
  int n, m, x;
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &x);
    int y = x;
    while (y) {
      if (y % 10 != 4 && y % 10 != 7) break;
      y /= 10;
    }
    if (!y)
      mp[x]++;
    else
      tot++;
  }
  for (it = mp.begin(); it != mp.end(); it++) {
    b[++cnt] = it->second;
  }
  dp[0][0] = 1;
  for (int i = 1; i <= cnt; i++) {
    dp[i][0] = 1;
    for (int j = 1; j <= i; j++) {
      dp[i][j] = (dp[i - 1][j] + (dp[i - 1][j - 1] * b[i]) % mod) % mod;
    }
  }
  long long ans = 0;
  for (int i = 0; i <= m && i <= cnt; i++) {
    ans = (ans + C(tot, m - i) * dp[cnt][i] % mod) % mod;
  }
  printf("%lld\n", ans);
}
