#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2e5 + 5;
int n;
int cnt[2];
vector<int> Adj[MAXN];
void DFS(int node, int p, int c) {
  cnt[c]++;
  for (auto x : Adj[node]) {
    if (x == p) {
      continue;
    }
    DFS(x, node, 1 - c);
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n;
  for (int i = 1; i < n; i++) {
    int u, v;
    cin >> u >> v;
    Adj[u].push_back(v);
    Adj[v].push_back(u);
  }
  DFS(1, -1, 0);
  cout << min(cnt[0], cnt[1]) - 1;
}
