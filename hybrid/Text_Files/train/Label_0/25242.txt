#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 1;
struct my {
  int first, second, col, hld;
} b[N];
int l = 1, C = 1, tin[N], tout[N], timer, n, m, first, second, z, up[N][25],
    d[N], sz[N], s, v, ans[N];
pair<int, int> pred[N];
vector<pair<int, int> > a[N];
vector<int> tree[N], hld[N];
void dfs(int v, int pr = 0) {
  tin[v] = ++timer;
  up[v][0] = pr;
  for (int i = 1; i <= l; ++i) up[v][i] = up[up[v][i - 1]][i - 1];
  for (int i = 0; i < a[v].size(); ++i) {
    int to = a[v][i].first;
    if (to == pr) continue;
    pred[to] = make_pair(v, a[v][i].second);
    dfs(to, v);
    d[v] += d[to] + 1;
  }
  tout[v] = ++timer;
}
bool upper(int a, int b) { return (tin[a] <= tin[b] && tout[a] >= tout[b]); }
int lca(int a, int b) {
  if (upper(a, b)) return a;
  if (upper(b, a)) return b;
  for (int i = l; i >= 0; --i)
    if (up[a][i] != 0 && !upper(up[a][i], b)) a = up[a][i];
  return up[a][0];
}
void update(int level, int v, int l, int r, int L, int R) {
  if (r < L || l > R) return;
  if (l >= L && r <= R) {
    ++tree[level][v];
    return;
  }
  int mid = (l + r) >> 1;
  update(level, v + v, l, mid, L, R);
  update(level, v + v + 1, mid + 1, r, L, R);
}
void dfs2(int v, int pr = 0, int c = 1) {
  pair<int, int> z = make_pair(0, 0);
  for (int i = 0; i < a[v].size(); ++i) {
    pair<int, int> to = a[v][i];
    if (to.first == pr) continue;
    if (b[to.second].first != v) swap(b[to.second].first, b[to.second].second);
    if (d[to.first] >= d[z.first]) z = to;
  }
  if (!z.first) return;
  hld[C].push_back(z.second);
  b[z.second].col = C;
  b[z.second].hld = hld[C].size() - 1;
  dfs2(z.first, v, c);
  for (int i = 0; i < a[v].size(); ++i) {
    pair<int, int> to = a[v][i];
    if (to.first == pr || to.first == z.first) continue;
    C++;
    hld[C].push_back(to.second);
    b[to.second].col = C;
    b[to.second].hld = 0;
    dfs2(to.first, v, C);
  }
}
void solve(int first, int second) {
  int v = first;
  for (int i = l; i >= 0; --i)
    if (up[v][i] != 0 && !upper(up[v][i], second)) v = up[v][i];
  int f = pred[v].second, s = pred[first].second;
  while (b[s].col != b[f].col) {
    update(b[s].col, 1, 1, sz[b[s].col], 1, b[s].hld + 1);
    s = pred[b[hld[b[s].col][0]].first].second;
  }
  update(b[s].col, 1, 1, sz[b[s].col], b[f].hld + 1, b[s].hld + 1);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 1; i < n; ++i) {
    cin >> b[i].first >> b[i].second;
    first = b[i].first, second = b[i].second;
    a[first].push_back(make_pair(second, i));
    a[second].push_back(make_pair(first, i));
  }
  while ((1 << l) < n) ++l;
  dfs(1);
  dfs2(1);
  for (int i = 1; i <= C; ++i) {
    tree[i].resize(hld[i].size() << 2);
    sz[i] = 1;
    while (sz[i] < hld[i].size()) sz[i] <<= 1;
  }
  cin >> m;
  while (m--) {
    cin >> first >> second;
    z = lca(first, second);
    if (z != first) solve(first, z);
    if (z != second) solve(second, z);
  }
  for (int i = 1; i <= C; ++i)
    for (int j = 0; j < hld[i].size(); ++j) {
      s = 0, v = sz[i] + j;
      while (v) {
        s += tree[i][v];
        v >>= 1;
      }
      ans[hld[i][j]] = s;
    }
  for (int i = 1; i < n; ++i) printf("%d ", ans[i]);
}
