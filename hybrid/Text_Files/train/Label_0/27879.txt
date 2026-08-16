#include <bits/stdc++.h>
using namespace std;
const int MAXN = 500000;
int n;
vector<int> G[MAXN], W[MAXN];
long long dp[MAXN], dsum[MAXN], son[MAXN];
int indice[MAXN];
bool cmp(int u, int v) { return dsum[u] * son[v] < dsum[v] * son[u]; }
void dfs(int u, int fa) {
  dsum[u] = dp[u] = son[u] = 0;
  int cnt = 0;
  for (int i = 0; i < G[u].size(); i++) {
    int v = G[u][i];
    if (v == fa) continue;
    dfs(v, u);
    dsum[v] += 2 * W[u][i];
    dsum[u] += dsum[v];
    dp[v] += son[v] * W[u][i];
    dp[u] += dp[v];
    son[u] += son[v];
  }
  for (int i = 0; i < G[u].size(); i++)
    if (G[u][i] == fa)
      continue;
    else
      indice[++cnt] = G[u][i];
  sort(indice + 1, indice + cnt + 1, cmp);
  int s = son[u];
  for (int i = 1; i <= cnt; i++) {
    s -= son[indice[i]];
    dp[u] += s * dsum[indice[i]];
  }
  son[u] += 1;
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i < n; i++) {
    int u, v, d;
    scanf("%d%d%d", &u, &v, &d);
    G[u].push_back(v);
    G[v].push_back(u);
    W[u].push_back(d);
    W[v].push_back(d);
  }
  dfs(1, 0);
  printf("%.12f", (double)dp[1] / (n - 1));
  return 0;
}
