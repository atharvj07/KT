#include <bits/stdc++.h>
using namespace std;
const int N = 100000;
const int inf = (int)1e9 + 1;
const long long big = (long long)1e18 + 1;
const int P = 239;
const int MOD = (int)1e9 + 7;
const int MOD1 = (int)1e9 + 9;
const double eps = 1e-9;
const double pi = atan2(0, -1);
long long bin_pow(long long a, long long p) {
  long long res = 1;
  while (p) {
    if (p & 1) res = (res * a) % MOD;
    a = (a * a) % MOD;
    p >>= 1;
  }
  return res;
}
long long rev(long long x) { return bin_pow(x, MOD - 2); }
long long solve(long long n, long long k) {
  n %= MOD;
  long long pw[k + 2];
  pw[0] = 0;
  for (int i = 1; i < k + 2; i++) {
    pw[i] = bin_pow(i, k);
    pw[i] = (pw[i] + pw[i - 1]) % MOD;
  }
  if (n <= k + 1) return pw[n];
  long long cur = 1, ans = 0;
  for (int i = 1; i < k + 2; i++) {
    cur = cur * (n - i) % MOD;
    cur = cur * rev(0 - i + MOD) % MOD;
  }
  for (int i = 0; i < k + 2; i++) {
    ans = (ans + pw[i] * cur) % MOD;
    if (i == k + 1) break;
    cur = cur * (n - i) % MOD;
    cur = cur * rev(n - (i + 1)) % MOD;
    cur = cur * rev(i + 1) % MOD;
    cur = cur * (-((k + 1) - i) + MOD) % MOD;
  }
  return ans;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.precision(20);
  long long n, k;
  cin >> n >> k;
  cout << solve(n, k) << "\n";
  return 0;
}
