#include <bits/stdc++.h>
using namespace std;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const int MAX = 200010;
const long long MOD = (int)1e9 + 7;
const int INF = 1e9;
const long long LLINF = 0x3f3f3f3f3f3f3f3f;
const long double EPS = 1e-8;
long long fact[100010];
int qt[72];
vector<int> p;
long long fexp(long long b, long long e) {
  assert(e >= 0);
  if (e == 0) return 1;
  long long res = (fexp(b, e / 2)) % MOD;
  res = (res * res) % MOD;
  if (e % 2) res = (res * b) % MOD;
  return res;
}
long long inv(long long a) { return fexp(a, MOD - 2); }
long long comb(long long a, long long b) {
  long long num = fact[a];
  long long denom = (fact[a - b] * fact[b]) % MOD;
  return (num * inv(denom)) % MOD;
}
int solve(int num) {
  int res = 0;
  for (int i = 0; i < (int)p.size(); i++) {
    int e = 0;
    while (num % p[i] == 0) {
      e ^= 1;
      num /= p[i];
    }
    if (e) res ^= (1 << i);
  }
  return res;
}
int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  ;
  int n;
  cin >> n;
  for (int i = 0; i < (int)n; i++) {
    int val;
    cin >> val;
    qt[val]++;
  }
  for (int i = 2; i <= 70; i++) {
    bool primo = true;
    for (int j = 2; j < i; j++) {
      if (i % j == 0) {
        primo = false;
        break;
      }
    }
    if (primo) p.push_back(i);
  }
  fact[0] = 1;
  fact[1] = 1;
  for (long long i = 2; i <= 100000; i++) {
    fact[i] = (i * fact[i - 1]) % MOD;
  }
  vector<long long> ant((1 << 19) + 1, 0);
  ant[0] = 1;
  for (int val = 70; val >= 1; val--) {
    vector<long long> cur((1 << 19) + 1, 0);
    long long nmask = solve(val);
    long long qpega = 0, qnpega = 0;
    for (int i = 0; i <= qt[val]; i += 2)
      qnpega = (qnpega + comb(qt[val], i)) % MOD;
    for (int i = 1; i <= qt[val]; i += 2)
      qpega = (qpega + comb(qt[val], i)) % MOD;
    for (int mask = 0; mask < (1 << 19); mask++) {
      cur[mask] = (cur[mask] + qnpega * ant[mask]) % MOD;
      cur[mask] = (cur[mask] + qpega * ant[mask ^ nmask]) % MOD;
    }
    swap(ant, cur);
  }
  long long res = (ant[0] - 1 + MOD) % MOD;
  cout << res << '\n';
  return 0;
}
