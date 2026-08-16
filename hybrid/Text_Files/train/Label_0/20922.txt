#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 4;
const int maxlog = 22;
const int mod = 1e9 + 7;
const int sq = 350;
int n, m, st[maxn], co, h[maxn];
vector<pair<int, int> > ans;
vector<int> edge[maxn];
bool mark[maxn];
void dfs(int v, int par) {
  mark[v] = true;
  st[v] = co++;
  h[v] = st[v];
  for (int i = 0; i < edge[v].size(); i++) {
    int u = edge[v][i];
    if (u == par) continue;
    if (!mark[u] || st[u] < st[v]) ans.push_back(make_pair(v, u));
    if (!mark[u]) dfs(u, v);
    h[v] = min(h[v], st[u]);
    if (st[u] > st[v]) {
      h[v] = min(h[v], h[u]);
      if (h[u] == st[u]) {
        cout << 0;
        exit(0);
      }
    }
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cout.precision(20);
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    edge[u].push_back(v), edge[v].push_back(u);
  }
  dfs(1, 0);
  for (int i = 0; i < m; i++)
    cout << ans[i].first << " " << ans[i].second << endl;
  return 0;
}
