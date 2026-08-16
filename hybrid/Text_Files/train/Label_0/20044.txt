#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, i, j = 0, x, m, p, w = 0, l = 0, k = 0, y = 0, r = 0, yy = 0, mm;
  cin >> n;
  int a[n];
  for (j = 0; j < n; j++) cin >> a[j];
  for (i = 0; i < n - 1; i++) {
    if (a[i + 1] <= 2 * a[i]) {
      l++;
      k = max(k, l);
    } else {
      l = 0;
    }
  }
  cout << k + 1;
  return 0;
}
