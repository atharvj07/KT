#include <bits/stdc++.h>
using namespace std;
const int N = 200005;
struct edge {
  int to, next, v;
} e[N * 2];
int head[N], tot, n;
int vis[N], w[N], sz[N];
int ansid, mxv, mxrt;
double ans, S0, S1;
void add(int x, int y, int v) {
  e[++tot] = (edge){y, head[x], v};
  head[x] = tot;
}
void dfs(int x, int fa, int n) {
  sz[x] = 1;
  int mx = 0;
  for (int i = head[x]; i; i = e[i].next)
    if (e[i].to != fa && !vis[e[i].to]) {
      dfs(e[i].to, x, n);
      sz[x] += sz[e[i].to];
      mx = max(mx, sz[e[i].to]);
    }
  mx = max(mx, n - sz[x]);
  if (mx < mxv) mxv = mx, mxrt = x;
}
void calc(int x, int fa, int d) {
  double SQ = sqrt(d);
  S0 += w[x] * SQ * d;
  S1 += w[x] * SQ;
  for (int i = head[x]; i; i = e[i].next)
    if (e[i].to != fa) calc(e[i].to, x, d + e[i].v);
}
void solve(int x, int n) {
  mxv = 1 << 30;
  dfs(x, 0, n);
  vis[x = mxrt] = 1;
  double mx = S0 = 0;
  int id = 0;
  for (int i = head[x]; i; i = e[i].next) {
    S1 = 0;
    calc(e[i].to, x, e[i].v);
    if (!vis[e[i].to] && S1 > mx) mx = S1, id = e[i].to;
  }
  if (S0 < ans) ans = S0, ansid = x;
  if (id) solve(id, sz[id] > sz[x] ? n - sz[x] : sz[id]);
}
int main() {
  scanf("%d", &n);
  for (int i = (int)(1); i <= (int)(n); i++) scanf("%d", &w[i]);
  for (int i = (int)(1); i <= (int)(n - 1); i++) {
    int x, y, v;
    scanf("%d%d%d", &x, &y, &v);
    add(x, y, v);
    add(y, x, v);
  }
  ans = 1e100;
  solve(1, n);
  printf("%d %.15lf\n", ansid, ans);
}
