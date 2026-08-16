#include <bits/stdc++.h>
using namespace std;
int main() {
  int ans, w, h, k;
  cin >> w >> h >> k;
  ans = 0;
  for (int i = 0; i < 4 * k; i += 4) {
    ans += 2 * (h - i) + 2 * (w - i) - 4;
  }
  cout << ans << endl;
  return 0;
}
