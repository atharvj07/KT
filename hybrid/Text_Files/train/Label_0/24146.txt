#include <bits/stdc++.h>
using namespace std;
int n, m, a[205 << 1][205 << 1];
queue<pair<int, int> > q;
int main() {
  cin >> n >> m;
  a[205][205] = n;
  if (n >> 2) q.push(make_pair(205, 205));
  int dx[] = {0, 1, 0, -1};
  int dy[] = {1, 0, -1, 0};
  while (!q.empty()) {
    pair<int, int> p = q.front();
    q.pop();
    for (int i = 0; i < 4; i++) {
      int x = p.first + dx[i];
      int y = p.second + dy[i];
      a[x][y] += a[p.first][p.second] >> 2;
      if ((a[x][y] >> 2) && !((a[x][y] - (a[p.first][p.second] >> 2)) >> 2))
        q.push(make_pair(x, y));
    }
    a[p.first][p.second] %= 4;
  }
  while (m--) {
    int x, y;
    cin >> x >> y;
    if (x < -205 || x >= 205 || y < -205 || y >= 205)
      cout << 0 << "\n";
    else
      cout << a[x + 205][y + 205] << "\n";
  }
}
