#include <bits/stdc++.h>
using namespace std;
int main() {
  long long a, b, n, l, t, m;
  cin >> a >> b >> n;
  while (n--) {
    cin >> l >> t >> m;
    if (a + (l - 1) * b > t) {
      cout << -1 << endl;
      continue;
    }
    long long L = l, R = t * m;
    long long f = a + (l - 1) * b;
    while (L < R) {
      long long mid = L + R + 1 >> 1;
      long long e = a + (mid - 1) * b;
      long long s = (f + e) * (mid - l + 1) / 2;
      if (e <= t && s <= t * m)
        L = mid;
      else
        R = mid - 1;
    }
    cout << L << endl;
  }
  return 0;
}
