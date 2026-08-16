#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1e9 + 7;
const long long N = 2e5 + 5;
const long double pi = 3.14159265;
long long gcd(long long a_, long long b_) {
  if (b_ > a_) swap(b_, a_);
  return (b_ == 0 ? a_ : gcd(b_, a_ % b_));
}
long long n, m, k;
long long p(long long d, long long t) {
  if (t == 0) return 1;
  long long tmp = p(d, t / 2);
  if (t % 2) return tmp * tmp % MOD * d % MOD;
  return tmp * tmp % MOD;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m >> k;
  if (k == -1 && (n % 2 != m % 2)) {
    cout << 0;
    return 0;
  }
  cout << p(p(2, n - 1), m - 1);
  return 0;
}
