#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int64_t a, b, c;
  cin >> a >> b >> c;
  if (c == 0) {
    if (a == b) {
      cout << "YES" << '\n';
    } else {
      cout << "NO" << '\n';
    }
    return 0;
  }
  int64_t d = b - a;
  int64_t k = d / c;
  if (d % c != 0 || k < 0) {
    cout << "NO" << '\n';
    return 0;
  }
  cout << "YES" << '\n';
  return 0;
}
