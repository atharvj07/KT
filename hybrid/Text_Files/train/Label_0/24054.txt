#include <bits/stdc++.h>
const int N = 1e5 + 7;
using namespace std;
int n, u, v, deg[N], child[N];
bool visited[N];
vector<int> adj[N];
void dfs(int u, int p) {
  child[u] = 1;
  for (int v : adj[u]) {
    if (!visited[v] && v != p) {
      dfs(v, u);
      child[u] += child[v];
    }
  }
}
int findcen(int u, int p, int sz) {
  for (int v : adj[u]) {
    if (v != p && !visited[v] && child[v] > sz / 2) {
      return findcen(v, u, sz);
    }
  }
  return u;
}
void centroid(int root, int degree) {
  dfs(root, root);
  int u = findcen(root, root, child[root]);
  deg[u] = degree;
  visited[u] = 1;
  for (int v : adj[u]) {
    if (!visited[v]) {
      centroid(v, degree + 1);
    }
  }
}
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n;
  for (int i = 1; i < n; ++i) {
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  centroid(1, 0);
  for (int i = 1; i <= n; ++i) {
    cout << (char)(deg[i] + 'A') << " ";
  }
}
