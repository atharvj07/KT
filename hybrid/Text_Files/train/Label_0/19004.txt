#include <bits/stdc++.h>
using namespace std;
long long choice(long long a, long long b) {
  long long opt1 = min(a / 2, b);
  a -= 2 * opt1;
  b -= opt1;
  long long opt2 = min(a, b / 2);
  return opt1 + opt2;
}
void solve() {
  long long a, b;
  cin >> a >> b;
  if ((a + b) / 3 <= min(a, b)) {
    cout << (a + b) / 3 << endl;
    return;
  };
  cout << min(a, b) << endl;
}
int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
