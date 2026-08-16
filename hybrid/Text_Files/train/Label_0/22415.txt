#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const int inf = 0x3f3f3f3f;
long long gcd(long long x, long long y) {
  if (y == 0)
    return x;
  else
    return gcd(y, x % y);
}
long long ksm(long long a, long long b) {
  long long r = 1;
  while (b) {
    if (b & 1) r = (r * a) % mod;
    a = a * a % mod;
    b >>= 1;
  }
  return r;
}
void exgcd(long long a, long long b, long long& d, long long& x, long long& y) {
  if (!b) {
    d = a;
    x = 1;
    y = 0;
  } else {
    exgcd(b, a % b, d, y, x);
    y -= x * (a / b);
  }
}
long long inv(long long a, long long p) {
  long long d, x, y;
  exgcd(a, p, d, x, y);
  return d == 1 ? (x + p) % p : -1;
}
inline int read() {
  char c = getchar();
  int x = 0, f = 1;
  while (c < '0' || c > '9') {
    if (c == '-') f = -1;
    c = getchar();
  }
  while (c >= '0' && c <= '9') {
    x = x * 10 + c - '0';
    c = getchar();
  }
  return x * f;
}
const int maxn = 2e4 + 100;
int n, m, k, t, l, r, dp[maxn];
int x[maxn], y[maxn], ans = 0, mx = 0;
struct qw {
  int h, v;
  qw() {}
  qw(int xx, int yy) { h = xx, v = yy; }
  bool operator<(const qw& x) const {
    if (v != x.v)
      return v < x.v;
    else
      return h > x.h;
  }
} a[maxn], b[maxn];
int n1 = 0, n2 = 0, sum[maxn];
int main() {
  n = read();
  l = read();
  r = read();
  for (int i = 1; i <= n; i++) {
    a[i].h = read();
    mx += a[i].h;
  }
  for (int i = 1; i <= n; i++) a[i].v = read();
  sort(a + 1, a + 1 + n);
  memset(dp, -1, sizeof(dp));
  dp[0] = 0;
  for (int i = 1; i <= n; i++)
    for (int j = mx; j >= a[i].h; j--) {
      if (dp[j - a[i].h] == -1) continue;
      if (j <= mx - l && j >= mx - r)
        dp[j] = max(dp[j], dp[j - a[i].h] + a[i].v);
      else
        dp[j] = max(dp[j], dp[j - a[i].h]);
    }
  for (int i = 0; i <= mx; i++) ans = max(ans, dp[i]);
  cout << ans << endl;
}
