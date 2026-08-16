#include <bits/stdc++.h>
using namespace std;
int dp[83][83][83][83];
vector<pair<int, int> > adj[103];
int n, k, m;
const int inf = 1e9;
int f(int nw, int baki, int l, int r) {
  if (baki == 0) return 0;
  if (dp[nw][baki][l][r] != (-1)) return dp[nw][baki][l][r];
  int ret = inf;
  for (pair<int, int> x : adj[nw]) {
    int v = x.first;
    int w = x.second;
    if (v <= l || v >= r) continue;
    if (v == nw) continue;
    if (v > nw) {
      ret = min(ret, w + f(v, baki - 1, nw, r));
    } else {
      ret = min(ret, w + f(v, baki - 1, l, nw));
    }
  }
  return dp[nw][baki][l][r] = ret;
}
int main() {
  memset(dp, -1, sizeof dp);
  cin >> n >> k >> m;
  while (m--) {
    int u, v, w;
    cin >> u >> v >> w;
    adj[u].push_back(make_pair(v, w));
  }
  int ses = inf;
  for (int i = 1; i <= n; i++) {
    ses = min(ses, f(i, k - 1, 0, n + 1));
  }
  if (ses >= inf) ses = -1;
  cout << ses << endl;
  return 0;
}
