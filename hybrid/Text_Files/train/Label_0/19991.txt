#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 10;
const int MAXP = 5000010;
struct node {
  int value, lc, rc;
} a[MAXP];
int n, m, tot;
int rt[MAXN];
template <typename T>
inline void chkmax(T &x, T y) {
  x = max(x, y);
}
template <typename T>
inline void chkmin(T &x, T y) {
  x = min(x, y);
}
template <typename T>
inline void read(T &x) {
  T f = 1;
  x = 0;
  char c = getchar();
  for (; !isdigit(c); c = getchar())
    if (c == '-') f = -f;
  for (; isdigit(c); c = getchar()) x = (x << 3) + (x << 1) + c - '0';
  x *= f;
}
inline void update(int x) {
  a[x].value = max(a[a[x].lc].value, a[a[x].rc].value);
}
inline void modify(int &root, int l, int r, int x, int y) {
  if (!root) root = ++tot;
  if (l == r) {
    a[root].value = y;
    return;
  }
  int mid = (l + r) >> 1;
  if (mid >= x)
    modify(a[root].lc, l, mid, x, y);
  else
    modify(a[root].rc, mid + 1, r, x, y);
  update(root);
}
inline int query(int root, int l, int r, int ql, int qr) {
  if (!root) return 0;
  if (l == ql && r == qr) return a[root].value;
  int mid = (l + r) >> 1;
  if (mid >= qr)
    return query(a[root].lc, l, mid, ql, qr);
  else if (mid + 1 <= ql)
    return query(a[root].rc, mid + 1, r, ql, qr);
  else
    return max(query(a[root].lc, l, mid, ql, mid),
               query(a[root].rc, mid + 1, r, mid + 1, qr));
}
int main() {
  read(n);
  read(m);
  int ans = 0;
  for (int i = 1; i <= m; i++) {
    int u, v, w;
    read(u);
    read(v);
    read(w);
    ++w;
    int value = query(rt[u], 0, 100000, 0, w - 1) + 1;
    chkmax(ans, value);
    modify(rt[v], 0, 100000, w, value);
  }
  printf("%d\n", ans);
  return 0;
}
