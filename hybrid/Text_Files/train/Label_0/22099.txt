#include <bits/stdc++.h>
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int Ans[1000010];
char A[1010][1010];
int vis[1000][1000];
int n, m, q;
int cnt;
int mark = 1;
using namespace std;
int valid(int x, int y) {
  if (x >= n || x < 0 || y >= m || y < 0 || A[x][y] == '.') {
    return 0;
  }
  return 1;
}
void dfs(int x, int y) {
  if (x >= n || x < 0 || y >= m || y < 0 || A[x][y] == '*' || vis[x][y]) return;
  vis[x][y] = mark;
  for (int i = 0; i < 4; i++) {
    if (valid(x + dx[i], y + dy[i])) cnt++;
    dfs(x + dx[i], y + dy[i]);
  }
}
int main() {
  cin >> n >> m >> q;
  for (int i = 0; i < n; i++) {
    cin >> A[i];
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (A[i][j] == '.' && !vis[i][j]) {
        dfs(i, j);
        Ans[mark] = cnt;
        cnt = 0;
        mark++;
      }
    }
  }
  while (q--) {
    int x, y;
    cin >> x >> y;
    cout << Ans[vis[x - 1][y - 1]] << endl;
  }
  return 0;
}
