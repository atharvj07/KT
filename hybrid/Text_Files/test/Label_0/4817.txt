#include <bits/stdc++.h>
using namespace std;
int n, m;
char g[2005][2005];
bool check(int x, int y) {
  if (g[x][y] == '.' || x < 0 || y < 0 || x >= n || y >= m) return 0;
  if (g[x][y - 1] == '.' && g[x - 1][y - 1] == '.' && g[x - 1][y] == '.')
    return 1;
  if (g[x - 1][y] == '.' && g[x - 1][y + 1] == '.' && g[x][y + 1] == '.')
    return 1;
  if (g[x][y + 1] == '.' && g[x + 1][y + 1] == '.' && g[x + 1][y] == '.')
    return 1;
  if (g[x][y - 1] == '.' && g[x + 1][y - 1] == '.' && g[x + 1][y] == '.')
    return 1;
  return 0;
}
int main() {
  while (~scanf("%d%d", &n, &m)) {
    for (int i = 0; i < n; i++) scanf("%s", g[i]);
    queue<pair<int, int> > q;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
        if (check(i, j)) q.push(pair<int, int>(i, j));
    while (!q.empty()) {
      pair<int, int> u = q.front();
      q.pop();
      int i = u.first, j = u.second;
      if (!check(i, j)) continue;
      g[i][j] = '.';
      for (int x = -2; x <= 2; x++)
        for (int y = -2; y <= 2; y++)
          if ((x || y) && check(i + x, j + y))
            q.push(pair<int, int>(i + x, j + y));
    }
    for (int i = 0; i < n; i++) puts(g[i]);
  }
  return 0;
}
