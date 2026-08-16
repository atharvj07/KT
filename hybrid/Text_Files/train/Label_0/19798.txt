#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  vector<int> cntpos(m);
  vector<string> row(n);
  for (int i = 0; i < n; ++i) {
    cin >> row[i];
    for (int j = 0; j < m; ++j) {
      cntpos[j] += (row[i][j] == '1');
    }
  }
  bool sol = false;
  for (int i = 0; i < n; ++i) {
    bool flag = true;
    for (int j = 0; j < m; ++j) {
      if (row[i][j] == '0') continue;
      if (cntpos[j] == 1) {
        flag = false;
        break;
      }
    }
    sol |= flag;
    if (sol) break;
  }
  if (sol)
    cout << "YES\n";
  else
    cout << "NO\n";
  return 0;
}
