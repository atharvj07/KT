#include <bits/stdc++.h>
using namespace std;
const int maxn = 1005;
vector<int> side[maxn];
bool flag = 0;
int mark[maxn], vis[maxn], bl[maxn];
void check(int u, int bk) {
  bl[u] = bk;
  for (int i = 0; i < side[u].size(); i++) {
    int v = side[u][i];
    if (!vis[v]) {
      vis[v] = 1;
      mark[v] = mark[u] ^ 1;
      check(v, bk);
    } else {
      if (mark[v] != (mark[u] ^ 1)) flag = 1;
    }
  }
}
int dis[maxn][maxn];
queue<int> q;
int ans[maxn];
int main() {
  ios::sync_with_stdio(0);
  int n, m;
  cin >> n >> m;
  for (int i = (1), iend = (m); i <= iend; i++) {
    int u, v;
    cin >> u >> v;
    side[u].push_back(v);
    side[v].push_back(u);
  }
  for (int i = (1), iend = (n); i <= iend; i++)
    if (!vis[i]) {
      vis[i] = 1;
      check(i, i);
    }
  if (flag) {
    cout << "-1";
    return 0;
  }
  for (int i = (1), iend = (n); i <= iend; i++) {
    memset(vis, 0, sizeof(vis));
    while (!q.empty()) q.pop();
    vis[i] = 1;
    q.push(i);
    while (!q.empty()) {
      int u = q.front();
      q.pop();
      for (int j = 0; j < side[u].size(); j++) {
        int v = side[u][j];
        if (vis[v]) continue;
        dis[i][v] = dis[i][u] + 1;
        vis[v] = 1;
        q.push(v);
      }
    }
  }
  for (int i = (1), iend = (n); i <= iend; i++)
    for (int j = (1), jend = (n); j <= jend; j++)
      if (bl[i] == bl[j]) ans[bl[i]] = max(ans[bl[i]], dis[i][j]);
  int mx = 0;
  for (int i = (1), iend = (n); i <= iend; i++) mx += ans[i];
  cout << mx;
  return 0;
}
