#include <bits/stdc++.h>
using namespace std;
int solveA() {
  int n, m;
  cin >> n >> m;
  vector<bool> mm(m);
  vector<vector<bool> > tbl(n, mm);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      int v;
      cin >> v;
      tbl[i][j] = v != 0;
    }
  }
  bool corner = false;
  if (tbl[0][0] || tbl[0][m - 1] || tbl[n - 1][0] || tbl[n - 1][m - 1])
    corner = true;
  if (corner) {
    cout << 1 << endl;
    return 0;
  }
  bool side = false;
  for (int i = 0; i < m; i++) {
    if (tbl[0][i] || tbl[n - 1][i]) side = true;
  }
  if (!side) {
    for (int i = 0; i < n; i++) {
      if (tbl[i][0] || tbl[i][m - 1]) side = true;
    }
  }
  if (side) {
    cout << 2 << endl;
    return 0;
  }
  cout << 4 << endl;
  return 0;
}
int main() { return solveA(); }
