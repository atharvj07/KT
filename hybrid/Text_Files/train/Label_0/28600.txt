#include <bits/stdc++.h>
using namespace std;
int n, m, cnt;
vector<vector<int> > adj;
bool vis[100000 + 9];
void dfs(int node) {
  vis[node] = 1;
  for (int i = 0; i < (int)adj[node].size(); i++) {
    int child = adj[node][i];
    if (!vis[child]) dfs(child);
  }
}
int main() {
  int n, m;
  cin >> n >> m;
  adj.resize(n);
  for (int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;
    x--, y--;
    adj[x].push_back(y);
    adj[y].push_back(x);
  }
  int cnt = 0;
  memset(vis, 0, sizeof(vis));
  for (int i = 0; i < n; i++) {
    if (vis[i] == 0) {
      dfs(i);
      cnt++;
    }
  }
  if (cnt == 1 && n == m) {
    cout << "FHTAGN!" << endl;
  } else {
    cout << "NO";
  }
  return 0;
}
