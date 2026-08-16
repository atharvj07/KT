#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 100, LOG = 20, MOD = 1000 * 1000 * 1000 + 7;
int sum(int a, int b) {
  a += b;
  if (a >= MOD)
    a -= MOD;
  else if (a < 0)
    a += MOD;
  return a;
}
void _sum(int &a, int b) {
  a += b;
  if (a >= MOD)
    a -= MOD;
  else if (a < 0)
    a += MOD;
}
int mul(int a, int b) { return 1LL * a * b % MOD; }
int n, u, v, w, q, h[N], sz[N], sum_down[N], sq_down[N], sq_up[N][LOG];
pair<int, int> upper[N][LOG], sum_up[N][LOG];
vector<pair<int, int> > nei[N];
int lca(int u, int v) {
  if (h[u] < h[v]) swap(u, v);
  for (int i = LOG - 1; i >= 0; i--)
    if (h[u] - (1 << i) >= h[v]) u = upper[u][i].first;
  if (u == v) return u;
  for (int i = LOG - 1; i >= 0; i--)
    if (upper[u][i].first != upper[v][i].first) {
      u = upper[u][i].first;
      v = upper[v][i].first;
    }
  return upper[u][0].first;
}
bool under(int u, int v) { return lca(u, v) == v; }
int dis(int u, int v) {
  int res = 0;
  for (int i = LOG - 1; i >= 0; i--)
    if (h[u] - (1 << i) >= h[v]) {
      _sum(res, upper[u][i].second);
      u = upper[u][i].first;
    }
  return res;
}
int get_sq(int u, int v) {
  int res = 0, len = 0;
  for (int i = LOG - 1; i >= 0; i--)
    if (h[u] - (1 << i) >= h[v]) {
      _sum(res, sq_up[u][i]);
      _sum(res, mul(len, sum(mul(len, sum_up[u][i].second),
                             mul(2, sum_up[u][i].first))));
      _sum(len, upper[u][i].second);
      u = upper[u][i].first;
    }
  return res;
}
void dfs_down(int v, int par = 0) {
  for (int i = 1; i < LOG; i++) {
    pair<int, int> p1 = upper[v][i - 1], p2 = upper[p1.first][i - 1];
    upper[v][i] = pair<int, int>(p2.first, sum(p1.second, p2.second));
  }
  int SUM = 0, SQ = 0, SZ = 0;
  for (pair<int, int> p : nei[v])
    if (p.first != par) {
      int u = p.first, d = p.second;
      upper[u][0] = pair<int, int>(v, d);
      h[u] = h[v] + 1;
      dfs_down(u, v);
      SZ += sz[u];
      _sum(SUM, sum(sum_down[u], mul(sz[u], d)));
      _sum(SQ,
           sum(sq_down[u], mul(d, sum(mul(d, sz[u]), mul(2, sum_down[u])))));
    }
  sz[v] = sum(SZ, 1);
  sum_down[v] = SUM;
  sq_down[v] = SQ;
}
void dfs_up(int v, int par = 0) {
  for (int i = 1; i < LOG; i++) {
    int u = upper[v][i - 1].first, d = upper[v][i - 1].second,
        SZ = sum_up[u][i - 1].second;
    sum_up[v][i].first =
        sum(sum_up[v][i - 1].first, sum(sum_up[u][i - 1].first, mul(SZ, d)));
    sum_up[v][i].second = sum(sum_up[v][i - 1].second, SZ);
    sq_up[v][i] =
        sum(sq_up[v][i - 1],
            sum(sq_up[u][i - 1],
                mul(d, sum(mul(SZ, d), mul(2, sum_up[u][i - 1].first)))));
  }
  for (pair<int, int> p : nei[v])
    if (p.first != par) {
      int u = p.first, d = p.second;
      sum_up[u][0].first =
          sum(sum_down[v],
              sum(-mul(d, sz[u]), sum(-sum_down[u], mul(sz[v] - sz[u], d))));
      sum_up[u][0].second = sz[v] - sz[u];
      sq_up[u][0] = sum(
          sq_down[v],
          -sum(sq_down[u], mul(d, sum(mul(d, sz[u]), mul(2, sum_down[u])))));
      _sum(sq_up[u][0], mul(d, sum(mul(d, sum_up[u][0].second),
                                   mul(2, sum(sum_up[u][0].first,
                                              -mul(d, sum_up[u][0].second))))));
      dfs_up(u, v);
    }
}
int main() {
  ios::sync_with_stdio(false), cin.tie(0);
  cin >> n;
  for (int i = 0; i < n - 1; i++) {
    cin >> u >> v >> w;
    nei[--u].push_back(pair<int, int>(--v, w));
    nei[v].push_back(pair<int, int>(u, w));
  }
  dfs_down(0);
  dfs_up(0);
  cin >> q;
  while (q--) {
    cin >> u >> v;
    u--, v--;
    int ans = sum(sq_down[u], get_sq(u, 0)), LCA = lca(u, v),
        d = sum(dis(v, LCA), dis(u, LCA));
    if (under(u, v))
      _sum(ans, -mul(2, sum(get_sq(u, v), sq_down[u])));
    else
      _sum(ans, -mul(2, sum(sq_down[v],
                            mul(d, sum(mul(d, sz[v]), mul(2, sum_down[v]))))));
    ans = (-ans + MOD) % MOD;
    cout << ans << '\n';
  }
  return 0;
}
