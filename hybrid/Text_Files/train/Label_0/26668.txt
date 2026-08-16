#include <bits/stdc++.h>
using namespace std;
int n, m;
long long w[2222];
long long b[2222];
long long maxW;
vector<int> G[2222];
int cn;
vector<int> lst[2222];
long long gb[2222], gw[2222];
int mark[2222];
void bfs(int x) {
  queue<int> Q;
  Q.push(x);
  mark[x] = cn;
  while (!Q.empty()) {
    int u = Q.front();
    Q.pop();
    gb[cn] += b[u];
    gw[cn] += w[u];
    lst[cn].push_back(u);
    for (auto v : G[u]) {
      if (mark[v] == 0) {
        Q.push(v);
        mark[v] = cn;
      }
    }
  }
}
long long dp[2222][2222];
long long f(int p, long long rem) {
  if (p > cn) {
    return 0;
  }
  if (rem <= 0) {
    return 0;
  }
  if (dp[p][rem] != -1) {
    return dp[p][rem];
  }
  dp[p][rem] = 0;
  long long ret = f(p + 1, rem);
  if (gw[p] <= rem) {
    ret = max(ret, f(p + 1, rem - gw[p]) + gb[p]);
  }
  for (auto u : lst[p]) {
    if (w[u] <= rem) {
      ret = max(ret, b[u] + f(p + 1, rem - w[u]));
    }
  }
  return dp[p][rem] = ret;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> m >> maxW;
  for (int i = 1; i <= n; i++) {
    cin >> w[i];
  }
  for (int i = 1; i <= n; i++) {
    cin >> b[i];
  }
  for (int i = 0; i <= n; i++) {
    G[i].clear();
    lst[i].clear();
  }
  for (int i = 1, u, v; i <= m; i++) {
    cin >> u >> v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  cn = 0;
  memset(gb, 0, sizeof(gb));
  memset(gw, 0, sizeof(gw));
  memset(mark, 0, sizeof(mark));
  for (int i = 1; i <= n; i++) {
    if (mark[i] == 0) {
      cn++;
      bfs(i);
    }
  }
  memset(dp, -1, sizeof(dp));
  long long ans = f(1, maxW);
  cout << ans << "\n";
  return 0;
}
