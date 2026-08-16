#include <bits/stdc++.h>
using namespace std;
int t, n, a[100500];
int main() {
  cin >> t;
  while (t--) {
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) scanf("%d", a + i);
    bool f = true, f2 = true;
    int las = 0, now = 0;
    for (int i = n; i; --i) {
      if (f)
        now = a[i], f = false;
      else if (a[i] + 1 != a[i + 1]) {
        f2 = false;
        break;
      }
      if (a[i] == las + 1) f = true, las = now;
    }
    if (f2 && las == n)
      cout << "Yes\n";
    else
      cout << "No\n";
  }
}
