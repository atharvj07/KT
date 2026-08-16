#include <bits/stdc++.h>
using namespace std;
const long long mod = 998244353;
long long binpow(long long a, long long p) {
  if (p == 0) return 1;
  if (p % 2)
    return (a * binpow(a, p - 1)) % mod;
  else {
    long long quadra = binpow(a, p / 2);
    return (quadra * quadra) % mod;
  }
}
signed main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long n, k;
  cin >> n >> k;
  vector<long long> fact(300001, 1);
  fact[0] = 1;
  for (long long i = 1; i < fact.size(); i++) {
    fact[i] = (fact[i - 1] * i) % mod;
  }
  vector<pair<long long, long long>> scanline;
  for (long long i = 0; i < n; i++) {
    long long l, r;
    cin >> l >> r;
    scanline.push_back({l, 1});
    scanline.push_back({r + 1, -1});
  }
  sort(scanline.begin(), scanline.end());
  long long bal = 0, res = 0;
  for (long long i = 0; i < 2 * n;) {
    long long elem = scanline[i].first;
    while (i < 2 * n && scanline[i].first == elem && scanline[i].second == -1) {
      bal--;
      i++;
    }
    while (i < 2 * n && scanline[i].first == elem) {
      if (bal >= k - 1)
        res = (res + ((fact[bal] * binpow(fact[k - 1], mod - 2)) % mod *
                      binpow(fact[bal - (k - 1)], mod - 2)) %
                         mod) %
              mod;
      bal++;
      i++;
    }
  }
  cout << res;
}
