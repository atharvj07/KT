#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, pos, l, r;
  cin >> n >> pos >> l >> r;
  int ans;
  if (l == 1 && r == n) {
    ans = 0;
  } else if (l == 1 && r != n) {
    ans = 1 + abs(r - pos);
  } else if (l != 1 && r == n) {
    ans = 1 + abs(pos - l);
  } else {
    if (pos == l) {
      ans = 1 + r - l + 1;
    } else if (pos == r) {
      ans = 1 + r - l + 1;
    } else {
      ans = r - l + 2 + min(abs(pos - l), abs(pos - r));
    }
  }
  cout << ans << endl;
  return 0;
}
