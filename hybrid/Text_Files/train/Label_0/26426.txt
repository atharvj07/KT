#include <bits/stdc++.h>
using namespace std;
int n, m, tot;
int head[400010], dep[400010], dfn[400010];
struct edge {
  int fr, to, nxt;
} e[400010 << 1];
int read() {
  int s = 0, w = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') w = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9')
    s = (s << 1) + (s << 3) + ch - '0', ch = getchar();
  return s * w;
}
void add(int fr, int to) {
  e[++tot] = (edge){fr, to, head[fr]};
  head[fr] = tot;
}
namespace Seg {
int b[400010], w[400010];
void pushup(int x) {
  b[x] = b[x << 1] + b[x << 1 | 1];
  w[x] = w[x << 1] + w[x << 1 | 1];
}
void build(int x, int l, int r) {
  if (l == r) {
    b[x] = 1;
    return;
  }
  int mid = l + r >> 1;
  build(x << 1, l, mid);
  build(x << 1 | 1, mid + 1, r);
  pushup(x);
}
void update_b(int x, int l, int r, int pos) {
  if (l == r) {
    w[x] = 0;
    b[x] = 1;
    return;
  }
  int mid = l + r >> 1;
  if (pos <= mid)
    update_b(x << 1, l, mid, pos);
  else
    update_b(x << 1 | 1, mid + 1, r, pos);
  pushup(x);
}
void update_w(int x, int l, int r, int pos) {
  if (l == r) {
    b[x] = 0;
    w[x] = 1;
    return;
  }
  int mid = l + r >> 1;
  if (pos <= mid)
    update_w(x << 1, l, mid, pos);
  else
    update_w(x << 1 | 1, mid + 1, r, pos);
  pushup(x);
}
int judge(int x, int l, int r, int L, int R) {
  int ans = 0;
  if (L <= l && R >= r) return w[x];
  int mid = l + r >> 1;
  if (L <= mid) ans += judge(x << 1, l, mid, L, R);
  if (R >= mid + 1) ans += judge(x << 1 | 1, mid + 1, r, L, R);
  return ans;
}
int query(int x, int l, int r, int L, int R) {
  int ans = 0;
  if (L <= l && R >= r) return b[x];
  int mid = l + r >> 1;
  if (L <= mid) ans += query(x << 1, l, mid, L, R);
  if (R >= mid + 1) ans += query(x << 1 | 1, mid + 1, r, L, R);
  return ans;
}
}  // namespace Seg
namespace Cut {
int cnt = 0;
int top[400010], son[400010];
int fa[400010], siz[400010];
void dfs1(int u, int fat) {
  dep[u] = dep[fat] + 1;
  fa[u] = fat;
  siz[u] = 1;
  for (int i = head[u]; i; i = e[i].nxt) {
    int to = e[i].to;
    if (to == fat) continue;
    dfs1(to, u);
    siz[u] += siz[to];
    if (siz[son[u]] < siz[to]) son[u] = to;
  }
}
void dfs2(int u, int tp) {
  top[u] = tp;
  dfn[u] = ++cnt;
  if (son[u]) dfs2(son[u], tp);
  for (int i = head[u]; i; i = e[i].nxt) {
    int to = e[i].to;
    if (to == fa[u] || to == son[u]) continue;
    dfs2(to, to);
  }
}
int query_w(int fr, int to) {
  int ans = 0;
  while (top[fr] != top[to]) {
    if (dep[top[fr]] < dep[top[to]]) swap(fr, to);
    ans += Seg::judge(1, 1, n, dfn[top[fr]], dfn[fr]);
    fr = fa[top[fr]];
  }
  if (dep[fr] > dep[to]) swap(fr, to);
  ans += Seg::judge(1, 1, n, dfn[fr] + 1, dfn[to]);
  return ans;
}
int query_b(int fr, int to) {
  int ans = 0;
  while (top[fr] != top[to]) {
    if (dep[top[fr]] < dep[top[to]]) swap(fr, to);
    ans += Seg::query(1, 1, n, dfn[top[fr]], dfn[fr]);
    fr = fa[top[fr]];
  }
  if (dep[fr] > dep[to]) swap(fr, to);
  ans += Seg::query(1, 1, n, dfn[fr] + 1, dfn[to]);
  return ans;
}
}  // namespace Cut
int main() {
  n = read();
  for (int i = 1, fr, to; i < n; i++) {
    fr = read();
    to = read();
    add(fr, to);
    add(to, fr);
  }
  Seg::build(1, 1, n);
  Cut::dfs1(1, 0);
  Cut::dfs2(1, 1);
  m = read();
  for (int i = 1, opt, u, v; i <= m; i++) {
    opt = read();
    u = read();
    if (opt == 1)
      Seg::update_b(1, 1, n,
                    dep[e[u * 2].fr] < dep[e[u * 2].to] ? dfn[e[u * 2].to]
                                                        : dfn[e[u * 2].fr]);
    else if (opt == 2)
      Seg::update_w(1, 1, n,
                    dep[e[u * 2].fr] < dep[e[u * 2].to] ? dfn[e[u * 2].to]
                                                        : dfn[e[u * 2].fr]);
    else {
      v = read();
      if (Cut::query_w(u, v))
        printf("-1\n");
      else
        printf("%d\n", Cut::query_b(u, v));
    }
  }
  return 0;
}
