#include <bits/stdc++.h>
using namespace std;
const long long mod = 998244353;
const long long lmt = 3e5 + 5;
long long n, k, fac[lmt], inv[lmt];
pair<long long, long long> a[lmt];
map<long long, long long> m;
set<long long> s;
long long bigmod(long long n, long long p) {
  if (p == 0) return 1;
  long long x = bigmod(n, p / 2) % mod;
  x = (x * x) % mod;
  if (p % 2) x = (x * n) % mod;
  return x;
}
long long ncr(long long n, long long r) {
  if (r > n) return 0;
  long long res = fac[n] % mod;
  res = (res * inv[n - r]) % mod;
  res = (res * inv[r]) % mod;
  return res;
}
int main() {
  ios_base::sync_with_stdio(false);
  fac[0] = inv[0] = 1;
  for (long long i = 1; i < lmt; i++) {
    fac[i] = (fac[i - 1] * i) % mod;
    inv[i] = bigmod(fac[i], mod - 2) % mod;
  }
  cin >> n >> k;
  for (long long i = 1; i <= n; i++) {
    cin >> a[i].first >> a[i].second;
    s.insert(a[i].first);
    s.insert(a[i].second);
  }
  long long indx = 0;
  for (auto &x : s) {
    indx++;
    m[x] = indx;
  }
  for (long long i = 1; i <= n; i++) {
    a[i].first = m[a[i].first], a[i].second = m[a[i].second];
  }
  vector<long long> start[indx + 1], end[indx + 1];
  for (long long i = 1; i <= n; i++) {
    start[a[i].first].push_back(i);
    end[a[i].second].push_back(i);
  }
  set<long long> s;
  s.clear();
  long long ans = 0;
  for (long long i = 1; i <= indx; i++) {
    for (long long x : start[i]) {
      ans = (ans + ncr(s.size(), k - 1)) % mod;
      s.insert(x);
    }
    for (long long x : end[i]) {
      s.erase(x);
    }
  }
  cout << ans << "\n";
  return 0;
}
