#include <bits/stdc++.h>
using namespace std;
const double eps = 1e-8;
const int N = 1e6 + 10, INF = 0x3f3f3f3f;
int n, m, x, S, T;
int a[N], b[N], c[N];
struct edge {
  int to;
  long long w;
  int next;
  edge(int to = 0, long long w = 0, int next = 0) : to(to), w(w), next(next) {}
} e[N];
int head[N], dep[N], vis[N], cur[N], cnt = 1;
queue<int> Q;
int bfs() {
  for (int i = 1; i <= n; ++i) dep[i] = INF, vis[i] = 0, cur[i] = head[i];
  dep[S] = 0, Q.push(S);
  while (Q.size()) {
    int u = Q.front();
    Q.pop();
    for (int i = head[u]; i; i = e[i].next) {
      if (dep[e[i].to] > dep[u] + 1 && e[i].w) {
        dep[e[i].to] = dep[u] + 1;
        Q.push(e[i].to);
      }
    }
  }
  return dep[T] != INF;
}
long long dfs(int x, long long w) {
  if (x == T) return w;
  long long used = 0;
  for (int i = cur[x]; i; i = e[i].next) {
    cur[x] = i;
    if (dep[e[i].to] == dep[x] + 1 && e[i].w) {
      int f = dfs(e[i].to, min(w - used, e[i].w));
      if (f) used += f, e[i].w -= f, e[i ^ 1].w += f;
      if (used == w) break;
    }
  }
  return used;
}
long long dinic() {
  long long ans = 0;
  while (bfs()) ans += dfs(S, 1e15);
  return ans;
}
void add(int u, int v, long long w) {
  e[++cnt] = edge(v, w, head[u]);
  head[u] = cnt;
  e[++cnt] = edge(u, 0, head[v]);
  head[v] = cnt;
}
int chk(double w) {
  w /= x;
  if (fabs(w) <= eps) return 1;
  cnt = 1, S = 1, T = n;
  for (int i = 1; i <= n; ++i) head[i] = 0;
  for (int i = 1; i <= m; ++i) add(a[i], b[i], c[i] / w);
  return dinic() >= x;
}
int main() {
  scanf("%d%d%d", &n, &m, &x);
  for (int i = 1; i <= m; ++i) scanf("%d%d%d", a + i, b + i, c + i);
  double l = 0, r = 1e11, ans;
  for (int i = 1; i <= 100; ++i) {
    double mid = (l + r) / 2;
    if (chk(mid))
      ans = mid, l = mid + eps;
    else
      r = mid - eps;
  }
  printf("%.10000lf\n", ans);
}
