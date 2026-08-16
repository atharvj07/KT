#include <bits/stdc++.h>
using namespace std;
template <class S, class T>
istream& operator>>(istream& is, pair<S, T>& p) {
  return is >> p.first >> p.second;
}
const double EPS = 1e-10;
const double PI = acos(-1.0);
const long long MOD = 1e9 + 7;
vector<int> G[400000];
int par[400000];
int sz[400000];
int N;
void init(int u, int p = -1) {
  sz[u] = 1;
  par[u] = p;
  for (int to : G[u]) {
    if (to == p) continue;
    init(to, u);
    sz[u] += sz[to];
  }
}
int cent(int u) {
  bool ok = true;
  for (int to : G[u]) {
    if (to == par[u]) continue;
    if (sz[to] > N / 2) ok = false;
  }
  ok = ok && (N - sz[u] <= N / 2);
  if (ok) return u;
  int res = -1;
  for (int to : G[u]) {
    if (to == par[u]) continue;
    res = cent(to);
    if (res != -1) break;
  }
  return res;
}
int ans[400000];
void dfs(int u, int p, int ix, int c) {
  if (ix > 0)
    ans[u] = N - sz[u] - sz[G[c][0]] <= N / 2;
  else
    ans[u] = (N - sz[G[c][0]] <= N / 2) ||
             (N - sz[u] - (int((G[c]).size()) > 1 ? sz[G[c][1]] : 0) <= N / 2);
  for (int to : G[u]) {
    if (to == p) continue;
    dfs(to, u, ix, c);
  }
}
int main() {
  cin.tie(0);
  ios_base::sync_with_stdio(false);
  cin >> N;
  for (int i = (0); i < (N - 1); ++i) {
    int u, v;
    cin >> u >> v;
    --u;
    --v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  init(0);
  int c = cent(0);
  init(c);
  ans[c] = 1;
  sort((G[c]).begin(), (G[c]).end(),
       [&](int i, int j) { return sz[i] > sz[j]; });
  for (int i = (0); i < (int((G[c]).size())); ++i) {
    dfs(G[c][i], c, i, c);
  }
  for (int i = (0); i < (N); ++i) cout << (i ? " " : "") << ans[i];
  cout << endl;
  return 0;
}
