#include <bits/stdc++.h>
using namespace std;
void solve() {
  int n, k;
  cin >> n >> k;
  int ans = n - n % k;
  ans += min(n % k, k / 2);
  cout << ans << endl;
}
int main() {
  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
