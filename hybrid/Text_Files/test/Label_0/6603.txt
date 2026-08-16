#include <bits/stdc++.h>
using namespace std;
const int dx[4] = {1, 0, 0, -1}, dy[4] = {0, -1, 1, 0};
int n, m, k, sti, stj, d[1001][1001];
string s[1001], add = "DLRU";
bool valid(int x, int y) {
  return (x >= 0 && x < n && y >= 0 && y < m && s[x][y] != '*');
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n >> m >> k;
  if (k & 1) cout << "IMPOSSIBLE", exit(0);
  for (int i = 0; i < n; i++) {
    cin >> s[i];
    for (int j = 0; j < m; j++) {
      if (s[i][j] == 'X') sti = i, stj = j;
      d[i][j] = INT_MAX;
    }
  }
  queue<pair<int, int> > q;
  q.emplace(sti, stj);
  d[sti][stj] = 0;
  while (!q.empty()) {
    int x = q.front().first, y = q.front().second;
    q.pop();
    for (int i = 0; i < 4; i++) {
      int xx = x + dx[i], yy = y + dy[i];
      if (valid(xx, yy) && d[xx][yy] > d[x][y] + 1)
        q.emplace(xx, yy), d[xx][yy] = d[x][y] + 1;
    }
  }
  string res = "";
  for (int i = 0, x = sti, y = stj; i < k; i++) {
    int dir = 0;
    while (dir < 4) {
      int xx = x + dx[dir], yy = y + dy[dir];
      if (valid(xx, yy) && d[xx][yy] <= k - i - 1) break;
      dir++;
    }
    if (dir == 4) cout << "IMPOSSIBLE", exit(0);
    x += dx[dir];
    y += dy[dir];
    res += add[dir];
  }
  cout << res;
}
