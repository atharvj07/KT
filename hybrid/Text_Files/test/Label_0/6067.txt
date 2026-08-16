#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.precision(10);
  cout << fixed;
  int n, m;
  cin >> n >> m;
  int l = (n + m) * 6;
  int ans = 0;
  for (int i = 1; i <= l; i++) {
    if (i % 2 == 0 && i % 3 == 0) {
      if (n > m) {
        n--;
      } else if (n < m) {
        m--;
      } else {
        m--;
      }
    } else if (i % 2 == 0 && n > 0) {
      n--;
    } else if (i % 3 == 0 && m > 0) {
      m--;
    }
    if (n == 0 && m == 0) {
      ans = i;
      break;
    }
  }
  cout << ans;
  return 0;
}
