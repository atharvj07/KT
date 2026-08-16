#include <bits/stdc++.h>
using namespace std;
const int MAXN = 105;
const int MAXK = 42;
const int mod = (int)1e9 + 7;
int n, k;
vector<int> g[MAXN], g2[MAXN];
int dp[MAXN][MAXK + 5][MAXK + 5];
int dp2[MAXN][MAXK + 5][MAXK + 5][MAXN][2];
int NN;
void dfs(int v, int p = -1) {
  for (int i = 0; i < (int)g2[v].size(); i++) {
    int to = g2[v][i];
    if (to != p) {
      g[v].push_back(to);
      dfs(to, v);
    }
  }
}
int calc(int v, int up, int down);
int calc2(int v, int up, int down, int e = 0, int filled = 0) {
  if (up > NN) up = NN;
  if (down > NN) down = NN;
  int en = (int)g[v].size();
  if (en == 0) {
    if (down == NN) return 1;
    return 0;
  }
  if (e == en) {
    if (filled || down == NN) return 1;
    return 0;
  }
  if (dp2[v][up][down][e][filled] != -1) return dp2[v][up][down][e][filled];
  dp2[v][up][down][e][filled] = 0;
  for (int i = down; i <= NN; i++) {
    int cur = 1ll * calc(g[v][e], up, i) *
              calc2(v, up, down, e + 1, (filled || (i == down)) ? 1 : 0) % mod;
    dp2[v][up][down][e][filled] = (dp2[v][up][down][e][filled] + cur) % mod;
  }
  return dp2[v][up][down][e][filled];
}
int calc(int v, int up, int down) {
  if (up > NN) up = NN;
  if (down > NN) down = NN;
  if (dp[v][up][down] != -1) return dp[v][up][down];
  dp[v][up][down] = 0;
  if (down == 0) {
    dp[v][up][down] = 1;
    for (int i = 0; i < (int)g[v].size(); i++) {
      int to = g[v][i];
      int sum = 0;
      for (int j = 0; j <= NN; j++) {
        sum = (sum + calc(to, 1, j)) % mod;
      }
      dp[v][up][down] = (1ll * dp[v][up][down] * sum) % mod;
    }
    return dp[v][up][down];
  }
  if (up > k && down > k) {
    return 0;
  }
  dp[v][up][down] = calc2(v, min(up + 1, down + 1), down == NN ? NN : down - 1);
  return dp[v][up][down];
}
int main() {
  scanf("%d %d", &n, &k);
  NN = 2 * k + 1;
  for (int i = 1; i < n; i++) {
    int from, to;
    scanf("%d %d", &from, &to);
    g2[from].push_back(to);
    g2[to].push_back(from);
  }
  dfs(1);
  memset(dp, -1, sizeof(dp));
  memset(dp2, -1, sizeof(dp2));
  int ans = 0;
  for (int i = 0; i <= NN; i++) {
    ans = (ans + calc(1, NN, i)) % mod;
  }
  cout << ans << endl;
  return 0;
}
