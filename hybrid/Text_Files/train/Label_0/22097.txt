#include <bits/stdc++.h>
using namespace std;
long long x, y, z, n, m, q;
long long a[155];
string pat = "aoeui";
int main() {
  long long q;
  cin >> q;
  while (q--) {
    long long l, r, x;
    cin >> l >> r >> x;
    long long fl = 0;
    if (l == r) {
      cout << 1 << " " << l << endl;
      continue;
    }
    x--;
    for (int i = 0; i < 50; i++) {
      if ((l + 1) * (1LL << i) > r) {
        break;
      }
      long long lft = r - (l + 1) * (1LL << i);
      if (lft <= (1LL << i) * x) {
        a[0] = l;
        for (int j = 0; j <= i; j++) {
          a[j + 1] = 1;
          for (int k = 0; k <= j; k++) {
            a[j + 1] += a[k];
          }
        }
        for (int j = i; j >= 0; j--) {
          long long pr = j;
          if (pr > 0) {
            pr--;
          }
          long long px = (lft >> pr);
          px = min(px, x);
          lft -= px * (1LL << pr);
          for (int k = i + 1 - j; k <= i + 1; k++) {
            long long df = (k - (i + 1 - j));
            if (df > 0) {
              df--;
            }
            a[k] += px * (1LL << df);
          }
        }
        cout << i + 2;
        for (int k = 0; k <= i + 1; k++) {
          cout << " " << a[k];
        }
        cout << endl;
        fl = 1;
        break;
      }
    }
    if (!fl) {
      cout << -1 << endl;
    }
  }
  return 0;
}
