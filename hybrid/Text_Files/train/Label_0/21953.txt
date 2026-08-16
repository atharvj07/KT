#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 7;
const int LG = 20;
const int MOD = 1e9 + 7;
int dp[N][2], up[N][2], cnt[N];
vector<pair<int, int> > adj[N];
int d[N], par[N][LG], path[N][LG];
int n;
void add(int &a, long long val) {
  a += val % MOD;
  a %= MOD;
  a += MOD;
  a %= MOD;
}
void dfs_down(int v, int p) {
  cnt[v]++;
  for (auto e : adj[v]) {
    int u = e.first;
    int w = e.second;
    if (u == p) continue;
    d[u] = d[v] + 1;
    par[u][0] = v;
    path[u][0] = w;
    for (int i = 1; i < LG; i++) {
      par[u][i] = par[par[u][i - 1]][i - 1];
      path[u][i] = (path[u][i - 1] + path[par[u][i - 1]][i - 1]) % MOD;
    }
    dfs_down(u, v);
    cnt[v] += cnt[u];
    add(dp[v][0], 1LL * dp[u][0] + 1LL * cnt[u] * w % MOD);
    add(dp[v][1], 1LL * dp[u][1] + 2LL * dp[u][0] * w % MOD +
                      1LL * cnt[u] * w % MOD * w % MOD);
  }
}
void dfs_up(int v, int p) {
  for (auto e : adj[v]) {
    int u = e.first;
    int w = e.second;
    if (u == p) continue;
    int sum = dp[v][0];
    add(sum, -1LL * dp[u][0] + -1LL * cnt[u] * w % MOD);
    int sum2 = dp[v][1];
    add(sum2, -1LL * dp[u][1] + -2LL * dp[u][0] * w % MOD +
                  -1LL * cnt[u] * w % MOD * w % MOD);
    add(up[u][0], 1LL * (sum + up[v][0]) % MOD + 1LL * (n - cnt[u]) * w % MOD);
    add(up[u][1], 1LL * (sum2 + up[v][1]) % MOD +
                      2LL * (sum + up[v][0]) % MOD * w % MOD +
                      1LL * (n - cnt[u]) * w % MOD * w % MOD);
    dfs_up(u, v);
  }
}
pair<int, int> get_parent(int v, int a) {
  int ans = 0;
  for (int i = 0; i < LG; i++)
    if ((a >> i) & 1) {
      ans += path[v][i], ans %= MOD;
      v = par[v][i];
    }
  return {v, ans};
}
int lca(int v, int u) {
  if (d[u] > d[v]) swap(u, v);
  v = get_parent(v, d[v] - d[u]).first;
  if (v == u) return v;
  for (int i = LG - 1; i >= 0; i--)
    if (par[v][i] != par[u][i]) v = par[v][i], u = par[u][i];
  return par[u][0];
}
int main() {
  ios::sync_with_stdio(false);
  cin >> n;
  for (int i = 1; i < n; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    u--, v--;
    adj[v].push_back({u, w});
    adj[u].push_back({v, w});
  }
  dfs_down(0, -1);
  dfs_up(0, -1);
  int q;
  cin >> q;
  while (q--) {
    int u, v;
    cin >> u >> v;
    u--, v--;
    int w = lca(u, v);
    int dis = (get_parent(v, d[v] - d[w]).second +
               get_parent(u, d[u] - d[w]).second) %
              MOD;
    int ans = 0;
    if (w == v)
      add(ans, 1LL * dp[u][1] + 1LL * up[u][1] +
                   -2LL *
                       (1LL * up[v][1] + 2LL * up[v][0] * dis % MOD +
                        1LL * (n - cnt[v]) * dis % MOD * dis % MOD) %
                       MOD);
    else
      add(ans, -1LL * dp[u][1] + -1LL * up[u][1] +
                   2LL *
                       (1LL * dp[v][1] + 2LL * dp[v][0] * dis % MOD +
                        1LL * cnt[v] * dis % MOD * dis % MOD) %
                       MOD);
    cout << ans << "\n";
  }
  return 0;
}
