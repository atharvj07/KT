#include <bits/stdc++.h>
using namespace std;
vector<int> adj[100005];
bool visited[100005];
int level[100005];
void dfs(int src) {
  visited[src] = true;
  for (auto dest : adj[src]) {
    if (!visited[dest]) {
      level[dest] = level[src] + 1;
      dfs(dest);
    }
  }
}
int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    int v;
    cin >> v;
    if (v == -1) v = 0;
    adj[i].push_back(v);
    adj[v].push_back(i);
  }
  dfs(0);
  int ans = 0;
  for (int i = 1; i <= n + 1; i++) ans = max(ans, level[i]);
  cout << ans << endl;
}
