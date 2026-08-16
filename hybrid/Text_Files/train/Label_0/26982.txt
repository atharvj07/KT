#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5, Mod = 1e9 + 7, MAXN = 1e5, Lg = 27, M = 1e7 + 10,
          P = 727, Sq = 320;
const long long inf = 3e18 + 10;
int seg[4 * N], lz[4 * N], Par[N][Lg], St[N], Ed[N], H[N], Ans[N], Tim = 1, n,
                                                                   q;
vector<int> Adj[N];
vector<pair<int, int> > Q[N];
inline void Shift(int s, int e, int ind) {
  int x = lz[ind];
  seg[(2 * (ind))] += x, seg[((2 * (ind)) + 1)] += x, lz[(2 * (ind))] += x,
      lz[((2 * (ind)) + 1)] += x;
  lz[ind] = 0;
}
void Add(int s, int e, int ind, int l, int r, int x) {
  if (s >= l && e <= r) {
    seg[ind] += x, lz[ind] += x;
    return;
  }
  Shift(s, e, ind);
  int mid = (s + e) / 2;
  if (l < mid) Add(s, mid, (2 * (ind)), l, r, x);
  if (r > mid) Add(mid, e, ((2 * (ind)) + 1), l, r, x);
  seg[ind] = max(seg[(2 * (ind))], seg[((2 * (ind)) + 1)]);
}
int Max(int s, int e, int ind, int l, int r) {
  if (s >= l && e <= r) return seg[ind];
  Shift(s, e, ind);
  int mid = (s + e) / 2, ret = -Mod;
  if (l < mid) ret = max(ret, Max(s, mid, (2 * (ind)), l, r));
  if (r > mid) ret = max(ret, Max(mid, e, ((2 * (ind)) + 1), l, r));
  return ret;
}
void Dfs(int u, int par) {
  Par[u][0] = par;
  for (int i = 1; i < Lg; i++) Par[u][i] = Par[Par[u][i - 1]][i - 1];
  St[u] = Tim++;
  Add(1, N, 1, St[u], St[u] + 1, H[u]);
  for (int i = 0; i < (int)Adj[u].size(); i++) {
    int x = Adj[u][i];
    if (x == par) continue;
    H[x] = H[u] + 1;
    Dfs(x, u);
  }
  Ed[u] = Tim;
}
inline int Find(int u, int x) {
  while (x) {
    int ct = __builtin_ctz(x);
    u = Par[u][ct];
    x = (x ^ (1 << ct));
  }
  return u;
}
inline int Lca(int u, int v) {
  if (H[u] > H[v]) swap(u, v);
  v = Find(v, H[v] - H[u]);
  if (u == v) return u;
  for (int i = Lg - 1; i >= 0; i--)
    if (Par[u][i] != Par[v][i]) u = Par[u][i], v = Par[v][i];
  return Par[u][0];
}
inline void Recalc(int x, int y) {
  if (St[x] < St[y]) {
    Add(1, N, 1, St[y], Ed[y], -1);
    if (St[y] > 1) Add(1, N, 1, 1, St[y], 1);
    if (Ed[y] < N) Add(1, N, 1, Ed[y], N, 1);
  } else {
    Add(1, N, 1, St[x], Ed[x], 1);
    if (St[x] > 1) Add(1, N, 1, 1, St[x], -1);
    if (Ed[x] < N) Add(1, N, 1, Ed[x], N, -1);
  }
}
void Solve(int u, int par) {
  for (int i = 0; i < (int)Q[u].size(); i++) {
    int x = Q[u][i].first, y = u, lc = Lca(x, y),
        dis = (H[x] + H[y]) - 2 * (H[lc]) - 1, ret = 0;
    int cur = (dis / 2), nxt = 0;
    if (u > x) cur = (dis + 1) / 2;
    if (H[u] < H[x] || (H[u] == H[x] && u > x)) {
      nxt = Find(x, dis - cur);
      if (St[nxt] > 1) ret = max(ret, Max(1, N, 1, 1, St[nxt]));
      if (Ed[nxt] < N) ret = max(ret, Max(1, N, 1, Ed[nxt], n + 1));
    } else {
      nxt = Find(u, cur);
      ret = max(ret, Max(1, N, 1, St[nxt], Ed[nxt]));
    }
    Ans[Q[u][i].second] = max(Ans[Q[u][i].second], ret);
  }
  for (int i = 0; i < (int)Adj[u].size(); i++) {
    int x = Adj[u][i];
    if (x == par) continue;
    Recalc(u, x);
    Solve(x, u);
    Recalc(x, u);
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n - 1; i++) {
    int x, y;
    scanf("%d%d", &x, &y);
    Adj[x].push_back(y), Adj[y].push_back(x);
  }
  for (int i = 0; i < Lg; i++) Par[1][i] = 1;
  Dfs(1, 1);
  scanf("%d", &q);
  for (int i = 1; i <= q; i++) {
    int x, y;
    scanf("%d%d", &x, &y);
    Q[x].push_back(make_pair(y, i));
    Q[y].push_back(make_pair(x, i));
  }
  Solve(1, 1);
  for (int i = 1; i <= q; i++) printf("%d\n", Ans[i]);
  return 0;
}
