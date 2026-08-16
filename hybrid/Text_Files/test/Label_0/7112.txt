#include <bits/stdc++.h>
using namespace std;
vector<int> E[100000 + 10], V;
bool vis[100000 + 10], adj[100000 + 10];
void dfs(int nd) {
  vis[nd] = 1;
  V.push_back(nd);
  for (int i = 0; i < E[nd].size(); i++) {
    if (!vis[E[nd][i]]) return dfs(E[nd][i]);
  }
  for (int i = 0; i < E[nd].size(); i++) adj[E[nd][i]] = 1;
}
int main() {
  int i, j, k, cs, t, n, m;
  scanf("%d %d %d", &n, &m, &k);
  for (i = 1; i <= m; i++) {
    scanf("%d %d", &j, &k);
    E[j].push_back(k);
    E[k].push_back(j);
  }
  dfs(1);
  for (i = 0;; i++) {
    if (adj[V[i]] == 1) {
      printf("%d\n", V.size() - i);
      printf("%d", V[i]);
      for (i++; i < V.size(); i++) printf(" %d", V[i]);
      break;
    }
  }
  return 0;
}
