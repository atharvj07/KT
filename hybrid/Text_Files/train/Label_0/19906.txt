#include <bits/stdc++.h>
using namespace std;
const int N = 1000005;
namespace LCT {
struct TNode {
  int ch[2], f;
  bool r;
};
TNode t[N];
inline bool isroot(int pos) {
  return t[t[pos].f].ch[0] != pos && t[t[pos].f].ch[1] != pos;
}
inline void pushdown(int pos) {
  if (t[pos].r) {
    t[pos].r = 0;
    t[t[pos].ch[0]].r ^= 1;
    t[t[pos].ch[1]].r ^= 1;
    swap(t[pos].ch[0], t[pos].ch[1]);
  }
}
void rotate(int pos) {
  int y = t[pos].f, z = t[y].f, k = t[y].ch[1] == pos, w = t[pos].ch[k ^ 1];
  if (!isroot(y)) t[z].ch[t[z].ch[1] == y] = pos;
  t[pos].f = z;
  t[pos].ch[!k] = y;
  t[y].ch[k] = w;
  t[w].f = y;
  t[y].f = pos;
}
int stk[N];
void splay(int pos) {
  int ptr = 0, tmp = pos;
  stk[ptr++] = tmp;
  while (!isroot(tmp)) stk[ptr++] = tmp = t[tmp].f;
  while (ptr--) pushdown(stk[ptr]);
  while (!isroot(pos)) {
    int y = t[pos].f, z = t[y].f;
    if (!isroot(y)) rotate((t[y].ch[0] == pos) ^ (t[z].ch[0] == y) ? pos : y);
    rotate(pos);
  }
}
void access(int pos) {
  for (int last = 0; pos; pos = t[last = pos].f)
    splay(pos), t[pos].ch[1] = last;
}
inline void makeroot(int pos) {
  access(pos);
  splay(pos);
  t[pos].r ^= 1;
}
int findroot(int pos) {
  access(pos);
  splay(pos);
  pushdown(pos);
  while (t[pos].ch[0]) pushdown(pos = t[pos].ch[0]);
  splay(pos);
  return pos;
}
inline void split(int x, int y) {
  makeroot(x);
  access(y);
  splay(y);
}
inline bool link(int x, int y) {
  makeroot(x);
  if (findroot(y) != x) {
    t[x].f = y;
    return 1;
  } else
    return 0;
}
inline void cut(int x, int y) {
  makeroot(x);
  if (findroot(y) == x && t[y].f == x && !t[y].ch[0]) t[x].ch[1] = t[y].f = 0;
}
}  // namespace LCT
struct SegTree {
  struct TNode {
    int l, r, mn, v;
  } t[N << 2];
  int lazy[N << 2];
  inline int lc(int pos) { return pos << 1; }
  inline int rc(int pos) { return pos << 1 | 1; }
  inline void pushdown(int pos) {
    if (lazy[pos]) {
      lazy[lc(pos)] += lazy[pos];
      lazy[rc(pos)] += lazy[pos];
      t[lc(pos)].mn += lazy[pos];
      t[rc(pos)].mn += lazy[pos];
      lazy[pos] = 0;
    }
  }
  void pushup(int pos) {
    t[pos].mn = min(t[lc(pos)].mn, t[rc(pos)].mn);
    t[pos].v = t[lc(pos)].v * (t[pos].mn == t[lc(pos)].mn) +
               t[rc(pos)].v * (t[pos].mn == t[rc(pos)].mn);
  }
  void build(int pos, int l, int r) {
    t[pos].l = l;
    t[pos].r = r;
    if (l == r) {
      t[pos].v = 1;
      return;
    }
    int mid = (l + r) >> 1;
    build(lc(pos), l, mid);
    build(rc(pos), mid + 1, r);
    pushup(pos);
  }
  void modify(int pos, int l, int r, int v) {
    if (t[pos].l == l && t[pos].r == r) {
      lazy[pos] += v, t[pos].mn += v;
      return;
    }
    pushdown(pos);
    int mid = (t[pos].l + t[pos].r) >> 1;
    if (r <= mid)
      modify(lc(pos), l, r, v);
    else if (l > mid)
      modify(rc(pos), l, r, v);
    else
      modify(lc(pos), l, mid, v), modify(rc(pos), mid + 1, r, v);
    pushup(pos);
  }
  int query(int pos, int l, int r) {
    if (t[pos].l == l && t[pos].r == r) return (t[pos].mn == 1) * t[pos].v;
    pushdown(pos);
    int mid = (t[pos].l + t[pos].r) >> 1;
    if (r <= mid)
      return query(lc(pos), l, r);
    else if (l > mid)
      return query(rc(pos), l, r);
    else
      return query(lc(pos), l, mid) + query(rc(pos), mid + 1, r);
  }
} t;
using ll = long long;
vector<int> v[N];
const int M = 3005;
const int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};
int n, m, w[M][M];
ll ans;
int main() {
  ios::sync_with_stdio(false);
  cin >> n >> m;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++) cin >> w[i][j];
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
      for (int k = 0; k < 4; k++) {
        int x = i + dx[k], y = j + dy[k];
        if (x < 1 || y < 1 || x > n || y > m || w[i][j] > w[x][y]) continue;
        v[w[x][y]].push_back(w[i][j]);
        v[w[i][j]].push_back(w[x][y]);
      }
  int r = 0, tt = n * m;
  t.build(1, 1, tt);
  for (int i = 1; i <= tt; i++) {
    for (int j = r + 1; j <= tt; j++) {
      int fl = 0;
      for (auto &d : v[j])
        if (d < j && d >= i && !LCT::link(d, j)) {
          fl = 1;
          break;
        }
      for (auto &d : v[j]) LCT::cut(j, d);
      if (fl == 1) break;
      r = j;
      int cc = 0;
      for (auto &d : v[j])
        if (d < j && d >= i) LCT::link(d, j), ++cc;
      t.modify(1, r, r, r - i + 1);
      t.modify(1, r, tt, -cc);
    }
    ans += t.query(1, i, r);
    for (auto &d : v[i])
      if (d <= r && d > i) LCT::cut(d, i), t.modify(1, d, tt, 1);
    t.modify(1, i, r, -1);
  }
  cout << ans << endl;
  return 0;
}
