#include <bits/stdc++.h>
using namespace std;
vector<vector<pair<int, long long> > > g;
int n, a[100005];
bool erased[100005];
void dfs(int cur, long long cost, long long minCost) {
  if (cost - minCost > 1ll * a[cur]) {
    erased[cur] = 1;
    return;
  }
  for (int i = 0; i < g[cur].size(); i++) {
    dfs(g[cur][i].first, cost + g[cur][i].second, min(minCost, cost));
  }
}
int count(int u) {
  if (erased[u]) return 0;
  int ans = 1;
  for (int i = 0; i < g[u].size(); i++) ans += count(g[u][i].first);
  return ans;
}
int main() {
  scanf("%d", &n);
  g.assign(n, vector<pair<int, long long> >());
  for (int i = 0; i < n; i++) scanf("%d", &a[i]);
  for (int i = 1; i < n; i++) {
    int v, c;
    scanf("%d %d", &v, &c);
    v--;
    g[v].push_back(pair<int, long long>(i, c));
  }
  memset(erased, 0, sizeof erased);
  dfs(0, 0ll, 0ll);
  printf("%d\n", n - count(0));
}
