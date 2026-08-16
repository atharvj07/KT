#include <bits/stdc++.h>
using namespace std;
struct E {
  long long node, cost, num;
};
const int N = 1e5 + 7;
vector<long long> adj[N], topo;
vector<E> edge[N];
long long vis[N], cycle, n, order[N];
void dfs(long long n) {
  vis[n] = 1;
  for (auto it : adj[n]) {
    if (!vis[it])
      dfs(it);
    else if (vis[it] == 1)
      cycle = 1;
  }
  vis[n] = 2;
  topo.push_back(n);
}
void can_do(long long mx) {
  cycle = 0;
  memset(vis, 0, sizeof vis);
  topo.clear();
  for (long long i = 0; i < n; i++) {
    adj[i].clear();
    for (auto it : edge[i]) {
      if (it.cost > mx) adj[i].push_back(it.node);
    }
  }
  for (long long i = 0; i < n; i++) {
    if (!vis[i]) dfs(i);
  }
}
int main() {
  long long m, i, j, u, v, c;
  cin >> n >> m;
  long long mx = 0;
  for (i = 0; i < m; i++) {
    cin >> u >> v >> c;
    u--, v--;
    edge[u].push_back({v, c, i});
    mx = max(mx, c);
  }
  long long low = 0, hi = mx;
  while (low < hi) {
    long long mid = (low + hi) / 2;
    can_do(mid);
    if (!cycle)
      hi = mid;
    else
      low = mid + 1;
  }
  can_do(low);
  for (i = 0; i < n; i++) order[topo[i]] = i;
  vector<long long> ans;
  for (i = 0; i < n; i++) {
    for (auto it : edge[i]) {
      if (order[i] < order[it.node]) ans.push_back(it.num);
    }
  }
  cout << low << ' ' << ans.size() << endl;
  for (auto it : ans) cout << it + 1 << ' ';
  return 0;
}
