#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    int rem = 0, i = 0;
    while (i * (i - 1) / 2 <= n) ++i;
    if (i * (i - 1) / 2 > n) --i;
    rem = n - i * (i - 1) / 2;
    cout << 133;
    while (rem--) {
      cout << 7;
    }
    i -= 2;
    while (i--) cout << 3;
    cout << 7 << endl;
  }
  return 0;
}
