#include <bits/stdc++.h>
using namespace std;
int a[1005];
int main() {
  int n;
  while (cin >> n) {
    int x = 1, y = 1, z = 0, k = 0;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) {
      if (a[i] == 1 && x == 1 && y == 1) {
        y = 0;
        z = 1;
      } else if (a[i] == 2 && x == 1 && y == 1) {
        x = 0;
        z = 1;
      } else if (a[i] == 1 && x == 1 && z == 1) {
        z = 0;
        y = 1;
      } else if (a[i] == 3 && x == 1 && z == 1) {
        x = 0;
        y = 1;
      } else if (a[i] == 2 && y == 1 && z == 1) {
        z = 0;
        x = 1;
      } else if (a[i] == 3 && y == 1 && z == 1) {
        y = 0;
        x = 1;
      } else {
        k = 1;
        break;
      }
    }
    if (k == 1)
      cout << "NO" << endl;
    else if (k == 0)
      cout << "YES" << endl;
  }
  return 0;
}
