#include <bits/stdc++.h>
inline int read() {
  int x = 0;
  char ch = getchar();
  for (; ch < 48 || ch > 57; ch = getchar())
    ;
  for (; ch > 47 && ch < 58; ch = getchar())
    x = (x << 1) + (x << 3) + (ch ^ 48);
  return x;
}
using namespace std;
int poi[300005], fir[300005], son[300005], fat[300005], top[300005],
    siz[300005], dep[300005], arr[300005 << 1], nex[300005 << 1],
    cot[300005 << 1], e;
long long dwn[300005], edg[300005], sum[300005], fly[300005], dis[300005];
void dfs(int u) {
  dwn[u] = poi[u];
  dep[u] = dep[fat[u]] + (siz[u] = 1);
  for (int i = fir[u], v; i; i = nex[i])
    if ((v = arr[i]) != fat[u]) {
      fat[v] = u;
      dis[v] = cot[i];
      dfs(v);
      siz[u] += siz[v];
      dwn[u] += edg[v];
      if (siz[v] > siz[son[u]]) son[u] = v;
    }
  edg[u] = max(0ll, dwn[u] - 2 * dis[u]);
}
void DFS(int u) {
  fly[u] =
      max(0ll, fly[fat[u]] + (sum[u] = dwn[fat[u]] - edg[u] - dis[u]) - dis[u]);
  sum[u] += sum[fat[u]];
  if (son[u]) {
    top[son[u]] = top[u], DFS(son[u]);
    for (int i = fir[u]; i; i = nex[i])
      if (arr[i] != fat[u] && arr[i] != son[u])
        top[arr[i]] = arr[i], DFS(arr[i]);
  }
}
int lca(int x, int y) {
  for (; top[x] != top[y];)
    dep[top[x]] > dep[top[y]] ? x = fat[top[x]] : y = fat[top[y]];
  return dep[x] < dep[y] ? x : y;
}
int main() {
  int n = read(), q = read();
  for (int i = 1; i <= n; ++i) poi[i] = read();
  for (int i = 1; i < n; ++i) {
    int u = read(), v = read(), w = read();
    arr[++e] = v;
    nex[e] = fir[u];
    fir[u] = e;
    cot[e] = w;
    arr[++e] = u;
    nex[e] = fir[v];
    fir[v] = e;
    cot[e] = w;
  }
  dfs(1);
  top[1] = 1;
  DFS(1);
  for (int i = 0; i < q; ++i) {
    int u = read(), v = read(), l = lca(u, v);
    printf("%lld\n",
           sum[u] + sum[v] - (sum[l] << 1) + dwn[u] + dwn[v] - dwn[l] + fly[l]);
  }
  return 0;
}
