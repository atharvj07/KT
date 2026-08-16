#include <bits/stdc++.h>
using namespace std;
const long long maxn = 1e5 + 1, mod = 1e9 + 7, inf = 1e18;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t, a, b, c;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cin >> a >> b >> c;
    int tmp = min(b, c / 2);
    b -= tmp;
    tmp += min(a, b / 2);
    cout << tmp * 3 << endl;
  }
  return 0;
}
