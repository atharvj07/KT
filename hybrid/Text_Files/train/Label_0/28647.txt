#include <bits/stdc++.h>
#pragma GCC optimize("-O3")
using namespace std;
const long long N = 1e6 + 5;
void pairsort(long long a[], long long b[], long long n) {
  pair<long long, long long> pairt[n];
  for (long long i = 0; i < n; i++) {
    pairt[i].first = a[i];
    pairt[i].second = b[i];
  }
  sort(pairt, pairt + n);
  for (long long i = 0; i < n; i++) {
    a[i] = pairt[i].first;
    b[i] = pairt[i].second;
  }
}
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
long long isPrime(long long n) {
  if (n < 2) return 0;
  if (n < 4) return 1;
  if (n % 2 == 0 or n % 3 == 0) return 0;
  for (long long i = 5; i * i <= n; i += 6)
    if (n % i == 0 or n % (i + 2) == 0) return 0;
  return 1;
}
long long C(long long n, long long r) {
  if (r > n - r) r = n - r;
  long long ans = 1;
  for (long long i = 1; i <= r; i++) {
    ans *= n - r + i;
    ans /= i;
  }
  return ans;
}
long long mod = 1e9 + 7;
long long modexpo(long long x, long long p) {
  long long res = 1;
  x = x % mod;
  while (p) {
    if (p % 2) res = res * x;
    p >>= 1;
    x = x * x % mod;
    res %= mod;
  }
  return res;
}
long long n;
string s;
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  long long n, k;
  cin >> n >> k;
  vector<long long> vec(n);
  long long lf = 0;
  long long ans = 0;
  long long lim = 2 * k;
  for (long long i = 0; i < n; i++) cin >> vec[i];
  sort(vec.begin(), vec.end());
  while (1) {
    long long l = lf;
    long long r = n - 1;
    long long val = -1;
    long long ind = -1;
    while (l <= r) {
      long long mid = (l + r) / 2;
      if (vec[mid] <= lim) {
        l = mid + 1;
        val = (val > vec[mid] ? val : vec[mid]);
        ind = (ind > mid ? ind : mid);
      } else
        r = mid - 1;
    }
    if (ind == -1) {
      long long nxt = vec[lf];
      while (lim < nxt) {
        ans++;
        lim *= 2;
      }
    } else {
      lf = ind + 1;
      lim = (2 * val > lim ? 2 * val : lim);
      if (lf > n - 1) break;
    }
  }
  cout << ans;
}
