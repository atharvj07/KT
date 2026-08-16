#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    if (m >= i) {
      m -= i;
      if (i == n) {
        i = 0;
        continue;
      }
    } else {
      cout << m;
      return 0;
    }
  }
  cout << 0;
  return 0;
}
