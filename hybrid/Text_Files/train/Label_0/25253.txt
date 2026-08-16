#include <bits/stdc++.h>
using namespace std;
int a[100005];
int b[100005];
int c[100005];
int main() {
  int t;
  cin >> t;
  while (t--) {
    memset(a, 0, sizeof a);
    memset(b, 0, sizeof b);
    memset(c, 0, sizeof c);
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    for (int i = 1; i <= n; i++) cin >> b[i];
    for (int i = 1; i <= n; i++) a[i] = a[i] - b[i];
    for (int i = 1; i <= n + 1; i++) c[i] = a[i] - a[i - 1];
    int x = 0;
    int f = 0;
    for (int i = 1; i <= n + 1; i++) {
      if (c[i] != 0) x++;
    }
    for (int i = 1; i <= n; i++) {
      if (a[i] > 0) {
        cout << "no" << endl;
        f = 1;
        break;
      }
    }
    if (f == 0) {
      if (x == 2 || x == 0)
        cout << "yes" << endl;
      else
        cout << "no" << endl;
    }
  }
  return 0;
}
