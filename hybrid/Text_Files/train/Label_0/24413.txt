#include <bits/stdc++.h>
#pragma GCC optimize("O2")
#pragma GCC optimize("unroll-loops")
using namespace std;
const long double eps = 1e-7;
const int inf = 1000000010;
const long long INF = 10000000000000010LL;
const int mod = 1000000007;
const int MAXN = 200010, LOG = 20;
int n, m, k, u, v, x, y, t, a, b, ans;
int A[MAXN], g[MAXN];
int val[MAXN];
int mark[MAXN];
vector<int> G[MAXN], topol;
void dfs(int node) {
  mark[node] = 1;
  for (int v : G[node])
    if (!mark[v]) dfs(v);
  topol.push_back(node);
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> m;
  for (int i = 1; i <= n; i++) cin >> A[i];
  while (m--) {
    cin >> u >> v;
    G[u].push_back(v);
  }
  for (int v = 1; v <= n; v++)
    if (!mark[v]) dfs(v);
  memset(mark, 0, sizeof(mark));
  for (int v : topol) {
    for (int u : G[v]) mark[g[u]] = v;
    while (mark[g[v]] == v) g[v]++;
    val[g[v]] ^= A[v];
  }
  for (int i = n; ~i; i--)
    if (val[i]) {
      for (int v = 1; v <= n; v++)
        if (g[v] == i && (A[v] ^ val[i]) < A[v]) {
          A[v] ^= val[i];
          for (int u : G[v]) {
            A[u] ^= val[g[u]];
            val[g[u]] = 0;
          }
          break;
        }
      cout << "WIN\n";
      for (int v = 1; v <= n; v++) cout << A[v] << ' ';
      cout << '\n';
      return 0;
    }
  cout << "LOSE\n";
  return 0;
}
