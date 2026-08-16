#include <bits/stdc++.h>
using namespace std;
const long long INF = 1ll << 60;
long long n, m, Max[500010], d[500010], L[500010], R[500010], ans[500010];
long long ver[1000010], edge[1000010], Next[1000010], head[500010], tot;
vector<long long> q[500010];
struct SegmentTree {
  long long l, r, Min, lazy;
} tree[500010 << 2];
inline long long read() {
  long long x = 0, tmp = 1;
  char ch = getchar();
  while (!isdigit(ch)) {
    if (ch == '-') tmp = -1;
    ch = getchar();
  }
  while (isdigit(ch)) {
    x = (x << 3) + (x << 1) + (ch ^ 48);
    ch = getchar();
  }
  return tmp * x;
}
inline void write(long long x) {
  if (x < 0) {
    putchar('-');
    x = -x;
  }
  long long y = 10, len = 1;
  while (y <= x) {
    y = (y << 3) + (y << 1);
    len++;
  }
  while (len--) {
    y /= 10;
    putchar(x / y + 48);
    x %= y;
  }
}
inline void addEdge(long long x, long long y, long long z) {
  ver[++tot] = y;
  edge[tot] = z;
  Next[tot] = head[x];
  head[x] = tot;
}
void dfs1(long long x) {
  Max[x] = x;
  for (long long i = head[x]; i; i = Next[i]) {
    long long y = ver[i], z = edge[i];
    d[y] = d[x] + z;
    dfs1(y);
    Max[x] = max(Max[x], Max[y]);
  }
}
inline void pushup(long long p) {
  tree[p].Min = min(tree[p << 1].Min, tree[p << 1 | 1].Min);
}
inline void pushdown(long long p) {
  if (tree[p].lazy) {
    tree[p << 1].Min += tree[p].lazy;
    tree[p << 1].lazy += tree[p].lazy;
    tree[p << 1 | 1].Min += tree[p].lazy;
    tree[p << 1 | 1].lazy += tree[p].lazy;
    tree[p].lazy = 0;
  }
}
void build(long long p, long long l, long long r) {
  tree[p].l = l;
  tree[p].r = r;
  if (l == r) return;
  long long mid = (l + r) >> 1;
  build(p << 1, l, mid);
  build(p << 1 | 1, mid + 1, r);
}
void update(long long p, long long l, long long r, long long val) {
  if (l <= tree[p].l && tree[p].r <= r) {
    tree[p].Min += val;
    tree[p].lazy += val;
    return;
  }
  pushdown(p);
  long long mid = (tree[p].l + tree[p].r) >> 1;
  if (l <= mid) update(p << 1, l, r, val);
  if (r > mid) update(p << 1 | 1, l, r, val);
  pushup(p);
}
long long query(long long p, long long l, long long r) {
  if (l <= tree[p].l && tree[p].r <= r) return tree[p].Min;
  pushdown(p);
  long long mid = (tree[p].l + tree[p].r) >> 1, ans = INF;
  if (l <= mid) ans = min(ans, query(p << 1, l, r));
  if (r > mid) ans = min(ans, query(p << 1 | 1, l, r));
  return ans;
}
void dfs2(long long x) {
  for (long long i : q[x]) ans[i] = query(1, L[i], R[i]);
  for (long long i = head[x]; i; i = Next[i]) {
    long long y = ver[i], z = edge[i];
    update(1, 1, n, z);
    update(1, y, Max[y], -2 * z);
    dfs2(y);
    update(1, 1, n, -z);
    update(1, y, Max[y], 2 * z);
  }
}
int main() {
  n = read();
  m = read();
  for (long long i = 2; i <= n; i++) {
    long long y = read(), z = read();
    addEdge(y, i, z);
  }
  dfs1(1);
  build(1, 1, n);
  for (long long i = 1; i <= n; i++) update(1, i, i, i == Max[i] ? d[i] : INF);
  for (long long i = 1; i <= m; i++) {
    long long x = read();
    L[i] = read();
    R[i] = read();
    q[x].push_back(i);
  }
  dfs2(1);
  for (long long i = 1; i <= m; i++) {
    write(ans[i]);
    putchar('\n');
  }
  return 0;
}
