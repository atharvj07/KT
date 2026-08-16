#include <bits/stdc++.h>
using namespace std;
template <class T>
void read(T &first) {
  char ch;
  for (ch = getchar(); (ch < '0' || ch > '9') && ch != '-';) ch = getchar();
  first = 0;
  int t = 1;
  if (ch == '-') {
    ch = getchar();
    t = -1;
  }
  for (; ch >= '0' && ch <= '9'; ch = getchar()) first = first * 10 + ch - '0';
  first *= t;
}
const int N = 100010;
const long long inf = 1000000000000000000ll;
struct segtree {
  long long ma, mi, delta;
  int lch, rch, lnum, rnum;
} tree[4 * N];
int cnt, a[N], op[N], c[N][2], l[N], r[N], deg[N];
long long t[N], s[N];
pair<int, int> b[2 * N];
void build(int k, int l, int r) {
  tree[k].lnum = l;
  tree[k].rnum = r;
  tree[k].delta = 0;
  tree[k].ma = -inf;
  tree[k].mi = inf;
  if (l == r) return;
  int mid = (l + r) >> 1;
  tree[k].lch = ++cnt;
  build(cnt, l, mid);
  tree[k].rch = ++cnt;
  build(cnt, mid + 1, r);
}
void update(int k, long long d) {
  tree[k].mi += d;
  tree[k].ma += d;
  tree[k].delta += d;
}
void pushdown(int k) {
  if (tree[k].delta) {
    update(tree[k].lch, tree[k].delta);
    update(tree[k].rch, tree[k].delta);
    tree[k].delta = 0;
  }
}
void pushup(int k) {
  tree[k].mi = min(tree[tree[k].lch].mi, tree[tree[k].rch].mi);
  tree[k].ma = max(tree[tree[k].lch].ma, tree[tree[k].rch].ma);
}
void change1(int k, int l, int r, long long d) {
  if (l <= tree[k].lnum && r >= tree[k].rnum) {
    update(k, d);
    return;
  }
  pushdown(k);
  if (l < tree[tree[k].rch].lnum) change1(tree[k].lch, l, r, d);
  if (r > tree[tree[k].lch].rnum) change1(tree[k].rch, l, r, d);
  pushup(k);
}
void change2(int k, int p, long long d1, long long d2) {
  if (tree[k].lnum == tree[k].rnum) {
    tree[k].mi = d1;
    tree[k].ma = d2;
    return;
  }
  pushdown(k);
  if (p < tree[tree[k].rch].lnum)
    change2(tree[k].lch, p, d1, d2);
  else
    change2(tree[k].rch, p, d1, d2);
  pushup(k);
}
long long query(int k, int p) {
  if (tree[k].lnum == tree[k].rnum) return tree[k].mi;
  pushdown(k);
  if (p < tree[tree[k].rch].lnum)
    return query(tree[k].lch, p);
  else
    return query(tree[k].rch, p);
}
int main() {
  int n, q;
  read(n);
  read(q);
  for (int i = 1; i <= n; i++) read(t[i]);
  for (int i = 1; i <= n; i++) read(a[i]);
  for (int i = 1; i <= n; i++) b[i] = make_pair(a[i], i);
  int m = n;
  for (int i = 1; i <= q; i++) {
    read(op[i]);
    if (op[i] < 3) {
      read(c[i][0]);
      if (op[i] == 1) {
        read(c[i][1]);
        b[++m] = make_pair(c[i][1], c[i][0]);
      }
    }
  }
  sort(b + 1, b + m + 1);
  int tm = 1;
  for (int i = 2; i <= m; i++)
    if (b[i - 1] != b[i]) b[++tm] = b[i];
  m = tm;
  for (int i = 1; i <= n; i++) {
    l[i] = m + 1;
    r[i] = 0;
  }
  for (int i = 1; i <= m; i++) r[b[i].first] = i;
  for (int i = m; i; i--) l[b[i].first] = i;
  cnt = 0;
  build(0, 1, m);
  for (int i = 1; i <= n; i++) deg[a[i]]++;
  for (int i = 1; i <= n; i++)
    s[i] =
        t[i] - t[i] / (deg[i] + 2) * (deg[i] + 1) + t[a[i]] / (deg[a[i]] + 2);
  for (int i = 1; i <= n; i++) s[a[i]] += t[i] / (deg[i] + 2);
  for (int i = 1; i <= n; i++)
    change2(0, lower_bound(b + 1, b + m + 1, make_pair(a[i], i)) - b, s[i],
            s[i]);
  for (int i = 1; i <= q; i++) {
    if (op[i] == 1) {
      int first = c[i][0], second = a[c[i][0]], z = c[i][1];
      long long w =
          t[second] / (deg[second] + 1) - t[second] / (deg[second] + 2);
      change1(0, l[second], r[second], w);
      int p =
          lower_bound(b + 1, b + m + 1, make_pair(a[a[second]], a[second])) - b;
      change1(0, p, p, w);
      w = -t[second] / (deg[second] + 1) * deg[second] +
          t[second] / (deg[second] + 2) * (deg[second] + 1) -
          t[first] / (deg[first] + 2);
      p = lower_bound(b + 1, b + m + 1, make_pair(a[second], second)) - b;
      change1(0, p, p, w);
      p = lower_bound(b + 1, b + m + 1, make_pair(second, first)) - b;
      long long v = query(0, p) - t[second] / (deg[second] + 1);
      change2(0, p, inf, -inf);
      deg[second]--;
      deg[z]++;
      w = t[z] / (deg[z] + 2) - t[z] / (deg[z] + 1);
      change1(0, l[z], r[z], w);
      p = lower_bound(b + 1, b + m + 1, make_pair(a[a[z]], a[z])) - b;
      change1(0, p, p, w);
      w = -t[z] / (deg[z] + 2) * (deg[z] + 1) + t[z] / (deg[z] + 1) * deg[z] +
          t[first] / (deg[first] + 2);
      p = lower_bound(b + 1, b + m + 1, make_pair(a[z], z)) - b;
      change1(0, p, p, w);
      v += t[z] / (deg[z] + 2);
      p = lower_bound(b + 1, b + m + 1, make_pair(z, first)) - b;
      change2(0, p, v, v);
      a[first] = z;
    }
    if (op[i] == 2)
      printf("%I64d\n", query(0, lower_bound(b + 1, b + m + 1,
                                             make_pair(a[c[i][0]], c[i][0])) -
                                     b));
    if (op[i] == 3) printf("%I64d %I64d\n", tree[0].mi, tree[0].ma);
  }
  return 0;
}
