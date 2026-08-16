#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int ans = 0, i, k, n, x, a = 1;
  std::ios::sync_with_stdio(false);
  cin >> n;
  for (i = 0; i < n; ++i) {
    cin >> k;
    if (i == 0) {
      x = k;
      continue;
    }
    if (k == x)
      a++;
    else {
      ans += a * (a + 1) / 2;
      a = 1;
      x = k;
    }
  }
  ans += a * (a + 1) / 2;
  cout << ans << endl;
  return 0;
}
