#include <bits/stdc++.h>
using namespace std;
const long long MAX = 100000 + 10;
long long a[MAX], d[MAX], n, ans = 0;
long long gcd(long long x, long long y) {
  if (y < x) swap(x, y);
  if (y % x == 0) return x;
  return gcd(x, y % x);
}
int main() {
  ios_base::sync_with_stdio(false);
  cin >> n;
  for (long long i = 0; i < n; i++) {
    cin >> a[i];
    ans += a[i];
  }
  sort(a, a + n);
  d[1] = a[1] - a[0];
  ans += (d[1] * 2);
  for (long long i = 2; i < n; i++) {
    d[i] = (d[i - 1] + (a[i] - a[i - 1]) * i);
    ans += d[i] * 2;
  }
  long long k = gcd(ans, n);
  cout << ans / k << ' ' << n / k << endl;
}
