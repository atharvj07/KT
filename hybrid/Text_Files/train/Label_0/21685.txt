#include <bits/stdc++.h>
using namespace std;
const int N = 300005;
set<int> s[N];
int n, q, i, j, k, x, y, z, head[N], adj[N * 2], nxt[N * 2], size[N], id[N],
    dep[N], p[N][25], mark[N * 5], num[N * 5];
void update(int o, int l, int r, int x, int y) {
  if (l == x && r == y) {
    mark[o] += z;
    if (mark[o])
      num[o] = y - x + 1;
    else
      num[o] = num[o << 1] + num[o << 1 | 1];
    return;
  }
  int mid = l + r >> 1;
  if (y <= mid)
    update(o << 1, l, mid, x, y);
  else if (x > mid)
    update(o << 1 | 1, mid + 1, r, x, y);
  else
    update(o << 1, l, mid, x, mid), update(o << 1 | 1, mid + 1, r, mid + 1, y);
  num[o] = (mark[o] ? r - l + 1 : num[o << 1] + num[o << 1 | 1]);
}
void dfs(int x, int dad) {
  id[x] = ++k;
  size[x] = 1;
  for (int y = head[x]; y; y = nxt[y])
    if (adj[y] != dad) {
      dep[adj[y]] = dep[x] + 1;
      p[adj[y]][0] = x;
      dfs(adj[y], x);
      size[x] += size[adj[y]];
    }
}
int lca(int a, int b) {
  int c, d;
  if (dep[a] < dep[b]) swap(a, b);
  for (c = dep[a] - dep[b], d = 0; c; c >>= 1, ++d)
    if (c & 1) a = p[a][d];
  if (a == b) return a;
  for (c = 20; c >= 0; --c)
    if (p[a][c] != p[b][c]) a = p[a][c], b = p[b][c];
  return p[a][0];
}
int main() {
  scanf("%d%d", &n, &q);
  for (i = 1; i < n; ++i) {
    scanf("%d%d", &j, &k);
    adj[i * 2 - 1] = k;
    nxt[i * 2 - 1] = head[j];
    head[j] = i * 2 - 1;
    adj[i * 2] = j;
    nxt[i * 2] = head[k];
    head[k] = i * 2;
  }
  k = 0;
  dfs(1, -1);
  for (i = 1; (1 << i) < n; ++i)
    for (j = 1; j <= n; ++j)
      if (p[j][i - 1]) p[j][i] = p[p[j][i - 1]][i - 1];
  while (q--) {
    scanf("%d%d", &i, &j);
    if (p[i][0] == j || p[j][0] == i) continue;
    if (id[i] > id[j]) swap(i, j);
    if (s[i].count(j)) {
      s[i].erase(j);
      s[j].erase(i);
      z = -1;
    } else {
      s[i].insert(j);
      x = y = 1;
      s[j].insert(i);
      z = 1;
    }
    if (lca(i, j) == i) {
      for (k = dep[j] - dep[i] - 1, x = 0, y = j; k; k >>= 1, ++x)
        if (k & 1) y = p[y][x];
      k = y;
      x = id[k], y = id[j] - 1;
      if (x <= y) update(1, 1, n, x, y);
      x = id[j] + size[j], y = id[k] + size[k] - 1;
      if (x <= y && y <= n) update(1, 1, n, x, y);
    } else {
      x = 1, y = id[i] - 1;
      if (x <= y) update(1, 1, n, x, y);
      x = id[i] + size[i], y = id[j] - 1;
      if (x <= y) update(1, 1, n, x, y);
      x = id[j] + size[j], y = n;
      if (x <= y) update(1, 1, n, x, y);
    }
    printf("%d\n", n - num[1]);
  }
  return 0;
}
