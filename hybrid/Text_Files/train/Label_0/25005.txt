#include <bits/stdc++.h>
using namespace std;
const int MAXN = 4e5 + 5;
int n, size[MAXN], hev[MAXN], down[MAXN], up[MAXN];
int tot, Last[MAXN], Go[MAXN * 2], Next[MAXN * 2];
void link(int u, int v) { Next[++tot] = Last[u], Last[u] = tot, Go[tot] = v; }
void dfs1(int now, int pre) {
  size[now] = 1;
  for (int p = Last[now]; p; p = Next[p]) {
    int v = Go[p];
    if (v == pre) continue;
    dfs1(v, now);
    size[now] += size[v];
    down[now] = max(down[now], (size[v] <= n / 2) ? size[v] : down[v]);
    hev[now] = max(hev[now], size[v]);
  }
}
void dfs2(int now, int pre) {
  multiset<int> d;
  for (int p = Last[now]; p; p = Next[p]) {
    int v = Go[p];
    if (v != pre) d.insert((size[v] <= n / 2) ? size[v] : down[v]);
  }
  for (int p = Last[now]; p; p = Next[p]) {
    int v = Go[p];
    if (v == pre) continue;
    if (n - size[v] <= n / 2)
      up[v] = max(up[v], n - size[v]);
    else {
      up[v] = max(up[v], up[now]);
      d.erase(d.find(size[v] <= n / 2 ? size[v] : down[v]));
      if (!d.empty()) up[v] = max(up[v], *d.rbegin());
      d.insert((size[v] <= n / 2) ? size[v] : down[v]);
    }
    dfs2(v, now);
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i < n; i++) {
    int u, v;
    scanf("%d%d", &u, &v);
    link(u, v), link(v, u);
  }
  dfs1(1, 0);
  dfs2(1, 0);
  for (int i = 1; i <= n; i++) {
    int ans = 1;
    if (n - size[i] > n / 2) ans = (n - size[i] - up[i] <= n / 2);
    if (hev[i] > n / 2) ans = (hev[i] - down[i] <= n / 2);
    printf("%d ", ans);
  }
}
