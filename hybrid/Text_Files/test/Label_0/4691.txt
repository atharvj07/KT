#include <bits/stdc++.h>
using namespace std;
template <typename T>
bool MinPlace(T &a, const T &b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}
template <typename T>
bool MaxPlace(T &a, const T &b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}
int dr[8] = {0, -1, -1, -1, 0, 1, 1, 1};
int dc[8] = {1, 1, 0, -1, -1, -1, 0, 1};
vector<pair<int, int> > centers;
bool check(int x, vector<vector<int> > &cnt, vector<string> &grid, int n, int m,
           int store = 0) {
  int dist[n + 1][m + 1];
  bool visited[n + 1][m + 1];
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      dist[i][j] = (long long)1e9;
      visited[i][j] = false;
    }
  }
  queue<pair<int, int> > q;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      int cost = (i + x <= n && i - x >= 1 && j + x <= m && j - x >= 1)
                     ? (cnt[i + x][j + x] - cnt[i + x][j - x - 1] -
                        cnt[i - x - 1][j + x] + cnt[i - x - 1][j - x - 1])
                     : 0;
      if (cost == (2 * x + 1) * (2 * x + 1)) {
        dist[i][j] = 0;
        q.push({i, j});
        visited[i][j] = true;
      }
    }
  }
  if (store == 1) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        if (visited[i][j])
          cout << 'X';
        else
          cout << '.';
      }
      cout << "\n";
    }
    return 0;
  }
  while (!q.empty()) {
    auto t = q.front();
    q.pop();
    int cost = dist[t.first][t.second];
    for (int j = 0; j < 8; j++) {
      int r1 = t.first + dr[j];
      int c1 = t.second + dc[j];
      if (r1 >= 1 && r1 <= n && c1 >= 1 && c1 <= m && !visited[r1][c1]) {
        dist[r1][c1] = 1 + cost;
        visited[r1][c1] = true;
        q.push({r1, c1});
      }
    }
  }
  int flag = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      if (grid[i][j] == 'X' && dist[i][j] > x) {
        flag = 1;
        break;
      }
    }
  }
  return (flag == 0);
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  int n, m;
  cin >> n >> m;
  vector<string> grid(n + 1);
  vector<vector<int> > cnt(n + 1, vector<int>(m + 1, 0));
  for (int i = 1; i <= n; i++) {
    string str;
    cin >> str;
    string str2 = "$" + str;
    grid[i] = str2;
  }
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      cnt[i][j] = cnt[i - 1][j] + cnt[i][j - 1] - cnt[i - 1][j - 1] +
                  (grid[i][j] == 'X');
    }
  }
  int low = 0;
  int high = max(n, m);
  int mid;
  while (high >= low) {
    mid = low + (high - low) / 2;
    if (check(mid, cnt, grid, n, m))
      low = mid + 1;
    else
      high = mid - 1;
  }
  cout << high << endl;
  check(high, cnt, grid, n, m, 1);
}
