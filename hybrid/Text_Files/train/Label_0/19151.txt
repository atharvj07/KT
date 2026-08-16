#include <bits/stdc++.h>
using namespace std;
const long long BINF = 9e18, LINF = 2e9, mod = 998244353, P = 179,
                Q = 1791791791;
const long long MAXN = 1e5 + 7;
long long gcd(long long a, long long b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}
long long first = BINF, second = -BINF;
long long n, k;
void upd(long long a, long long b) {
  long long aa, bb, d;
  for (long long i = 0; i < n; ++i) {
    aa = a;
    bb = b + k * i;
    if (aa > bb)
      d = n * k - (aa - bb);
    else
      d = bb - aa;
    if (d == 0) d = n * k;
    first = min(first, n * k / gcd(d, n * k));
    second = max(second, n * k / gcd(d, n * k));
  }
  return;
}
void solve() {
  cin >> n >> k;
  long long a, b;
  cin >> a >> b;
  upd(a, b);
  upd(a, (k - b) % k);
  upd((k - a) % k, (k - b) % k);
  upd((k - a) % k, b);
  cout << first << " " << second << endl;
  return;
}
signed main() {
  ios_base::sync_with_stdio(false);
  cout.precision(40);
  solve();
  return 0;
}
