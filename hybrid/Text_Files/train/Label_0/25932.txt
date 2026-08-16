#include <bits/stdc++.h>
using namespace std;
const int maxn = 150001;
struct BIT {
  int bit[maxn];
  BIT() { memset(bit, 0, sizeof(bit)); }
  void add(int x, int v) {
    for (x++; x < maxn; x += x & -x) bit[x] += v;
  }
  void add(int a, int b, int v) { add(a, 1), add(b + 1, -1); }
  int qry(int x) {
    int ret = 0;
    for (x++; x; x -= x & -x) ret += bit[x];
    return ret;
  }
};
struct segTree {
  int l, r;
  segTree *left = 0, *right = 0;
  int val = 0;
  segTree(int a, int b) : l(a), r(b){};
  void add(int x, int v) {
    if (l == r) {
      val += v;
      return;
    }
    int mid = (l + r) / 2;
    if (x <= mid) {
      if (!left) left = new segTree(l, mid);
      left->add(x, v);
    } else {
      if (!right) right = new segTree(mid + 1, r);
      right->add(x, v);
    }
    val = (left ? left->val : 0) + (right ? right->val : 0);
  }
  void mrg(segTree *tre) {
    if (!tre) return;
    if (!left)
      left = tre->left;
    else if (tre->left)
      left->mrg(tre->left);
    if (!right)
      right = tre->right;
    else if (tre->right)
      right->mrg(tre->right);
    val += tre->val;
    delete tre;
  }
  int qry(int a, int b) {
    if (a <= l && r <= b) return val;
    int ret = 0, mid = (l + r) / 2;
    if (a <= mid && b >= l && left) ret += left->qry(a, b);
    if (b > mid && a <= r && right) ret += right->qry(a, b);
    return ret;
  }
  void clear() {
    if (left) left->clear();
    if (right) right->clear();
    delete this;
  }
};
const int w = 18;
int n, m, k;
int q[maxn][2];
int p[w][maxn];
int d[maxn], sz[maxn], h[maxn], l[maxn], r[maxn];
vector<int> graph[maxn], v[maxn], v2[maxn];
BIT bit;
segTree *tre[maxn];
int dfsh(int c) {
  sz[c] = 1, h[c] = -1;
  for (int i = 1; i < w; i++) {
    p[i][c] = ~p[i - 1][c] ? p[i - 1][p[i - 1][c]] : -1;
  }
  for (int i : graph[c]) {
    if (i == p[0][c]) continue;
    p[0][i] = c;
    d[i] = d[c] + 1;
    sz[c] += dfsh(i);
    if (!~h[c] || sz[i] > sz[h[c]]) h[c] = i;
  }
  return sz[c];
}
int dfsh2(int c) {
  r[c] = l[c];
  for (int i : graph[c]) {
    if (i == p[0][c] || i == h[c]) continue;
    l[i] = r[c] + 1;
    r[c] = dfsh2(i);
  }
  if (~h[c]) {
    l[h[c]] = r[c] + 1;
    r[c] = dfsh2(h[c]);
  }
  return r[c];
}
int lft(int c, int x) {
  for (int i = 0; i < w; i++) {
    if (((x >> i) & 1) && ~c) c = p[i][c];
  }
  return c;
}
int lca(int x, int y) {
  if (d[x] < d[y]) swap(x, y);
  x = lft(x, d[x] - d[y]);
  for (int i = w - 1; ~i; i--) {
    if (p[i][x] != p[i][y]) x = p[i][x], y = p[i][y];
  }
  return x == y ? x : p[0][x];
}
long long dfs2(int c, int rt) {
  long long ret = 0;
  tre[c] = new segTree(0, n - 1);
  for (int i : v2[c]) {
    int dd = max(0, k + d[rt] - d[q[i][0]]);
    int j = q[i][1];
    if (d[j] - d[rt] >= dd) {
      j = lft(j, d[j] - d[rt] - dd);
      ret += tre[c]->qry(l[j], r[j]);
    }
    tre[c]->add(l[q[i][1]], 1);
  }
  for (int i : graph[c]) {
    if (i == p[0][c] || (c == rt && i == h[c])) continue;
    ret += dfs2(i, rt);
    if (v2[c].size() < v2[i].size()) {
      swap(v2[c], v2[i]);
      swap(tre[c], tre[i]);
    }
    for (int it : v2[i]) {
      int dd = max(0, k + d[rt] - d[c]);
      int j = q[it][1];
      if (d[j] - d[rt] >= dd) {
        j = lft(j, d[j] - d[rt] - dd);
        ret += tre[c]->qry(l[j], r[j]);
      }
      v2[c].push_back(it);
    }
    v2[i].clear();
    tre[c]->mrg(tre[i]);
  }
  return ret;
}
long long dfs(int c) {
  long long ret = 0;
  for (int i : graph[c])
    if (i != p[0][c]) ret += dfs(i);
  for (int t = 0; t < 2; t++) {
    for (int i : v[c]) ret += bit.qry(l[q[i][t]]);
    for (int i : v[c]) {
      int j = q[i][t];
      if (d[j] - d[c] >= k) {
        j = lft(j, d[j] - d[c] - k);
        bit.add(l[j], r[j], 1);
      }
      if (!t) v2[q[i][t]].push_back(i);
    }
  }
  ret += dfs2(c, c);
  v2[c].clear();
  tre[c]->clear();
  return ret;
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m >> k;
  for (int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--, v--;
    graph[u].push_back(v);
    graph[v].push_back(u);
  }
  p[0][0] = -1;
  dfsh(0), dfsh2(0);
  for (int i = 0; i < m; i++) {
    cin >> q[i][0] >> q[i][1];
    q[i][0]--, q[i][1]--;
    if (l[q[i][0]] > l[q[i][1]]) swap(q[i][0], q[i][1]);
    v[lca(q[i][0], q[i][1])].push_back(i);
  }
  cout << dfs(0) << '\n';
  return 0;
}
