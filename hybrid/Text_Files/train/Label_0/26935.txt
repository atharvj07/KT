#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t, n, i, j;
  int l, r, x, y, k;
  cin >> l >> r >> x >> y >> k;
  int flag = 0;
  for (int i = l; i <= r; i++) {
    if (i % k == 0) {
      int reqd = i / k;
      if (reqd >= x && reqd <= y) {
        flag = 1;
        break;
      }
    }
  }
  if (flag)
    cout << "YES\n";
  else
    cout << "NO\n";
  return 0;
}
