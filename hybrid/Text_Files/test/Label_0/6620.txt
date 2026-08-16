#include <bits/stdc++.h>
using namespace std;
long long mod = 1000000000 + 7;
long long powe(long long x, long long y) {
  x = x % mod, y = y % (mod - 1);
  long long ans = 1;
  while (y > 0) {
    if (y & 1) {
      ans = (1ll * x * ans) % mod;
    }
    y >>= 1;
    x = (1ll * x * x) % mod;
  }
  return ans;
}
void fun() {}
bool isPrime(long long n) {
  for (long long i = 2; i * i <= n; i++)
    if (n % i == 0) return false;
  return true;
}
signed main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  fun();
  long long tt = 1;
  while (tt--) {
    long long n, a, b, c;
    cin >> n >> a >> b >> c;
    if (n < b or b - c >= a) return cout << n / a, 0;
    long long count = (n - c) / (b - c);
    long long left = (n - c) % (b - c);
    n = c + left;
    count += n / a;
    cout << count;
  }
  return 0;
}
