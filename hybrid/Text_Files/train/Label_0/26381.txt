#include <bits/stdc++.h>
using namespace std;
int main() {
  int m, n, i, x;
  cin >> n >> m;
  if (n < m) {
    cout << -1;
    return 0;
  }
  if (n == m) {
    cout << n;
    return 0;
  }
  if (n % 2 == 0) {
    x = n / 2;
    if (x % m == 0) {
      cout << x;
      return 0;
    }
    for (i = x + 1; i <= n; i++) {
      if (i % m == 0) {
        cout << i;
        return 0;
      }
    }
  } else {
    x = (n - 1) / 2;
    x = x + 1;
    if (x % m == 0) {
      cout << x;
      return 0;
    }
    for (i = x + 1; i <= n; i++) {
      if (i % m == 0) {
        cout << i;
        return 0;
      }
    }
  }
  cout << -1;
}
