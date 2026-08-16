#include <bits/stdc++.h>
using namespace std;
int n, m, q;
struct T {
  int l, r, mid, mn, mx, v;
} t[200005 << 2];
inline void pushup(int rt) {
  t[rt].mn = min(t[(rt << 1)].mn, t[(rt << 1 | 1)].mn),
  t[rt].mx = max(t[(rt << 1)].mx, t[(rt << 1 | 1)].mx),
  t[rt].v = t[(rt << 1)].mn <= t[(rt << 1 | 1)].mx | t[(rt << 1)].v |
            t[(rt << 1 | 1)].v;
}
void build(int rt, int l, int r) {
  int mid = (l + r) >> 1;
  t[rt].mid = mid;
  t[rt].l = l, t[rt].r = r;
  if (l == r) return;
  build((rt << 1), l, mid), build((rt << 1 | 1), mid + 1, r);
}
void updateL(int rt, int x, int k) {
  if (t[rt].l == t[rt].r) {
    t[rt].mn = k, t[rt].v = k <= t[rt].mx;
    return;
  }
  if (x <= t[rt].mid)
    updateL((rt << 1), x, k);
  else
    updateL((rt << 1 | 1), x, k);
  pushup(rt);
}
void updateR(int rt, int x, int k) {
  if (t[rt].l == t[rt].r) {
    t[rt].mx = k, t[rt].v = t[rt].mn <= k;
    return;
  }
  if (x <= t[rt].mid)
    updateR((rt << 1), x, k);
  else
    updateR((rt << 1 | 1), x, k);
  pushup(rt);
}
set<pair<int, int> > s;
set<int> l[200005], r[200005];
inline int read() {
  int x = 0, f = 1;
  char ch = getchar();
  while (ch > '9' || ch < '0') {
    if (ch == '-') f = -1;
    ch = getchar();
    if (ch == -1) return 0;
  }
  while (ch >= '0' && ch <= '9') {
    x = x * 10 + ch - '0';
    ch = getchar();
  }
  return x * f;
}
inline void write(int x) {
  if (x < 0) {
    putchar('-');
    x = -x;
  }
  if (x >= 10) write(x / 10);
  putchar(x % 10 + '0');
}
int main() {
  n = read(), m = read(), q = read();
  build(1, 1, n);
  for (int i = 1; i <= n; i++)
    l[i].insert(m + 1), updateL(1, i, m + 1), r[i].insert(0), updateR(1, i, 0);
  while (q--) {
    int x, y;
    x = read(), y = read();
    if (s.count(make_pair(x, y))) {
      s.erase(make_pair(x, y));
      if (x & 1)
        l[(x + 1) >> 1].erase((y + 1) >> 1),
            updateL(1, (x + 1) >> 1, *l[(x + 1) >> 1].begin());
      else
        r[x >> 1].erase(y >> 1), updateR(1, x >> 1, *r[x >> 1].rbegin());
    } else {
      s.insert(make_pair(x, y));
      if (x & 1)
        l[(x + 1) >> 1].insert((y + 1) >> 1),
            updateL(1, (x + 1) >> 1, *l[(x + 1) >> 1].begin());
      else
        r[x >> 1].insert(y >> 1), updateR(1, x >> 1, *r[x >> 1].rbegin());
    }
    puts(t[1].v ? "NO" : "YES");
  }
  return 0;
}
