#include <bits/stdc++.h>
#pragma GCC optimize("Ofast,unroll-loops")
using namespace std;
const int N = 1e6 + 2;
vector<int> adj[N];
int k, ans = 1;
int dfs(int u, int pai = -1) {
  bool leaf = true;
  vector<int> deps;
  for (int v : adj[u]) {
    if (v == pai) continue;
    int depth = dfs(v, u) + 1;
    deps.push_back(depth);
    leaf = false;
  }
  if (leaf) return 0;
  sort(deps.begin(), deps.end());
  while (int(deps.size()) > 1) {
    int a = deps[int(deps.size()) - 1], b = deps[int(deps.size()) - 2];
    if (a + b <= k) return a;
    ans++;
    deps.pop_back();
  }
  return deps[0];
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n;
  cin >> n >> k;
  for (int i = 0; i < n - 1; ++i) {
    int a, b;
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }
  int root;
  for (int i = 1; i <= n; ++i) {
    if (int(adj[i].size()) != 1) root = i;
  }
  dfs(root);
  cout << ans << endl;
  return 0;
}
