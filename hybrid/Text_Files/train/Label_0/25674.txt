#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n, m, h;
  cin >> n >> m >> h;
  int fro[m];
  for (int i = 0; i < m; i++) cin >> fro[i];
  int left[n];
  for (int i = 0; i < n; i++) cin >> left[i];
  int a[n][m], ans[n][m];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) cin >> a[i][j];
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (a[i][j] == 1) {
        ans[i][j] = min(fro[j], left[i]);
      } else
        ans[i][j] = 0;
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) cout << ans[i][j] << " ";
    cout << endl;
  }
  return 0;
}
