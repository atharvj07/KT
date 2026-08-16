#include <bits/stdc++.h>
using namespace std;
const int N = 300000 + 7;
int n, q;
long long val[N];
struct edge {
  int to, nex;
  long long wei;
} e[N << 1];
int fir[N], eid;
int siz[N], dep[N], fa[N], son[N], ltp[N];
long long faw[N];
int dfn[N], inx;
long long f[N], g[N];
long long bit[N];
void addedge(int u, int v, int w);
void dfs1(int s);
void dfs2(int s);
void dfs3(int s, long long up);
void build();
int lca(int x, int y);
long long get(int x, int z);
void add(int i, long long v);
long long sum(int i);
int main() {
  scanf("%d%d", &n, &q);
  for (int i = 1; i <= n; ++i) scanf("%lld", val + i);
  for (int i = 1, u, v, w; i < n; ++i)
    scanf("%d%d%d", &u, &v, &w), addedge(u, v, w), addedge(v, u, w);
  dfs1(1);
  ltp[1] = 1;
  dfs2(1);
  dfs3(1, 0);
  build();
  for (int x, y, z; q; --q) {
    scanf("%d%d", &x, &y);
    if (x == y)
      printf("%lld\n", g[x]);
    else
      z = lca(x, y), printf("%lld\n", g[z] + get(x, z) + get(y, z));
  }
  return 0;
}
void addedge(int u, int v, int w) {
  e[++eid] = (edge){v, fir[u], 1ll * w};
  fir[u] = eid;
}
void dfs1(int s) {
  siz[s] = 1;
  f[s] = val[s];
  for (int i = fir[s]; i; i = e[i].nex) {
    if (e[i].to == fa[s]) continue;
    fa[e[i].to] = s;
    faw[e[i].to] = e[i].wei;
    dep[e[i].to] = dep[s] + 1;
    dfs1(e[i].to);
    siz[s] += siz[e[i].to];
    son[s] = siz[e[i].to] > siz[son[s]] ? e[i].to : son[s];
    f[s] += max(0ll, f[e[i].to] - 2 * e[i].wei);
  }
}
void dfs2(int s) {
  dfn[s] = ++inx;
  if (!son[s]) return;
  ltp[son[s]] = ltp[s];
  dfs2(son[s]);
  for (int i = fir[s]; i; i = e[i].nex)
    if (e[i].to != fa[s] && e[i].to != son[s])
      ltp[e[i].to] = e[i].to, dfs2(e[i].to);
}
void dfs3(int s, long long up) {
  g[s] = f[s] + max(0ll, up);
  for (int i = fir[s]; i; i = e[i].nex)
    if (e[i].to != fa[s])
      dfs3(e[i].to, g[s] - max(0ll, f[e[i].to] - 2 * e[i].wei) - 2 * e[i].wei);
}
void build() {
  for (int i = 1; i <= n; ++i)
    add(dfn[i], f[i] - max(0ll, f[i] - 2 * faw[i]) - faw[i]);
}
int lca(int x, int y) {
  for (; ltp[x] != ltp[y]; x = fa[ltp[x]])
    if (dep[ltp[x]] < dep[ltp[y]]) swap(x, y);
  return dep[x] < dep[y] ? x : y;
}
long long get(int x, int z) {
  long long t = 0;
  for (; ltp[x] != ltp[z]; x = fa[ltp[x]])
    t += sum(dfn[x]) - sum(dfn[ltp[x]] - 1);
  return t + sum(dfn[x]) - sum(dfn[z]);
}
void add(int i, long long v) {
  for (; i <= n; i += i & -i) bit[i] += v;
}
long long sum(int i) {
  long long t = 0;
  for (; i; i -= i & -i) t += bit[i];
  return t;
}
