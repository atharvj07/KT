#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m, dl = 100, dc = 100, fl = -1, fc = -1;
  char t[50][50];
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> t[i][j];
      if ((t[i][j] == '*') && (i < dl)) {
        dl = i;
      }
      if ((t[i][j] == '*') && (j < dc)) {
        dc = j;
      }
      if ((t[i][j] == '*') && (i > fl)) {
        fl = i;
      }
      if ((t[i][j] == '*') && (j > fc)) {
        fc = j;
      }
    }
  }
  for (int i = dl; i <= fl; i++) {
    for (int j = dc; j <= fc; j++) cout << t[i][j];
    cout << endl;
  }
  return 0;
}
