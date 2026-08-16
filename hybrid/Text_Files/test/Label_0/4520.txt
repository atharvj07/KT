#include <bits/stdc++.h>
using namespace std;
const int maxn = 3010;
const int maxq = 4e5 + 10;
const int base = 31337;
const int mod = 1e9 + 7;
const int inf = 0x3f3f3f3f;
const int logo = 20;
const int off = 1 << logo;
const int treesiz = off << 1;
int n, m, q;
vector<int> graph[maxn], graph2[maxn];
int ss[maxq], ts[maxq], ks[maxq];
int sol[maxq];
vector<int> qs[maxn];
bool bio[maxn];
int dp[logo + 10][maxn];
int ac[maxn];
void dfs(int x) {
  bio[x] = true;
  for (int i = 0; i < graph2[x].size(); i++) {
    int tren = graph2[x][i];
    if (!bio[tren]) dfs(tren);
  }
}
int f(int x, int val) {
  for (int i = 0; i <= logo; i++) {
    if (val & (1 << i)) x = dp[i][x];
  }
  return x;
}
int main() {
  scanf("%d%d%d", &n, &m, &q);
  for (int i = 0; i < m; i++) {
    int a, b;
    scanf("%d%d", &a, &b);
    graph[a].push_back(b);
    graph2[b].push_back(a);
  }
  for (int i = 0; i < q; i++) {
    scanf("%d%d%d", ss + i, ts + i, ks + i);
    qs[ts[i]].push_back(i);
  }
  for (int i = 1; i <= n; i++) {
    memset(bio, false, sizeof bio);
    dfs(i);
    for (int j = 1; j <= n; j++) {
      if (i == j) continue;
      if (!bio[j]) continue;
      int mini = n + 1;
      for (int l = 0; l < graph[j].size(); l++) {
        int tren = graph[j][l];
        if (bio[tren]) mini = min(mini, tren);
      }
      dp[0][j] = mini;
    }
    dp[0][i] = 0;
    for (int i = 1; i <= logo; i++)
      for (int j = 1; j <= n; j++) dp[i][j] = dp[i - 1][dp[i - 1][j]];
    for (auto ind : qs[i]) {
      int s = ss[ind];
      int t = ts[ind];
      int k = ks[ind];
      if (!bio[s])
        sol[ind] = -1;
      else {
        int a = f(s, k - 1);
        if (a == 0 || f(s, maxn * 2) != 0)
          sol[ind] = -1;
        else
          sol[ind] = a;
      }
    }
  }
  for (int i = 0; i < q; i++) printf("%d\n", sol[i]);
  return 0;
}
