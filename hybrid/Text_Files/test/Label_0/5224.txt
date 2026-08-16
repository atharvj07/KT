#include <bits/stdc++.h>
using namespace std;
long long mpow(long long x, long long y, long long m) {
  long long res = 1;
  while (y > 0) {
    if (y & 1) res = res * x % m;
    y = y >> 1;
    x = x * x % m;
  }
  return res;
}
void solve() {
  long long n, k;
  cin >> n >> k;
  long long a[n], dp[n + 1][2];
  for (long long i = (0); i < (n); i++) cin >> a[i];
  dp[0][0] = 1, dp[0][1] = 0;
  for (long long i = (1); i < (n + 1); i++) {
    dp[i][0] = (k - 1) * dp[i - 1][1] % 998244353ll;
    dp[i][1] = (dp[i - 1][0] + (k - 2) * dp[i - 1][1]) % 998244353ll;
  }
  long long ans = 1, last = -1;
  for (long long i = 0; i < n; i += 2) {
    if (a[i] != -1) {
      if (last == -1)
        ans = ans * mpow(k - 1, i / 2, 998244353ll) % 998244353ll;
      else {
        if (a[i] == a[last])
          ans = ans * ((k - 1) * dp[(i - last) / 2 - 1][1] % 998244353ll) %
                998244353ll;
        else
          ans = ans *
                ((k - 2) * dp[(i - last) / 2 - 1][1] % 998244353ll +
                 dp[(i - last) / 2 - 1][0]) %
                998244353ll;
      }
      last = i;
    }
  }
  if (last == -1)
    ans = ans * mpow(k - 1, (n - 1) / 2, 998244353ll) % 998244353ll * k %
          998244353ll;
  else
    ans = ans * mpow(k - 1, (n - 1 - last) / 2, 998244353ll) % 998244353ll;
  last = -1;
  for (long long i = 1; i < n; i += 2) {
    if (a[i] != -1) {
      if (last == -1)
        ans = ans * mpow(k - 1, i / 2, 998244353ll) % 998244353ll;
      else {
        if (a[i] == a[last])
          ans = ans * ((k - 1) * dp[(i - last) / 2 - 1][1] % 998244353ll) %
                998244353ll;
        else
          ans = ans *
                ((k - 2) * dp[(i - last) / 2 - 1][1] % 998244353ll +
                 dp[(i - last) / 2 - 1][0]) %
                998244353ll;
      }
      last = i;
    }
  }
  if (last == -1)
    ans = ans * mpow(k - 1, n / 2 - 1, 998244353ll) % 998244353ll * k %
          998244353ll;
  else
    ans = ans * mpow(k - 1, (n - 1 - last) / 2, 998244353ll) % 998244353ll;
  cout << ans;
}
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long t = 1;
  for (long long i = (1); i < (t + 1); i++) {
    solve();
    cout << "\n";
  }
}
