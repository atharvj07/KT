#include <bits/stdc++.h>
using namespace std;
int n;
void solve() {
  string ans = "1";
  int i;
  for (i = 2; i < 1e5; i++) {
    if (i * (i - 1) / 2 > n) {
      i--;
      n -= (i * (i - 1)) / 2;
      break;
    }
  }
  i -= 2;
  while (i--) {
    ans += '3';
  }
  while (n--) {
    ans += '1';
  }
  ans += "337";
  cout << ans << endl;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    cin >> n;
    solve();
  }
  return 0;
}
