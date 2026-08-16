#include <bits/stdc++.h>
using namespace std;
int main() {
  long long q, t, n, k, d1, d2, x, y;
  cin >> t;
  while (t--) {
    cin >> n >> k >> d1 >> d2;
    q = k;
    k = n - k;
    if (k - (d1 + d2) >= 0) {
      x = (d1 + d2 + q) / 3;
      y = (q - d1 - d2) / 3;
      if ((k - (d1 + d2)) % 3 == 0 && (d1 + d2 + q) % 3 == 0 && (x - d1 >= 0) &&
          (x - d2) >= 0) {
        cout << "yes\n";
        continue;
      }
    }
    if ((k - (2 * max(d1, d2) - min(d1, d2))) >= 0) {
      x = (q - d1 - d2) / 3;
      if ((k - (2 * max(d1, d2) - min(d1, d2))) % 3 == 0 &&
          (q - d1 - d2) % 3 == 0 && x >= 0) {
        cout << "yes\n";
        continue;
      }
    }
    if (k - (d1 + 2 * d2) >= 0) {
      x = (q + d1 - d2) / 3;
      if ((k - (d1 + 2 * d2)) % 3 == 0 && (q + d1 - d2) % 3 == 0 &&
          (x - d1) >= 0) {
        cout << "yes\n";
        continue;
      }
    }
    if (k - (2 * d1 + d2) >= 0) {
      x = (q - d1 + d2) / 3;
      if ((k - (2 * d1 + d2)) % 3 == 0 && (q - d1 + d2) % 3 == 0 &&
          (x - d2) >= 0) {
        cout << "yes\n";
        continue;
      }
    }
    cout << "no\n";
  }
}
