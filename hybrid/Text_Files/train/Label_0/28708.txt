#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const long long LINF = 0x3f3f3f3f3f3f3f3fll;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int n, m, x, y;
    cin >> n >> m >> x >> y;
    long long ans = 0;
    y = min(y, 2 * x);
    for (int i = 0; i < n; i++) {
      int now = 0;
      for (int j = 0; j < m; j++) {
        char c;
        cin >> c;
        if (c == '*') {
          ans += x * (now % 2);
          ans += y * (now / 2);
          now = 0;
        } else
          now++;
      }
      ans += x * (now % 2);
      ans += y * (now / 2);
    }
    cout << ans << '\n';
  }
  exit(0);
}
