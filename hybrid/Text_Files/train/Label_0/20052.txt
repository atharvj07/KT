#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e3 + 10, inf = 1e8;
int n, m, dp[4][maxn][maxn], mark[maxn][maxn], color = 0, dis[5][5];
vector<pair<int, int> > ve[4];
char mat[maxn][maxn];
queue<pair<int, int> > qu;
pair<int, int> mov[] = {pair<int, int>(0, 1), pair<int, int>(0, -1),
                        pair<int, int>(1, 0), pair<int, int>(-1, 0)};
bool pos(int a, int b) {
  if (min(a, b) < 0 || a >= n || b >= m || mat[a][b] == '#') return 0;
  return 1;
}
void dfs(int a, int b) {
  mark[a][b] = color;
  dp[color][a][b] = 0;
  ve[color].push_back(pair<int, int>(a, b));
  for (int i = 0; i < 4; i++) {
    int ap = a + mov[i].first, bp = b + mov[i].second;
    if (pos(ap, bp) and mat[ap][bp] != '.' and !mark[ap][bp]) dfs(ap, bp);
  }
}
void bfs(int C) {
  for (int i = 0; i < (int)ve[C].size(); i++) qu.push(ve[C][i]);
  while (!qu.empty()) {
    pair<int, int> id = qu.front();
    qu.pop();
    int a = id.first, b = id.second;
    for (int i = 0; i < 4; i++) {
      int ap = a + mov[i].first, bp = b + mov[i].second;
      if (pos(ap, bp) and dp[C][ap][bp] > dp[C][a][b] + 1) {
        dp[C][ap][bp] = dp[C][a][b] + 1;
        qu.push(pair<int, int>(ap, bp));
        if (mark[ap][bp] != 0) {
          int colorp = mark[ap][bp];
          dis[colorp][color] = min(dis[colorp][color], dp[C][ap][bp]);
          dp[C][ap][bp] = dis[colorp][color];
        }
      }
    }
  }
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      cin >> mat[i][j];
      for (int k = 0; k < 4; k++) {
        dp[k][i][j] = inf;
        for (int l = 0; l < 4; l++) dis[k][l] = inf;
      }
    }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (mat[i][j] != '.' and mat[i][j] != '#' and !mark[i][j]) {
        color++;
        dfs(i, j);
      }
    }
  }
  int t = color;
  for (int i = 1; i <= t; i++) {
    color = i;
    bfs(i);
  }
  if (t == 1) {
    cout << "0\n";
    return 0;
  }
  int ans = inf;
  if (t == 2) {
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++) ans = min(ans, dp[1][i][j] + dp[2][i][j] - 1);
    cout << (ans >= inf - 10 ? -1 : ans) << '\n';
    return 0;
  }
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      ans = min(ans, dp[1][i][j] + dp[2][i][j] + dp[3][i][j] - 2);
  cout << (ans >= inf ? -1 : ans) << endl;
  return 0;
}
