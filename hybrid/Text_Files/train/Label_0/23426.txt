#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long i, j, m, n, k;
  long long t;
  cin >> t;
  while (t--) {
    cin >> n;
    char a[n][n];
    for (i = 0; i < n; i++) {
      for (j = 0; j < n; j++) {
        cin >> a[i][j];
      }
    }
    if (a[0][1] == a[1][0] && a[n - 1][n - 2] == a[n - 2][n - 1]) {
      if (a[0][1] != a[n - 1][n - 2]) {
        cout << 0 << "\n";
      } else {
        cout << 2 << "\n";
        cout << 1 << " " << 2 << "\n";
        cout << 2 << " " << 1 << "\n";
      }
    } else if (a[0][1] == a[1][0] && a[n - 1][n - 2] != a[n - 2][n - 1]) {
      cout << 1 << "\n";
      if (a[0][1] == a[n - 1][n - 2]) {
        cout << n << " " << n - 1 << "\n";
      } else
        cout << n - 1 << " " << n << "\n";
    } else if (a[0][1] != a[1][0] && a[n - 1][n - 2] == a[n - 2][n - 1]) {
      cout << 1 << "\n";
      if (a[0][1] == a[n - 1][n - 2]) {
        cout << 1 << " " << 2 << "\n";
      } else
        cout << 2 << " " << 1 << "\n";
    } else {
      cout << 2 << "\n";
      if (a[0][1] == a[n - 1][n - 2]) {
        cout << 1 << " " << 2 << "\n";
        cout << n - 1 << " " << n << "\n";
      } else {
        cout << 1 << " " << 2 << "\n";
        cout << n << " " << n - 1 << "\n";
      }
    }
  }
}
