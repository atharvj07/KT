#include <bits/stdc++.h>
using namespace std;
vector<int> g[300010], ans, rec;
set<pair<int, int>> edge;
int n, m, u, v;
int dis[300010], fa[300010], in[300010];
int cls[300010], vis[300010];
void dfs(int u) {
  rec.push_back(u);
  vis[u] = 1;
  for (int v : g[u])
    if (!vis[v]) dfs(v);
}
int main() {
  scanf("%d %d", &n, &m);
  for (int i = 1; i <= m; i++) {
    scanf("%d %d", &u, &v);
    g[u].push_back(v);
    g[v].push_back(u);
    edge.insert(make_pair(u, v));
    edge.insert(make_pair(v, u));
  }
  for (int i = 2; i <= n; i++) dis[i] = 1e9;
  queue<int> que;
  que.push(1);
  while (!que.empty()) {
    int u = que.front();
    que.pop();
    in[u] = 0;
    for (int v : g[u])
      if (dis[v] > dis[u] + 1) {
        dis[v] = dis[u] + 1;
        fa[v] = u;
        if (!in[v]) {
          in[v] = 1;
          que.push(v);
        }
      }
  }
  if (dis[n] != 1e9) {
    for (int u = n; u; u = fa[u]) ans.push_back(u);
    reverse(ans.begin(), ans.end());
  }
  if (ans.empty() || ans.size() > 4) {
    for (int u : g[1]) cls[u] = 1;
    cls[1] = 1;
    bool ok = false;
    for (int u : g[1]) {
      for (int v : g[u])
        if (!cls[v]) {
          ans = {1, u, v, 1, n};
          ok = true;
          break;
        }
      if (ok) break;
    }
  }
  if (ans.empty() || ans.size() > 5) {
    vis[1] = 1;
    bool ok = false;
    for (int u : g[1]) {
      if (vis[u]) continue;
      rec.clear();
      dfs(u);
      if (g[u].size() != rec.size()) {
        int cur = 1;
        while (cur < rec.size() && edge.count({u, rec[cur]})) cur++;
        for (int i = 1; i < cur; i++)
          if (edge.count({rec[i], rec[cur]})) {
            ans = {1, u, rec[i], rec[cur], u, n};
            ok = true;
          }
      } else {
        for (int i = 0; i < g[u].size(); i++) {
          for (int j = i + 1; j < g[u].size(); j++)
            if (g[u][i] != 1 && g[u][j] != 1 &&
                !edge.count({g[u][i], g[u][j]})) {
              ans = {1, g[u][i], u, g[u][j], g[u][i], n};
              ok = true;
              break;
            }
        }
        if (ok) break;
      }
      if (ok) break;
    }
  }
  if (ans.empty())
    puts("-1");
  else {
    printf("%d\n", (int)ans.size() - 1);
    for (int u : ans) printf("%d ", u);
    puts("");
  }
  return 0;
}
