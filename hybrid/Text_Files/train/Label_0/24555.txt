#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int n, x, y;
  cin >> n >> x >> y;
  string s;
  cin >> s;
  int ans = 0;
  for (int i = n - 1; i >= n - x; --i) {
    if (i == n - y - 1 || i == n - x - 1) {
      if (s[i] != '1') ++ans;
    } else if (s[i] == '1') {
      ++ans;
    }
  }
  cout << ans << '\n';
}
