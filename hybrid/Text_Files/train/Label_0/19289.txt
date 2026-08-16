#include <bits/stdc++.h>
using namespace std;
int main() {
  int64_t n, m, i, j, r, s, a[600][600];
  cin >> n >> m;
  s = 0;
  r = 0;
  for (i = 1; i <= n; i++)
    for (j = 1; j <= m; j++) {
      cin >> a[n - i][m - j];
    }
  for (i = 0; i < n; i++)
    for (j = 0; j < m; j++) {
      if (a[i][j] == 0) {
        if (a[i - 1][j] > a[i][j - 1]) {
          a[i][j] = a[i][j - 1] - 1;
        } else {
          a[i][j] = a[i - 1][j] - 1;
        }
      }
      if (a[i][j] <= a[i + 1][j] or a[i][j] <= a[i][j + 1]) {
        r = -1;
      }
      s = s + a[i][j];
    }
  if (r != -1) {
    cout << s;
  } else {
    cout << r;
  }
}
