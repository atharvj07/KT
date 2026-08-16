#include <bits/stdc++.h>
using namespace std;
const int MN = 100005, inf = 1000000005, mod = 1000000007;
const long long INF = 1000000000000000005LL;
int dp[2][MN];
pair<int, int> naj[4][MN];
vector<int> G[MN];
int ans;
void dfs_pre(int x, int p) {
  int sons = G[x].size() - (p != 0);
  for (auto v : G[x])
    if (v != p) {
      dfs_pre(v, x);
      if (dp[0][v] >= naj[0][x].first) {
        naj[1][x] = naj[0][x];
        naj[0][x] = {dp[0][v], v};
      } else if (dp[0][v] > naj[1][x].first) {
        naj[1][v] = {dp[0][v], v};
      }
      if (dp[1][v] >= naj[2][x].first) {
        naj[3][x] = naj[2][x];
        naj[2][x] = {dp[1][v], v};
      } else if (dp[1][v] > naj[3][x].first) {
        naj[3][v] = {dp[1][v], v};
      }
    }
  dp[0][x] = max(0, sons - 1 + max(naj[0][x].first, naj[2][x].first));
  dp[1][x] = 1 + naj[0][x].first;
}
void dfs_licz(int x, int p, int res_par_bez, int res_par_z) {
  int sons = G[x].size();
  if (res_par_bez >= naj[0][x].first) {
    naj[1][x] = naj[0][x];
    naj[0][x] = {res_par_bez, p};
  } else if (res_par_bez > naj[1][x].first) {
    naj[1][x] = {res_par_bez, p};
  }
  if (res_par_z >= naj[2][x].first) {
    naj[3][x] = naj[2][x];
    naj[2][x] = {res_par_z, p};
  } else if (res_par_z > naj[3][x].first) {
    naj[3][x] = {res_par_z, p};
  }
  int res_bez = max(0, sons - 1 + max(naj[0][x].first, naj[2][x].first));
  int res_z = 1 + naj[0][x].first;
  ans = max(ans, max(res_bez, res_z));
  for (auto v : G[x])
    if (v != p) {
      int idx_bez = (naj[0][x].second == v),
          idx_z = 2 + (naj[2][x].second == v);
      res_bez =
          max(0, sons - 2 + max(naj[idx_bez][x].first, naj[idx_z][x].first));
      res_z = 1 + naj[idx_bez][x].first;
      dfs_licz(v, x, res_bez, res_z);
    }
}
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 1; i < n; ++i) {
    int u, v;
    scanf("%d%d", &u, &v);
    G[u].push_back(v);
    G[v].push_back(u);
  }
  dfs_pre(1, 0);
  dfs_licz(1, 0, 0, 0);
  printf("%d", ans);
}
