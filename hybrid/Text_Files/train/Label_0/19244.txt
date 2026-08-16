#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  long long inf = 300000000000;
  long long a[n], b[n], c[n];
  for (int i = 0; i < n; i++) {
    a[i] = 0;
    b[i] = 0;
    c[i] = inf;
  }
  int t[m], l[m], r[m], d[m];
  for (int i = 0; i < m; i++) {
    cin >> t[i];
    if (t[i] == 1) {
      cin >> l[i] >> r[i] >> d[i];
      for (int j = l[i] - 1; j < r[i]; j++) {
        a[j] += d[i];
      }
    } else {
      cin >> l[i] >> r[i] >> d[i];
      for (int j = l[i] - 1; j < r[i]; j++) {
        c[j] = min(c[j], d[i] - a[j]);
      }
    }
  }
  for (int i = 0; i < n; i++) {
    if (c[i] == inf) {
      b[i] = -2000000;
      c[i] = -2000000;
    } else
      b[i] = c[i];
  }
  long long ma, posma;
  for (int i = 0; i < m; i++) {
    if (t[i] == 1) {
      for (int j = l[i] - 1; j < r[i]; j++) {
        b[j] += d[i];
      }
    } else {
      ma = b[l[i] - 1];
      for (int j = l[i] - 1; j < r[i]; j++) {
        posma = b[j];
        if (posma > ma) ma = posma;
      }
      if (ma != d[i]) {
        cout << "NO" << endl;
        return 0;
      }
    }
  }
  cout << "YES" << endl;
  for (int i = 0; i < n; i++) {
    if (i) cout << ' ';
    cout << c[i];
  }
  cout << endl;
  return 0;
}
