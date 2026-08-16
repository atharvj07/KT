#include <bits/stdc++.h>
#pragma GCC optimize("unroll-loops,no-stack-protector")
#pragma GCC target("sse,sse2,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
using namespace std;
const int MOD = 998244353;
const int INF32 = 1 << 30;
const long long INF64 = 1LL << 60;
const long double pi = acos(-1);
long long gcd(long long a, long long b) { return (!b ? a : gcd(b, a % b)); }
long long lcm(long long a, long long b) { return a * b / gcd(a, b); }
long long modpow(long long b, long long i) {
  long long s = 1;
  while (i) {
    if (i % 2) s = (s * b) % MOD;
    b = (b * b) % MOD;
    i /= 2;
  }
  return s;
}
long long inv(long long a) { return modpow(a, MOD - 2); }
long long add(long long a, long long b) { return (a + b) % MOD; }
long long sub(long long a, long long b) { return (a - b + MOD) % MOD; }
long long mul(long long a, long long b) { return a * b % MOD; }
long long nCr(long long n, long long r) {
  long long m1 = 1, m2 = 1;
  r = min(r, n - r);
  for (int i = 0; i < r; i++) {
    m1 = (m1 * (n - i)) % MOD;
    m2 = (m2 * (r - i)) % MOD;
  }
  return (m1 * inv(m2)) % MOD;
}
void solve() {
  int n;
  cin >> n;
  int cnt = 0, sum = 0, mn = 1000;
  for (int i = 0; i < 2 * n - 1; i++) {
    int x;
    cin >> x;
    if (x < 0) cnt++;
    sum += abs(x);
    mn = min(mn, abs(x));
  }
  if (n % 2 == 0 && cnt % 2)
    cout << sum - 2 * mn;
  else
    cout << sum;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  solve();
  return 0;
}
