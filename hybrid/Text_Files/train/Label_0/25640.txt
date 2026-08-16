#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  int a[n][m], b[n][m];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> a[i][j];
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> b[i][j];
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (a[i][j] > b[i][j]) {
        swap(a[i][j], b[i][j]);
      }
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (i == 0) {
        if (j != 0) {
          if (a[i][j] <= a[i][j - 1] || b[i][j] <= b[i][j - 1]) {
            cout << "Impossible";
            return 0;
          }
        }
      } else {
        if (j == 0) {
          if (a[i][j] <= a[i - 1][j] || b[i][j] <= b[i - 1][j]) {
            cout << "Impossible";
            return 0;
          }
        } else {
          if (a[i][j] <= a[i - 1][j] || b[i][j] <= b[i - 1][j] ||
              a[i][j] <= a[i][j - 1] || b[i][j] <= b[i][j - 1]) {
            cout << "Impossible";
            return 0;
          }
        }
      }
    }
  }
  cout << "Possible";
  return 0;
}
