#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 5;
int n, tme, m = 1, q;
int a[N], pl[N], p[N], dep[N], B[N], E[N];
int lg[N * 2];
pair<int, int> MN[22][N * 2];
vector<int> son[N];
int lca(int x, int y) {
  if (B[x] > B[y]) swap(x, y);
  x = B[x], y = E[y];
  int l = lg[y - x + 1];
  return min(MN[l][x], MN[l][y - (1 << l) + 1]).second;
}
void dfs(int x) {
  B[x] = E[x] = ++tme;
  MN[0][tme] = make_pair(dep[x], x);
  for (int i = 0; i < int(son[x].size()); i++) {
    int to = son[x][i];
    dep[to] = dep[x] + 1;
    dfs(to);
    E[x] = ++tme;
    MN[0][tme] = make_pair(dep[x], x);
  }
}
struct Line {
  int status;
  int px, py;
  Line() : px(0), py(0), status(0){};
  Line(int px, int py) : px(px), py(py), status(1){};
  int length() const { return dep[px] + dep[py] - 2 * dep[lca(px, py)]; }
  bool operator<(const Line &oth) const { return length() < oth.length(); }
  bool operator>(const Line &oth) const { return oth < (*this); }
  bool operator==(const Line &oth) const {
    return !((*this) < oth) && !(oth < (*this));
  }
  Line operator+(const Line &oth) const {
    if (!status) return oth;
    if (!oth.status) return (*this);
    if (status == 2) return (*this);
    if (oth.status == 2) return oth;
    Line r[7], mx, res;
    mx = r[1] = (*this);
    r[2] = oth;
    r[3] = Line(px, oth.px);
    r[4] = Line(px, oth.py);
    r[5] = Line(py, oth.px);
    r[6] = Line(py, oth.py);
    for (int i = 1; i <= 6; i++) mx = max(mx, r[i]);
    for (int i = 1; i <= 6; i++)
      if (mx == r[i]) {
        if (Line(mx.px, px).length() + Line(px, mx.py).length() ==
                mx.length() &&
            Line(mx.px, py).length() + Line(py, mx.py).length() ==
                mx.length() &&
            Line(mx.px, oth.px).length() + Line(oth.px, mx.py).length() ==
                mx.length() &&
            Line(mx.px, oth.py).length() + Line(oth.py, mx.py).length() ==
                mx.length())
          res = mx;
        else
          res.status = 2;
        break;
      }
    return res;
  }
};
int lson[N * 2], rson[N * 2];
Line val[N * 2];
void build(int pos, int x, int y) {
  if (x == y) {
    val[pos] = Line(pl[x], pl[x]);
    return;
  }
  int mid = (x + y) >> 1;
  lson[pos] = ++m;
  rson[pos] = ++m;
  build(lson[pos], x, mid);
  build(rson[pos], mid + 1, y);
  val[pos] = val[lson[pos]] + val[rson[pos]];
}
void modify(int pos, int x, int y, int l) {
  if (x >= l && y <= l) {
    val[pos] = Line(pl[l], pl[l]);
    return;
  }
  if (x > l || y < l) return;
  int mid = (x + y) >> 1;
  modify(lson[pos], x, mid, l);
  modify(rson[pos], mid + 1, y, l);
  val[pos] = val[lson[pos]] + val[rson[pos]];
}
int query(int pos, int x, int y, Line v) {
  Line nv;
  if (x == y) {
    nv = v + val[pos];
    if (nv.status == 2) x--;
    return x;
  }
  nv = v + val[lson[pos]];
  int mid = (x + y) >> 1;
  if (nv.status != 2)
    return query(rson[pos], mid + 1, y, nv);
  else
    return query(lson[pos], x, mid, v);
}
int main() {
  lg[1] = 0;
  for (int i = 2; i < N * 2; i++) lg[i] = lg[i / 2] + 1;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    int x;
    scanf("%d", &x);
    x++;
    a[i] = x;
    pl[x] = i;
  }
  for (int i = 2; i <= n; i++) {
    scanf("%d", p + i);
    son[p[i]].push_back(i);
  }
  dfs(1);
  for (int i = 1; i <= 21; i++)
    for (int j = 1; j + (1 << i) - 1 <= tme; j++)
      MN[i][j] = min(MN[i - 1][j], MN[i - 1][j + (1 << (i - 1))]);
  build(1, 1, n);
  scanf("%d", &q);
  while (q--) {
    int o;
    scanf("%d", &o);
    if (o == 1) {
      int x, y;
      scanf("%d%d", &x, &y);
      swap(a[x], a[y]);
      pl[a[x]] = x;
      pl[a[y]] = y;
      modify(1, 1, n, a[x]);
      modify(1, 1, n, a[y]);
    } else
      printf("%d\n", query(1, 1, n, Line()));
  }
  return 0;
}
