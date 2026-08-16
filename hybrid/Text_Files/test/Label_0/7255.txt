#include <bits/stdc++.h>
using namespace std;
const long long mod = (1e9 + 7);
const long long inf = (1e18 + 3);
const long long N = 1e3 + 2;
long long powmod(long long a, long long b) {
  long long res = 1;
  a %= mod;
  assert(b >= 0);
  for (; b; b >>= 1) {
    if (b & 1) res = res * a % mod;
    a = a * a % mod;
  }
  return res;
}
long long gcd(long long a, long long b) { return b ? gcd(b, a % b) : a; }
long long res = inf;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long n, d;
  cin >> n >> d;
  long long arr[n];
  for (long long i = 0; i < n; i++) cin >> arr[i];
  sort(arr, arr + n);
  for (long long i = 0, j = 0; i < n; i++) {
    while (arr[i] - arr[j] > d) j++;
    res = min(j + n - i - 1, res);
  }
  cout << res;
  return 0;
}
