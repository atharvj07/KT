#include <bits/stdc++.h>
using namespace std;
int const N = 6e3 + 10;
int n, r[N];
vector<int> adj[N];
int lis[N];
int ans;
void dfs(int v, int par) {
  int idx = lower_bound(lis, lis + n, r[v]) - lis;
  ans = max(ans, idx + 1);
  int tmp = lis[idx];
  lis[idx] = r[v];
  for (int i = 0; i < adj[v].size(); i++) {
    int u = adj[v][i];
    if (u != par) dfs(u, v);
  }
  lis[idx] = tmp;
}
void solve() {
  for (int i = 0; i <= n; i++) lis[i] = (int)(1e9);
  for (int i = 1; i <= n; i++) dfs(i, -1);
  printf("%d\n", ans);
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d", &r[i]);
  for (int i = 0; i < n - 1; i++) {
    int u, v;
    scanf("%d %d", &u, &v);
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  solve();
  return 0;
}
