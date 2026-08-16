#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n, l, r;
  cin >> n >> l >> r;
  long long ans = 0;
  long long now = 0;
  for (int i = 1; i <= n; ++i) {
    long long a, b;
    cin >> a >> b;
    ans += (a - now) / r;
    now = a + b;
  }
  ans += (l - now) / r;
  cout << ans << endl;
  return 0;
}
