#include <bits/stdc++.h>
using namespace std;
const long long M = 998244353ll;
long long l, r, k, p[20];
long long m, dig[20], f[20][2][1 << 11][2], cnt[20][2][1 << 11][2];
long long count(long long x) {
  long long sum = 0;
  while (x) sum += x & 1, x >>= 1;
  return sum;
}
long long dp(long long x, long long lim, long long s, long long p0) {
  if (x == 0) {
    cnt[x][lim][s][p0] = (count(s) <= k);
    return 0;
  }
  if (f[x][lim][s][p0] >= 0) return f[x][lim][s][p0];
  long long res = 0;
  for (long long i = 0; i <= 9; i++) {
    if (!lim && i > dig[x]) break;
    long long lim1 = (lim || i < dig[x]), s1 = (p0 && i == 0 ? s : s | 1 << i),
              p1 = (p0 && i == 0);
    res = (res + dp(x - 1, lim1, s1, p1)) % M;
    cnt[x][lim][s][p0] = (cnt[x][lim][s][p0] + cnt[x - 1][lim1][s1][p1]) % M;
    res = (res + i * p[x - 1] % M * cnt[x - 1][lim1][s1][p1] % M) % M;
  }
  return f[x][lim][s][p0] = res;
}
long long calc(long long x) {
  memset(dig, 0, sizeof(dig));
  memset(f, -1, sizeof(f));
  memset(cnt, 0, sizeof(cnt));
  m = 0;
  while (x) dig[++m] = x % 10, x /= 10;
  return dp(m, 0, 0, 1) % M;
}
signed main() {
  p[0] = 1;
  for (long long i = 1; i < 20; i++) p[i] = p[i - 1] * 10 % M;
  cin >> l >> r >> k;
  cout << (calc(r) - calc(l - 1) + M) % M << endl;
  return 0;
}
