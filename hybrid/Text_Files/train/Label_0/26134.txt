#include <bits/stdc++.h>
using namespace std;
long long gcd(long long a, long long b) { return (b ? gcd(b, a % b) : a); }
bool isPrime(long long n) {
  if (n == 1) return false;
  if (n == 2) return true;
  for (long long i = 2; i * i <= n; i++) {
    if (n % i == 0) return false;
  }
  return true;
}
long long power(long long x, unsigned long long y, long long p = 1000000007) {
  long long res = 1;
  x = x % p;
  if (x == 0) return 0;
  while (y > 0) {
    if (y & 1) {
      res = (res * x) % p;
    }
    y = y >> 1;
    x = (x * x) % p;
  }
  return res;
}
long long digit(long long n) {
  long long ans = 0;
  while (n) {
    ans++;
    n /= 10;
  }
  return ans;
}
long long lcm(long long a, long long b) { return a * b / gcd(a, b); }
vector<long long> sieve(long long n) {
  long long *arr = new long long[n + 1]();
  vector<long long> vect;
  for (long long i = 2; i <= n; i++)
    if (arr[i] == 0) {
      vect.push_back(i);
      for (long long j = 2 * i; j <= n; j += i) arr[j] = 1;
    }
  return vect;
}
void solve() {
  long long n;
  cin >> n;
  long long a;
  cin >> a;
  long long b;
  cin >> b;
  string s;
  cin >> s;
  vector<vector<long long>> dp(n + 1, vector<long long>(2, 1e18));
  dp[0][0] = b;
  for (long long i = 1; i <= n; i++) {
    if (s[i - 1] == '1') {
      dp[i][1] = dp[i - 1][1] + a + 2 * b;
    } else {
      dp[i][0] = min(dp[i - 1][0] + a, dp[i - 1][1] + a * 2) + b;
      dp[i][1] = min(dp[i - 1][1] + a, dp[i - 1][0] + a * 2) + 2 * b;
    }
  }
  cout << dp[n][0] << endl;
}
int32_t main() {
  ios_base ::sync_with_stdio(false), cin.tie(NULL);
  long long t = 1;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
