#include <bits/stdc++.h>
using namespace std;
int n, m;
vector<int> adj[100005];
vector<int> radj[100005];
int par[100005];
vector<int> node[100005];
bool vis[100005];
vector<int> order;
int findParent(int a) {
  if (par[a] == a) return a;
  return par[a] = findParent(par[a]);
}
void merge(int a, int b) {
  a = findParent(a);
  b = findParent(b);
  par[b] = a;
}
void dfs(int u) {
  vis[u] = 1;
  for (int v : adj[u]) {
    if (!vis[v]) dfs(v);
  }
  order.push_back(u);
}
int rdfs(int u) {
  int cnt = 1;
  vis[u] = 0;
  for (int v : radj[u]) {
    if (vis[v]) cnt += rdfs(v);
  }
  return cnt;
}
int solve(int source) {
  order.clear();
  for (int u : node[source]) {
    if (!vis[u]) dfs(u);
  }
  reverse(order.begin(), order.end());
  for (int u : order) {
    int cnt = rdfs(u);
    if (cnt > 1) return node[source].size();
  }
  return node[source].size() - 1;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> m;
  iota(par, par + n + 1, 0);
  memset(vis, 0, sizeof(vis));
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    adj[u].push_back(v);
    radj[v].push_back(u);
    merge(u, v);
  }
  for (int i = 1; i <= n; i++) {
    node[findParent(i)].push_back(i);
  }
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    if (findParent(i) == i) ans += solve(i);
  }
  cout << ans << "\n";
  return 0;
}
