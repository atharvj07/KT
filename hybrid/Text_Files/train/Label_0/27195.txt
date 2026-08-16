#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n;
  cin >> n;
  if (n % 3 != 0) {
    cout << 0 << endl;
    return 0;
  }
  n /= 3;
  int ans = 0;
  for (long long i = 2; i * i * i <= n; ++i) {
    if (n % i != 0) continue;
    long long r = n / i;
    for (long long j = max(
             i, (-i + (long long)sqrt((long double)i * i + 4 * r)) / 2 - 10);
         j * j <= r; ++j) {
      if (r % j != 0) continue;
      long long k = r / j;
      long long a = i - j + k;
      long long b = i + j - k;
      long long c = -i + j + k;
      if (a <= 0 || b <= 0 || c <= 0 || a % 2) continue;
      if (a == b && b == c) {
        ans++;
        continue;
      }
      if (a == b || a == c || b == c) {
        ans += 3;
        continue;
      }
      ans += 6;
    }
  }
  cout << ans << endl;
  return 0;
}
