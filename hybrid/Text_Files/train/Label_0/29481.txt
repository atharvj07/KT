#include <bits/stdc++.h>
using namespace std;
void solve() {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> g(n, vector<int>(n));
  while (m--) {
    int u, v;
    cin >> u >> v;
    --u, --v;
    g[u][v] = g[v][u] = 1;
  }
  auto bfs = [n, &g](int src, int trg, int t) -> int {
    vector<int> usd(n), dst(n, n);
    usd[src] = 1, dst[src] = 0;
    queue<int> q;
    q.push(src);
    while (!q.empty()) {
      int u = q.front();
      q.pop();
      if (u == trg) break;
      for (int v = 0; v < n; ++v) {
        if (g[u][v] == t && !usd[v]) {
          usd[v] = 1;
          dst[v] = dst[u] + 1;
          q.push(v);
        }
      }
    }
    return dst[trg];
  };
  int ans = bfs(0, n - 1, 1 - g[0][n - 1]);
  cout << (ans == n ? -1 : ans) << endl;
}
void init() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
}
int main() {
  init();
  solve();
  return 0;
}
