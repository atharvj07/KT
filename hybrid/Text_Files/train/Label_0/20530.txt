#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, i, j, x = 1, y = 1, ans = 0;
  cin >> n;
  for (i = 2; x < n; x += i, i++, y = 1) {
    for (j = 2; y < n - x; y += j, j++) {
    }
    if (x + y == n) ans = 1;
  }
  ans ? cout << "YES" : cout << "NO";
}
