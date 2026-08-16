#include <bits/stdc++.h>
using namespace std;
int g[2][10][10];
bool ans[2][10][10];
int main() {
  int n, m, i, j, x, y, tot = 0;
  cin >> n >> m;
  for (i = 1; i <= (n); i++) cin >> x >> y, g[0][x][y] = g[0][y][x] = 1;
  for (i = 1; i <= (m); i++) cin >> x >> y, g[1][x][y] = g[1][y][x] = 1;
  for (i = 1; i <= (9); i++)
    for (j = 1; j <= (9); j++)
      if (i != j)
        for (y = 1; y <= (9); y++)
          if (y != i && y != j && g[0][i][j] && g[0][i][j] == g[1][i][y]) {
            x = i;
            ans[0][i][j] = 1;
            ans[1][i][y] = 1;
          }
  for (i = 1; i <= (9); i++)
    for (j = 1; j <= (9); j++)
      if (ans[0][i][j]) {
        tot++;
        break;
      }
  if (tot == 1) cout << x, exit(0);
  for (i = 1; i <= (9); i++)
    for (j = 1; j <= (9); j++)
      if (i != j &&
          (ans[0][i][j] && ans[0][j][i] || ans[1][i][j] && ans[1][j][i]))
        cout << -1, exit(0);
  cout << 0;
  return 0;
}
