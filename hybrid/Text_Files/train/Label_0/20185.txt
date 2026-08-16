#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
  int t = 1;
  cin >> t;
  while (t--) {
    int n, m, a, b;
    cin >> n >> m >> a >> b;
    if (n * a != m * b) {
      cout << "NO" << endl;
      continue;
    }
    vector<vector<int> > res(n, vector<int>(m, 0));
    int d = 0;
    for (int i = (1); i <= (m - 1); i++) {
      if (d * n % m == 0) {
        break;
      }
    }
    for (int i = 0; i < n; i++) {
      for (int k = (0); k <= (b - 1); k++) {
        for (int j = (0); j <= (a - 1); j++) {
          res[i][(j + i * (a)) % m] = 1;
        }
      }
    }
    cout << "YES" << endl;
    for (int i = (0); i <= (n - 1); i++) {
      for (int j = (0); j <= (m - 1); j++) {
        cout << res[i][j];
      }
      cout << endl;
    }
  }
}
