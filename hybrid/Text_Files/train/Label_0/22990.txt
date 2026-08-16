#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n, m, f = 0;
    cin >> n >> m;
    int a[302][302], b[302][302];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cin >> a[i][j];
      }
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        b[i][j] = 4;
      }
    }
    for (int i = 1; i < n - 1; i++) {
      b[i][0] = 3;
      b[i][m - 1] = 3;
    }
    for (int i = 1; i < m - 1; i++) {
      b[0][i] = 3;
      b[n - 1][i] = 3;
    }
    b[0][0] = 2;
    b[0][m - 1] = 2;
    b[n - 1][0] = 2;
    b[n - 1][m - 1] = 2;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (b[i][j] < a[i][j]) f = 1;
      }
    }
    if (f == 1) {
      cout << "NO" << endl;
    } else {
      cout << "YES" << endl;
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          cout << b[i][j] << " ";
        }
        cout << endl;
      }
    }
  }
}
