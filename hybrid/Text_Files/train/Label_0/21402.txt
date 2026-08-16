#include <bits/stdc++.h>
using namespace std;
int n, m, k, l, r, t, qq;
int a[1000009];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> qq;
  while (qq--) {
    cin >> n >> k;
    m = 0;
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
      if (a[i] == k) m = 1;
      if (a[i] >= k)
        a[i] = 1;
      else if (a[i] < k)
        a[i] = 0;
    }
    if (m != 1) {
      cout << "no\n";
      continue;
    }
    m = 0;
    if (n == 1) {
      cout << "yes\n";
      continue;
    }
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        if (j - i > 2) break;
        if (a[i] != 0 && a[j] != 0) {
          m = 1;
          break;
        }
      }
      if (m == 1) break;
    }
    if (m == 1)
      cout << "yes\n";
    else
      cout << "no\n";
  }
  return 0;
}
