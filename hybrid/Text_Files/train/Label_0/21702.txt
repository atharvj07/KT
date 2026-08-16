#include <bits/stdc++.h>
using namespace std;
const long long M = 998244353;
const long long inf = 4e18;
const long long N = 3e5;
long long fac[N + 1];
long long power(long long x, long long y) {
  if (y < 0) return power(x, M - 2) * power(x, y + 1) % M;
  y %= (M - 1);
  long long res = 1;
  while (y > 0) {
    if (y & 1) res = res * x % M;
    y = y >> 1;
    x = x * x % M;
  }
  return res;
}
void factorial() {
  fac[0] = 1;
  for (long long i = 1; i <= N; i++) fac[i] = fac[i - 1] * i % M;
}
long long nCr(long long n, long long r) {
  if (r > n || r < 0) return 0;
  if (r == 0) return 1;
  return (fac[n] * power(fac[r], M - 2) % M * power(fac[n - r], M - 2) % M) % M;
}
int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  factorial();
  long long n, k;
  cin >> n >> k;
  vector<long long> right, left;
  for (long long i = 0; i < n; i++) {
    long long l, r;
    cin >> l >> r;
    left.emplace_back(l);
    right.emplace_back(r);
  }
  sort(left.begin(), left.end());
  sort(right.begin(), right.end());
  long long o = 0;
  for (long long i = 0; i < n; i++) {
    long long j =
        upper_bound(left.begin(), left.end(), right[i]) - left.begin();
    o = (o + nCr(j - i - 1, k - 1)) % M;
  }
  cout << o << '\n';
}
