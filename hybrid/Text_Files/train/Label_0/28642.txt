#include <bits/stdc++.h>
using namespace std;
int main() {
  long long q, n, m, k, mx;
  cin >> q;
  while (q--) {
    cin >> n >> m >> k;
    n = abs(n);
    m = abs(m);
    mx = -1;
    if (max(n, m) <= k) {
      if (n == m) {
        mx = n - 1;
        if ((k - mx) % 2) {
          mx = k;
        } else {
          mx += (k - mx - 2);
        }
      } else {
        mx = max(m, n) - 1;
        if ((n - m) % 2) {
          mx += (k - mx - 1);
        } else {
          if ((k - mx) % 2) {
            mx = k;
          } else {
            mx += (k - mx - 2);
          }
        }
      }
    }
    cout << mx << endl;
  }
  return 0;
}
