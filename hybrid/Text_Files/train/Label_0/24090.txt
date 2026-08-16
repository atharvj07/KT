#include <bits/stdc++.h>
using namespace std;
int a[111];
int main() {
  int n, m, i, j, d, k, l, x = 0;
  cin >> n >> d >> l;
  fill(a, a + n, 1);
  if (n % 2) d--;
  for (i = 0; i < n && d != 0; i += 2) {
    if (d > 0) {
      if (d > l - 1) {
        a[i] = l;
        d -= (l - 1);
      } else {
        a[i] += d;
        d = 0;
      }
    } else {
      if (i + 1 == n) break;
      if (-d > l - 1) {
        a[i + 1] = l;
        d += (l - 1);
      } else {
        a[i + 1] += -d;
        d = 0;
      }
    }
  }
  if (d)
    cout << -1;
  else
    for (i = 0; i < n; i++) cout << a[i] << ' ';
}
