#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10;
vector<pair<int, int> > G[N];
int in[N], cnt[N];
int ans[N];
void dfs(int u, int f, int k, int pre) {
  int cur = 1;
  if (in[u] <= k) {
    if (cur == pre) cur++;
    for (auto P : G[u]) {
      int v = P.first;
      if (v == f) continue;
      ans[P.second] = cur;
      dfs(v, u, k, cur);
      cur++;
      if (cur == pre) cur++;
    }
  } else {
    for (auto P : G[u]) {
      int v = P.first;
      if (v == f) continue;
      ans[P.second] = 1;
      dfs(v, u, k, 1);
    }
  }
}
void solve() {
  int n, k;
  scanf("%d%d", &n, &k);
  for (int i = 1; i < n; i++) {
    int u, v;
    scanf("%d%d", &u, &v);
    in[u]++, in[v]++;
    G[u].push_back(pair<int, int>(v, i));
    G[v].push_back(pair<int, int>(u, i));
  }
  for (int i = 1; i <= n; i++) cnt[in[i]]++;
  int tot = 0;
  for (int i = 1; i <= n - 1; i++) {
    tot += cnt[i];
    if (n - tot <= k) {
      printf("%d\n", i);
      dfs(1, 0, i, 0);
      for (int k = 1; k < n; k++) printf("%d ", ans[k]);
      printf("\n");
      return;
    }
  }
}
int main() {
  solve();
  return 0;
}
