#include <bits/stdc++.h>
using namespace std;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int n, m;
int len;
int sum = 0;
int vis[20][20];
char ma[20][20];
int aimx, aimy, sx, sy;
struct point {
  int x, y;
};
struct snake {
  int x, y, dep;
  int ex, ey;
  point s[10];
};
int BFS(snake start) {
  queue<snake> q;
  vis[start.x][start.y]++;
  snake p, f;
  start.dep = 0;
  q.push(start);
  while (!q.empty()) {
    p = q.front();
    q.pop();
    sum++;
    if (sum > n * m * 100) return -1;
    vis[p.x][p.y]--;
    for (int i = 0; i < 4; i++) {
      f.x = p.x + dx[i];
      f.y = p.y + dy[i];
      if (f.x < 1 || f.y < 1 || f.x > n || f.y > m) continue;
      if (ma[f.x - 1][f.y - 1] == '#' || vis[f.x][f.y] >= 3) continue;
      f.s[1].x = f.x, f.s[1].y = f.y;
      for (int k = 1; k <= len - 1; k++) f.s[k + 1] = p.s[k];
      int ok = 0;
      for (int k = 2; k <= len; k++) {
        if (f.s[k].x == f.x && f.s[k].y == f.y) ok++;
      }
      if (ok) continue;
      vis[f.x][f.y]++;
      f.dep = p.dep + 1;
      if (f.x == aimx && f.y == aimy) return f.dep;
      q.push(f);
    }
  }
  return -1;
}
int main() {
  cin >> n >> m;
  memset(vis, 0, sizeof(vis));
  int maxn = 0, maxx, maxy;
  for (int i = 0; i < n; i++) scanf("%s", ma[i]);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      if (maxn < ma[i][j] - '0' && isdigit(ma[i][j]))
        maxn = ma[i][j] - '0', maxx = i, maxy = j;
  int ok = 0;
  len = 0;
  snake start;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      if (ma[i][j] == maxn + '0') start.s[maxn].x = i, start.s[maxn].y = j;
      if (ma[i][j] == '@')
        aimx = i + 1, aimy = j + 1;
      else if (ma[i][j] == '1')
        start.x = i + 1, start.y = j + 1, start.s[1].x = i + 1,
        start.s[1].y = j + 1;
      else if (isdigit(ma[i][j]))
        start.s[ma[i][j] - '0'].x = i + 1, start.s[ma[i][j] - '0'].y = j + 1;
    }
  len = maxn;
  int ans = BFS(start);
  cout << ans << endl;
  return 0;
}
