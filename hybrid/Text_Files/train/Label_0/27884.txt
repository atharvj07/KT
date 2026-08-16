#include <bits/stdc++.h>
using namespace std;
const int inf = 1e9;
const int MAX = 5e5 + 10;
int dist[MAX], mark[MAX][2];
int ans[MAX];
int n, m;
vector<vector<pair<int, int> > > adj(MAX), adj2(MAX);
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < m; ++i) {
    int x, y, z;
    cin >> x >> y >> z;
    adj[x].push_back({y, z});
    adj2[y].push_back({x, z});
  }
  queue<int> q;
  q.push(n);
  dist[1] = -1;
  dist[n] = 0;
  mark[n][0] = mark[n][1] = 1;
  while (!q.empty()) {
    int node = q.front();
    q.pop();
    for (auto &child : adj2[node]) {
      int to = child.first, c = child.second;
      if (mark[to][c]) continue;
      mark[to][c] = 1;
      if (mark[to][c] && mark[to][!c]) {
        ans[to] = c;
        q.push(to);
        dist[to] = dist[node] + 1;
      }
    }
  }
  if (dist[1] == -1) {
    cout << -1 << "\n";
    for (int i = 1; i <= n; ++i) {
      if (!mark[i][0])
        cout << 0;
      else
        cout << 1;
    }
  } else {
    cout << dist[1] << "\n";
    for (int i = 1; i <= n; ++i) {
      if (!mark[i][1])
        cout << 1;
      else if (!mark[i][0])
        cout << 0;
      else
        cout << ans[i];
    }
  }
  return 0;
}
