#include <bits/stdc++.h>
using namespace std;
int main() {
  int i, n, k;
  string s;
  cin >> n >> k;
  cin >> s;
  if (k <= n / 2) {
    while (k > 1) {
      cout << "LEFT\n";
      --k;
    }
    while (k <= n) {
      cout << "PRINT " << s[k - 1] << '\n';
      if (k != n) cout << "RIGHT\n";
      ++k;
    }
  } else {
    while (k < n) {
      cout << "RIGHT\n";
      ++k;
    }
    while (k >= 1) {
      cout << "PRINT " << s[k - 1] << '\n';
      if (k > 1) cout << "LEFT\n";
      --k;
    }
  }
  return 0;
}
