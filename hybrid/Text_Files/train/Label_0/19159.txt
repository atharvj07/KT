/**
 *    author:  tourist
 *    created: 15.12.2019 11:28:41       
**/
#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, tt;
  cin >> n >> tt;
  vector<vector<int>> can(n, vector<int>(2, 0));
  can[0][0] = 1;
  can[1][1] = 1;
  while (tt--) {
    int x, y;
    cin >> x >> y;
    --x; --y;
    swap(can[x], can[y]);
    for (int z : {x, y, x - 1, x + 1, y - 1, y + 1}) {
      if (z >= 0 && z < n && can[z][0]) {
        if (z - 1 >= 0) can[z - 1][1] = 1;
        if (z + 1 < n) can[z + 1][1] = 1;
      }
    }
  }
  int ans = 0;
  for (int i = 0; i < n; i++) {
    ans += can[i][0] | can[i][1];
  }
  cout << ans << '\n';
  return 0;
}
