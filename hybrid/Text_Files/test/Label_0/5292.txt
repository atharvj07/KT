#include <bits/stdc++.h>
using namespace std;
int n, q, tot, lastans;
const int N = 100005;
int head[N], to[N << 1], nt[N << 1], len[N << 1];
void add(int f, int t, int d) {
  to[++tot] = t;
  len[tot] = d;
  nt[tot] = head[f];
  head[f] = tot;
}
struct SHU {
  int c, root, pos;
  int fa[N][17], dep[N], top[N], maxdep[N], dis[N], son[N], s[N], ans[N],
      col[N], LEN[N];
  vector<int> v[N];
  void dfs0(int u, int pr, int t) {
    if (t) {
      dep[u] = dep[fa[u][0] = pr] + 1;
      for (int j = 0; 2 << j < dep[u]; ++j) fa[u][j + 1] = fa[fa[u][j]][j];
    }
    maxdep[u] = dis[u];
    if (!t && dis[pos] < dis[u]) pos = u;
    for (int i = head[u]; i; i = nt[i])
      if (to[i] != pr) {
        dis[to[i]] = dis[u] + len[i], dfs0(to[i], u, t);
        maxdep[u] = std::max(maxdep[u], maxdep[to[i]]);
        if (t && maxdep[son[u]] < maxdep[to[i]]) son[u] = to[i];
      }
  }
  void dfs1(int u, int t) {
    v[top[u] = t].push_back(u);
    if (son[u]) dfs1(son[u], t);
    for (int i = head[u]; i; i = nt[i])
      if (to[i] != fa[u][0] && to[i] != son[u])
        dfs1(to[i], to[i]), LEN[to[i]] = maxdep[to[i]] - dis[u];
  }
  int YYCH(int x) {
    pos = 0, dis[x] = 0, dfs0(x, 0, 0);
    dis[root = pos] = 0, dfs0(root, 0, 1);
    dfs1(root, root), LEN[root] = maxdep[root];
    for (int i = 1; i <= n; ++i)
      if (top[i] == i) s[++c] = i;
    std::sort(s + 1, s + c + 1, [&](int i, int j) { return LEN[i] > LEN[j]; });
    for (int i = 1; i <= c; ++i) {
      ans[i] = ans[i - 1] + LEN[s[i]];
      for (int u = s[i]; u; u = son[u]) col[u] = i;
    }
    return root;
  }
  inline int plan(int x, int y, int *arr) {
    int u = x;
    for (int j = 16; j >= 0; --j)
      if (col[fa[u][j]] > y) u = fa[u][j];
    u = fa[u][0];
    return ans[y] + maxdep[x] - arr[u];
  }
  inline int ask(int x, int y) {
    y = 2 * y - 1;
    if (y >= c) return ans[c];
    if (col[x] <= y) return ans[y];
    return std::max(plan(x, y - 1, dis), plan(x, y, maxdep));
  }
} T1, T2;
int main() {
  cin >> n >> q;
  for (int i = 1, x, y, z; i < n; ++i)
    scanf("%d%d%d", &x, &y, &z), add(x, y, z), add(y, x, z);
  T2.YYCH(T1.YYCH(1));
  while (q--) {
    int x, y;
    scanf("%d%d", &x, &y);
    x = (x + lastans - 1) % n + 1;
    y = (y + lastans - 1) % n + 1;
    printf("%d\n", lastans = max(T1.ask(x, y), T2.ask(x, y)));
  }
  return 0;
}
