#include <bits/stdc++.h>
using namespace std;
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int n, m, vis[101][101], cnt;
string s[101];
int dfs(int x, int y) {
  if (x < 0 || x >= n || y < 0 || y >= m || vis[x][y] || s[x][y] == '.')
    return 0;
  vis[x][y] = 1;
  for (int i = 0; i < 4; i++) dfs(x + dx[i], y + dy[i]);
  return 1;
}
void code() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) cin >> s[i];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (s[i][j] == '.') continue;
      cnt++;
      memset(vis, 0, sizeof(vis));
      int tmp = 0;
      s[i][j] = '.';
      for (int k = 0; k < 4; k++) tmp += dfs(i + dx[k], j + dy[k]);
      if (tmp > 1) {
        cout << 1 << '\n';
        return;
      }
      s[i][j] = '#';
    }
  }
  cout << ((cnt < 3) ? -1 : 2) << '\n';
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t = 1;
  while (t--) {
    code();
  }
}
