#include <bits/stdc++.h>
using namespace std;
namespace FGF {
const int N = 1e5 + 5;
int n, m, is[N], f[N][3], g[N][3], h[N][2], sum[N], ans, mx, cnt, head[N],
    lca[N], fa[N];
struct edg {
  int to, nxt, w;
} e[N << 1];
void add(int u, int v, int w) {
  cnt++;
  e[cnt].to = v;
  e[cnt].nxt = head[u];
  head[u] = cnt;
  e[cnt].w = w;
}
void dfs(int u, int ff) {
  if (is[u]) f[u][0] = 0, g[u][0] = u;
  fa[u] = ff;
  for (int i = head[u]; i; i = e[i].nxt) {
    int v = e[i].to;
    if (v != ff) {
      dfs(v, u);
      int w = e[i].w + f[v][0];
      if (w > f[u][0])
        f[u][2] = f[u][1], f[u][1] = f[u][0], f[u][0] = w, g[u][2] = g[u][1],
        g[u][1] = g[u][0], g[u][0] = lca[v], h[u][1] = h[u][0], h[u][0] = v;
      else if (w > f[u][1])
        f[u][2] = f[u][1], f[u][1] = w, g[u][2] = g[u][1], g[u][1] = lca[v],
        h[u][1] = v;
      else if (w > f[u][2])
        f[u][2] = w, g[u][2] = lca[v];
    }
  }
  lca[u] = (f[u][0] == f[u][1] ? u : g[u][0]);
}
void dp(int u, int x, int LCA, int len) {
  if (is[u]) {
    if (f[u][0] > len) sum[lca[u]]++, sum[fa[u]]--;
    if (f[u][0] < len) sum[u]++, sum[x]++, sum[LCA]--, sum[fa[LCA]]--;
  }
  for (int i = head[u], k, l; i; i = e[i].nxt) {
    int v = e[i].to;
    if (v != fa[u]) {
      if (v == h[u][0])
        k = f[u][1], l = (f[u][1] == f[u][2] ? u : g[u][1]);
      else if (v == h[u][1])
        k = f[u][0], l = (f[u][0] == f[u][2] ? u : g[u][0]);
      else
        k = f[u][0], l = lca[u];
      if (k > len)
        dp(v, l, u, e[i].w + k);
      else if (k == len)
        dp(v, u, u, e[i].w + k);
      else
        dp(v, x, LCA, len + e[i].w);
    }
  }
}
void dfs2(int u, int fa) {
  for (int i = head[u]; i; i = e[i].nxt)
    if (e[i].to != fa) dfs2(e[i].to, u), sum[u] += sum[e[i].to];
}
void work() {
  scanf("%d%d", &n, &m);
  for (int i = 1, x; i <= m; i++) scanf("%d", &x), is[x] = 1;
  for (int i = 1, u, v, w; i < n; i++)
    scanf("%d%d%d", &u, &v, &w), add(u, v, w), add(v, u, w);
  memset(f, -0x3f, sizeof(f));
  dfs(1, 0), dp(1, 0, 0, -1e9), dfs2(1, 0);
  for (int i = 1; i <= n; i++)
    if (!is[i]) {
      if (sum[i] > mx)
        mx = sum[i], ans = 1;
      else if (sum[i] == mx)
        ans++;
    }
  printf("%d %d\n", mx, ans);
}
}  // namespace FGF
int main() {
  FGF::work();
  return 0;
}
