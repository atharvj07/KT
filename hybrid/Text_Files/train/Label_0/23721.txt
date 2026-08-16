#include <bits/stdc++.h>
using namespace std;
const int N = 100005, M = 50 * N + 5;
int n, m, k, ans, X[N], Y[N];
int cnt = 0, hed[M], to[M], nxt[M];
bool vis[M];
char s[55];
int f[M];
int dfn[M], low[M], bl[M], lb = 0, sum[M];
int sta[M], top = 0, idx = 0;
inline int g(int u, int d) { return u + d * n; }
inline int Min(int x, int y) { return x < y ? x : y; }
inline int Max(int x, int y) { return x > y ? x : y; }
inline void add(int x, int y) {
  to[++cnt] = y, nxt[cnt] = hed[x], hed[x] = cnt;
}
void tarjan(int u) {
  dfn[u] = low[u] = ++idx, sta[++top] = u;
  for (int i = hed[u]; i; i = nxt[i]) {
    int v = to[i];
    if (!dfn[v])
      tarjan(v), low[u] = Min(low[u], low[v]);
    else if (!bl[v])
      low[u] = Min(low[u], dfn[v]);
  }
  if (dfn[u] == low[u]) {
    for (bl[u] = ++lb, sum[lb] += vis[u]; sta[top] != u; --top)
      bl[sta[top]] = lb, sum[lb] += vis[sta[top]];
    --top;
  }
}
int main() {
  scanf("%d%d%d", &n, &m, &k);
  for (int i = (1), ied = (m); i <= ied; i++) {
    scanf("%d%d", &X[i], &Y[i]);
    for (int j = (0), jed = (k - 2); j <= jed; j++)
      add(g(X[i], j), g(Y[i], j + 1));
    add(g(X[i], k - 1), g(Y[i], 0));
  }
  for (int i = (1), ied = (n); i <= ied; i++) {
    scanf("%s", s);
    for (int j = (0), jed = (k - 1); j <= jed; j++) vis[g(i, j)] = s[j] - '0';
  }
  for (int i = (1), ied = (n * k); i <= ied; i++)
    if (!dfn[i]) tarjan(i);
  for (int i = (1), ied = (n); i <= ied; i++)
    for (int j = (0), jed = (k - 1); j <= jed; j++) {
      if (!vis[g(i, j)]) continue;
      for (int h = (j + 1), hed = (k - 1); h <= hed; h++)
        if (vis[g(i, h)] && bl[g(i, h)] == bl[g(i, j)])
          vis[g(i, h)] = 0, --sum[bl[g(i, j)]];
    }
  memset(hed, 0, sizeof(hed)), cnt = 0;
  for (int i = (1), ied = (m); i <= ied; i++) {
    for (int j = (0), jed = (k - 2); j <= jed; j++)
      if (bl[g(X[i], j)] != bl[g(Y[i], j + 1)])
        add(bl[g(X[i], j)], bl[g(Y[i], j + 1)]);
    if (bl[g(X[i], k - 1)] != bl[g(Y[i], 0)])
      add(bl[g(X[i], k - 1)], bl[g(Y[i], 0)]);
  }
  memset(f, -0x3f3f3f3f, sizeof(f)), f[bl[g(1, 0)]] = 0;
  for (int i = (lb), ied = (1); i >= ied; i--) {
    f[i] += sum[i];
    ans = Max(ans, f[i]);
    for (int j = hed[i]; j; j = nxt[j]) f[to[j]] = Max(f[to[j]], f[i]);
  }
  printf("%d\n", ans);
  return 0;
}
