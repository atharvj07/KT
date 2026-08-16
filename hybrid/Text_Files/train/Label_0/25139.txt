#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  for (int TST_CASE = 1; TST_CASE <= N; TST_CASE++) {
    int n, m;
    cin >> n >> m;
    int a[n][m];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++) cin >> a[i][j];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (i % 2 == 0) {
          if (j % 2 == 0) {
            if (a[i][j] % 2 == 1) a[i][j]++;
          } else {
            if (a[i][j] % 2 == 0) a[i][j]++;
          }
        } else {
          if (j % 2 == 1) {
            if (a[i][j] % 2 == 1) a[i][j]++;
          } else {
            if (a[i][j] % 2 == 0) a[i][j]++;
          }
        }
      }
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cout << a[i][j] << " ";
      }
      cout << "\n";
    }
  }
}
