#include <bits/stdc++.h>
using namespace std;
const int MAX_N = 1e5 + 1;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const long long LINF = 1e18;
vector<int> adj[200006], component;
vector<bool> visited(200006, false);
void dfs(int u) {
  visited[u] = true;
  component.push_back(u);
  for (auto i : adj[u]) {
    if (!visited[i]) {
      dfs(i);
    }
  }
}
void solve() {
  for (int i = 0; i < 200006; i++) visited[i] = false, adj[i].clear();
  int n;
  cin >> n;
  vector<int> ans(n + 1);
  for (int i = 1; i <= n; i++) {
    int key;
    cin >> key;
    adj[key].push_back(i);
    adj[i].push_back(key);
  }
  for (int i = 1; i <= n; i++) {
    if (!visited[i]) {
      dfs(i);
      for (auto j : component) {
        ans[j] = component.size();
      }
      component.clear();
    }
  }
  for (int i = 1; i <= n; i++) cout << ans[i] << " ";
  cout << "\n";
  component.clear();
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int tc = 1;
  cin >> tc;
  for (int t = 1; t <= tc; t++) {
    solve();
  }
  return 0;
}
