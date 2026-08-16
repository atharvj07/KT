#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
const int logN = 17;
int n, q, h[N], par[logN][N];
vector<int> adj[N];
void Dfs(int u, int p) {
  for (int i = 1; i <= logN - 1; i++) par[i][u] = par[i - 1][par[i - 1][u]];
  for (int v : adj[u])
    if (v != p) {
      h[v] = h[u] + 1;
      par[0][v] = u;
      Dfs(v, u);
    }
}
int LCA(int u, int v) {
  if (h[u] > h[v]) swap(u, v);
  for (int i = logN - 1; i >= 0; i--)
    if (h[u] <= h[v] - (1 << i)) v = par[i][v];
  if (v == u) return u;
  for (int i = logN - 1; i >= 0; i--)
    if (par[i][u] != par[i][v]) {
      u = par[i][u];
      v = par[i][v];
    }
  return par[0][u];
}
int Dist(int u, int v) {
  int lca = LCA(u, v);
  return h[u] + h[v] - 2 * h[lca];
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n - 1; i++) {
    int u, v;
    scanf("%d %d", &u, &v);
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  Dfs(1, 1);
  scanf("%d", &q);
  while (q--) {
    int x, y, a, b, k;
    scanf("%d %d %d %d %d", &x, &y, &a, &b, &k);
    int tmp = Dist(a, b);
    if (k >= tmp && (k - tmp) % 2 == 0) {
      printf("YES\n");
      continue;
    }
    tmp = Dist(a, x) + 1 + Dist(y, b);
    if (k >= tmp && (k - tmp) % 2 == 0) {
      printf("YES\n");
      continue;
    }
    tmp = Dist(a, y) + 1 + Dist(x, b);
    if (k >= tmp && (k - tmp) % 2 == 0) {
      printf("YES\n");
      continue;
    }
    printf("NO\n");
  }
}
