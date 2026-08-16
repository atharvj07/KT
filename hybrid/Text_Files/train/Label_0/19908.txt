#include <bits/stdc++.h>
using ll = long long;
namespace LCT {
int lson[200005], rson[200005], fa[200005];
bool rev[200005];
inline bool isrt(int u) { return lson[fa[u]] != u && rson[fa[u]] != u; }
inline void push_up(int u) {}
inline void push_down(int u) {
  if (!u || !rev[u]) return;
  std::swap(lson[u], rson[u]);
  rev[lson[u]] ^= 1;
  rev[rson[u]] ^= 1;
  rev[u] = false;
}
inline void rotate(int u) {
  int v = fa[u], *same = lson[v] == u ? lson : rson,
      *ano = lson[v] == u ? rson : lson;
  fa[u] = fa[v];
  if (!isrt(v)) (lson[fa[v]] == v ? lson : rson)[fa[v]] = u;
  same[v] = ano[u];
  fa[ano[u]] = v;
  ano[u] = v;
  fa[v] = u;
  push_up(v);
  push_up(u);
}
void splay(int u) {
  static int stk[200005];
  int tp = 0;
  stk[tp++] = u;
  for (int v = u; !isrt(v); v = fa[v]) stk[tp++] = fa[v];
  while (tp--) push_down(stk[tp]);
  while (!isrt(u)) {
    int v = fa[u];
    if (!isrt(v)) {
      if ((lson[fa[v]] == v) != (lson[v] == u))
        rotate(u);
      else
        rotate(v);
    }
    rotate(u);
  }
}
void access(int u) {
  for (int v = 0; u; v = u, u = fa[u]) {
    splay(u);
    rson[u] = v;
    push_up(u);
  }
}
int getfa(int u) {
  access(u);
  splay(u);
  push_down(u);
  while (lson[u]) {
    u = lson[u];
    push_down(u);
  }
  return u;
}
void mkrt(int u) {
  access(u);
  splay(u);
  rev[u] ^= 1;
}
void link(int u, int v) {
  mkrt(u);
  fa[u] = v;
}
void cut(int u, int v) {
  mkrt(u);
  access(v);
  splay(v);
  lson[v] = fa[u] = 0;
}
}  // namespace LCT
namespace segT {
struct data {
  int val, cnt;
} seg[800005];
int lazy[800005];
data operator+(const data &a, const data &b) {
  data res;
  res.val = std::min(a.val, b.val);
  res.cnt = a.cnt * (a.val == res.val) + b.cnt * (b.val == res.val);
  return res;
}
inline void paint(int u, int x) {
  lazy[u] += x;
  seg[u].val += x;
}
inline void push_down(int u) {
  if (lazy[u]) {
    paint(u << 1, lazy[u]);
    paint(u << 1 | 1, lazy[u]);
    lazy[u] = 0;
  }
}
void build(int u, int l, int r) {
  if (l == r) {
    seg[u] = {l, 1};
    return;
  }
  int m = l + r >> 1;
  build(u << 1, l, m);
  build(u << 1 | 1, m + 1, r);
  seg[u] = seg[u << 1] + seg[u << 1 | 1];
}
void modify(int u, int l, int r, int L, int R, int x) {
  if (L <= l && r <= R) {
    paint(u, x);
    return;
  }
  push_down(u);
  int m = l + r >> 1;
  if (L <= m) modify(u << 1, l, m, L, R, x);
  if (m < R) modify(u << 1 | 1, m + 1, r, L, R, x);
  seg[u] = seg[u << 1] + seg[u << 1 | 1];
}
data query(int u, int l, int r, int L, int R) {
  if (L <= l && r <= R) return seg[u];
  push_down(u);
  int m = l + r >> 1;
  data res = {(int)1e9, 0};
  if (L <= m) res = res + query(u << 1, l, m, L, R);
  if (m < R) res = res + query(u << 1 | 1, m + 1, r, L, R);
  return res;
}
}  // namespace segT
constexpr int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
int n, m, arr[1005][1005], pos_x[200005], pos_y[200005], lim[200005], seq[5];
template <typename T>
void for_adj(int u, T func) {
  int x = pos_x[u], y = pos_y[u];
  for (int i = 0; i < 4; i++) {
    int xx = x + dx[i], yy = y + dy[i];
    if (xx >= 0 && xx < n && yy >= 0 && yy < m) func(arr[xx][yy]);
  }
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf("%d", arr[i] + j);
      pos_x[--arr[i][j]] = i;
      pos_y[arr[i][j]] = j;
    }
  }
  for (int l = 0, r = 0; l < n * m; l++) {
    while (r < n * m) {
      int cnt = 0;
      for_adj(r, [&](int u) {
        if (u >= l && u < r) seq[cnt++] = LCT::getfa(u + 1) - 1;
      });
      bool flg = false;
      for (int i = 0; i < cnt && !flg; i++) {
        for (int j = 0; j < i && !flg; j++) flg |= seq[i] == seq[j];
      }
      if (flg) break;
      for_adj(r, [&](int u) {
        if (u >= l && u < r) LCT::link(u + 1, r + 1);
      });
      r++;
    }
    lim[l] = r - 1;
    for_adj(l, [&](int u) {
      if (u >= l && u < r) LCT::cut(u + 1, l + 1);
    });
  }
  segT::build(1, 0, n * m - 1);
  ll ans = 0;
  for (int i = n * m - 1; i >= 0; i--) {
    for_adj(i, [&](int u) {
      if (u >= i) segT::modify(1, 0, n * m - 1, u, n * m - 1, -1);
    });
    auto res = segT::query(1, 0, n * m - 1, i, lim[i]);
    ans += res.cnt * (res.val == i);
  }
  printf("%lld\n", ans);
  return 0;
}
