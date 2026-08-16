#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
const int M = N * 25;
int n, m;
long long C[M], x, y, tar[N], dep[N], in[M];
int fir[N], ne[M], to[M], cnt = 1, fa[N], fan[N];
void add(int x, int y) {
  ne[++cnt] = fir[x];
  fir[x] = cnt;
  to[cnt] = y;
}
void link(int x, int y) {
  add(x, y);
  add(y, x);
}
bool vis[N];
int dfs(int x, int f) {
  int res = 0;
  fa[x] = f;
  dep[x] = dep[f] + 1;
  vis[x] = 1;
  for (int i = fir[x]; i; i = ne[i]) {
    int V = to[i];
    if (vis[V]) {
      if (V != f) {
        if ((dep[V] + dep[x]) & 1)
          ;
        else
          res = i;
      }
      continue;
    }
    int cur = 0;
    if (cur = dfs(V, x)) res = cur;
    if (tar[V]) {
      tar[x] -= tar[V];
      C[i] += tar[V];
      C[i ^ 1] += tar[V];
      tar[V] = 0;
    }
    fan[V] = i;
  }
  return res;
}
void Bush(int x) {
  while (fa[x]) {
    tar[fa[x]] -= tar[x];
    C[fan[x]] += tar[x];
    C[fan[x] ^ 1] += tar[x];
    tar[x] = 0;
    x = fa[x];
  }
}
int main(void) {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i) scanf("%lld", &tar[i]);
  for (int i = 1; i <= m; ++i) scanf("%d%d", &x, &y), link(x, y);
  for (int i = 1; i <= n; ++i) {
    if (!vis[i]) {
      int cur = dfs(i, 0), a;
      if ((tar[i]) & 1 || (!cur && tar[i])) return puts("NO") * 0;
      a = (dep[to[cur]] & 1);
      C[cur] = C[cur ^ 1] += tar[i] / 2 * (a ? 1 : (-1));
      tar[to[cur ^ 1]] = tar[to[cur]] = -tar[i] / 2 * (a ? 1 : (-1));
      Bush(to[cur]);
      Bush(to[cur ^ 1]);
    }
  }
  puts("YES");
  for (int i = 1; i <= m; ++i) printf("%lld\n", C[i * 2]);
}
