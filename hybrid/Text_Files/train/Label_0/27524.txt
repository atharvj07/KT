#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 5;
int n, sz[N], a[N], c, ret, dp[N];
pair<int, int> m[N][2];
vector<int> adj[N];
void dfs(int x, int p) {
  int f = 0, u, i, d;
  dp[x] = 0;
  if (!sz[x]) f = 1, ++sz[x];
  d = a[x] >= c ? 1 : 0;
  for (i = 0; i < adj[x].size(); ++i) {
    u = adj[x][i];
    if (u != p) {
      dfs(u, x);
      if (f) sz[x] += sz[u];
      if (dp[u] == sz[u])
        dp[x] += dp[u];
      else {
        if (m[x][0].first < dp[u])
          m[x][1] = m[x][0], m[x][0] = make_pair(dp[u], u);
        else if (m[x][1].first < dp[u])
          m[x][1] = make_pair(dp[u], u);
      }
    }
  }
  dp[x] += d + m[x][0].first;
  if (d == 0) dp[x] = 0;
  ret = max(ret, dp[x]);
}
void dfs2(int x, int p, int d) {
  int u, i, nd, t, v = 0;
  if (d == n - sz[x]) v = d, d = 0;
  ret = max(ret, (t = v + dp[x] - m[x][0].first + max(m[x][0].first, d)));
  for (i = 0; i < adj[x].size(); ++i) {
    u = adj[x][i];
    if (u != p) {
      nd = t;
      if (m[x][0].second == u)
        nd = dp[x] - m[x][0].first + max(m[x][1].first, d) + v;
      else if (dp[u] == sz[u])
        nd = t - sz[x];
      if (a[x] < c) nd = 0;
      dfs2(u, x, nd);
    }
  }
}
int main() {
  int i, x, y, q, l, r, k, mid;
  cin >> n >> k;
  for (i = 1; i <= n; ++i) scanf("%d", &a[i]);
  for (i = 0; i < n - 1; ++i)
    scanf("%d%d", &x, &y), adj[x].push_back(y), adj[y].push_back(x);
  dfs(1, 0);
  l = 1, r = 1e6;
  while (l < r) {
    mid = (l + r + 1) / 2;
    c = mid;
    memset(dp, 0, sizeof(dp));
    memset(m, 0, sizeof(m));
    ret = 0;
    dfs(1, 0);
    dfs2(1, 0, 0);
    if (ret >= k)
      l = mid;
    else
      r = mid - 1;
  }
  printf("%d\n", l);
}
