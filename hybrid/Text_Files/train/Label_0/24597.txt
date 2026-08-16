#include <bits/stdc++.h>
using namespace std;
int n, m;
vector<vector<int> > adj;
int sameEdge = 0;
vector<int> diffEdge;
vector<int> visited;
void preprocess(void) { return; }
void dfs(int v) {
  visited[v] = 1;
  for (int i = 0; i < (int)adj[v].size(); i++) {
    int u = adj[v][i];
    if (!visited[u]) {
      dfs(u);
    }
  }
}
int main(void) {
  preprocess();
  int t;
  t = 1;
  for (int z = 1; z <= t; z++) {
    scanf("%d", &n), scanf("%d", &m);
    adj.resize(n);
    diffEdge.assign(n, 0);
    for (int i = 0; i < m; i++) {
      int u, v;
      scanf("%d", &u), scanf("%d", &v);
      u--, v--;
      adj[u].push_back(v);
      adj[v].push_back(u);
      if (u == v) {
        sameEdge++;
      } else {
        diffEdge[u]++;
        diffEdge[v]++;
      }
    }
    int cnt = 0;
    visited.assign(n, 0);
    for (int i = 0; i < n; i++) {
      if (!visited[i]) {
        dfs(i);
        if (adj[i].size() > 0) {
          cnt++;
        }
      }
    }
    if (cnt > 1) {
      printf("%d\n", 0);
      return 0;
    }
    long long ans = sameEdge * ((long long)sameEdge - 1);
    ans /= 2;
    long long auxans = 0;
    for (int i = 0; i < n; i++) {
      ans += (diffEdge[i] * ((long long)diffEdge[i] - 1)) / 2;
      auxans += sameEdge * (long long)diffEdge[i];
    }
    printf("%lld\n", ans + auxans / 2);
  }
  return 0;
}
