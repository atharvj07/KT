#include <bits/stdc++.h>
using namespace std;
struct node {
  long long u, v, w;
} edge[200005];
long long n, m;
vector<pair<long long, long long> > G[200005];
long long dep[200005], fa[200005], val[200005];
long long f[200005][21];
void makeSet() {
  for (long long i = 1; i <= n; i++) fa[i] = i;
}
long long find(long long x) { return (x == fa[x]) ? x : fa[x] = find(fa[x]); }
void dfs(long long u, long long Fa) {
  dep[u] = dep[Fa] + 1;
  for (long long i = 1; i <= 20; i++) f[u][i] = f[f[u][i - 1]][i - 1];
  for (long long i = 0; i < G[u].size(); i++) {
    long long v = G[u][i].first;
    if (v == Fa) continue;
    f[v][0] = u;
    if (G[u][i].second == 1) fa[v] = find(u);
    val[v] = G[u][i].second;
    dfs(v, u);
  }
}
long long lca(long long u, long long v) {
  if (dep[u] < dep[v]) swap(u, v);
  for (long long i = 20; ~i; i--)
    if (dep[f[u][i]] >= dep[v]) u = f[u][i];
  if (u == v) return u;
  for (long long i = 20; ~i; i--)
    if (f[u][i] != f[v][i]) u = f[u][i], v = f[v][i];
  return f[u][0];
}
signed main() {
  scanf("%lld %lld", &n, &m);
  for (long long i = 1; i < n; i++) {
    scanf("%lld %lld %lld", &edge[i].u, &edge[i].v, &edge[i].w);
    G[edge[i].u].push_back(make_pair(edge[i].v, edge[i].w));
    G[edge[i].v].push_back(make_pair(edge[i].u, edge[i].w));
  }
  makeSet();
  dfs(1, 0);
  while (m--) {
    long long opt, x, y, z;
    scanf("%lld %lld %lld", &opt, &x, &y);
    if (opt & 1) {
      scanf("%lld", &z);
      long long p = lca(x, y);
      while (dep[x] > dep[p] && z) {
        if (val[x]) z /= val[x];
        x = find(f[x][0]);
      }
      while (dep[y] > dep[p] && z) {
        if (val[y]) z /= val[y];
        y = find(f[y][0]);
      }
      printf("%lld\n", z);
    } else {
      long long u = edge[x].u, v = edge[x].v;
      if (f[u][0] == v)
        z = u;
      else
        z = v;
      val[z] = y;
      if (val[z] == 1) fa[z] = find(f[z][0]);
    }
  }
  return 0;
}
