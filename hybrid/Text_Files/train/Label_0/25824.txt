#include <bits/stdc++.h>
using namespace std;
long long spf[101];
long long fac[101];
void sieve() {
  spf[1] = 1;
  for (long long i = 2; i < 101; i++) spf[i] = i;
  for (long long i = 4; i < 101; i += 2) spf[i] = 2;
  for (long long i = 3; i * i < 101; i++) {
    if (spf[i] == i) {
      for (long long j = i * i; j < 101; j += i)
        if (spf[j] == j) spf[j] = i;
    }
  }
}
map<long long, long long> getfactor(long long a) {
  map<long long, long long> m;
  while (a > 1) {
    m[spf[a]]++;
    a /= spf[a];
  }
  return m;
}
long long power(long long x, long long y, long long p) {
  long long res = 1;
  x = x;
  if (x == 0) return 0;
  while (y > 0) {
    if (y & 1) res = (res * x) % p;
    y = y >> 1;
    x = (x * x) % p;
  }
  return res;
}
long long gcd(long long a, long long b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}
long long inverse(long long a, long long p) { return power(a, p - 2, p); }
long long ncr(long long n, long long r, long long p) {
  if (r == 0) return 1;
  return (fac[n] * inverse(fac[r], p) % p * inverse(fac[n - r], p) % p) % p;
}
long long h[100005], p[100005], n, m;
bool check(long long mid) {
  long long cur = 0;
  for (long long i = 0; i < n; i++) {
    long long diff = abs(h[i] - p[cur]);
    if (diff > mid && h[i] > p[cur]) return 0;
    long long maxi = max(mid - 2 * diff, (mid - diff) / 2);
    maxi = max(0ll, maxi);
    if (h[i] <= p[cur]) maxi = mid;
    while (cur < m && p[cur] <= h[i] + maxi) cur++;
    if (cur >= m) return 1;
  }
  return 0;
}
void solve() {
  cin >> n >> m;
  for (long long i = 0; i < n; i++) cin >> h[i];
  for (long long i = 0; i < m; i++) cin >> p[i];
  long long l = 0, r = 1e12;
  long long ans = 0;
  while (l <= r) {
    long long mid = (l + r) / 2;
    if (check(mid)) {
      r = mid - 1;
      ans = mid;
    } else
      l = mid + 1;
  }
  cout << ans << '\n';
}
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long t = 1;
  while (t--) {
    solve();
  }
}
