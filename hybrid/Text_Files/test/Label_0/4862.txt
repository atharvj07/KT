#include <bits/stdc++.h>
using namespace std;
int main() {
  int t, n, i, j, k, c, mn;
  cin >> t;
  for (i = 0; i < t; i++) {
    c = 0;
    mn = 999999999;
    cin >> n;
    int a[n];
    for (j = 0; j < n; j++) {
      cin >> a[j];
    }
    for (j = n - 1; j >= 0; j--) {
      if (mn >= a[j]) {
        mn = a[j];
      } else {
        c++;
      }
    }
    cout << c << endl;
    ;
  }
}
