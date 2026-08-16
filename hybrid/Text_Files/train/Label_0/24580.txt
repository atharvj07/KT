#include <bits/stdc++.h>
using namespace std;
int n, m;
int u, v;
char s[4];
int dp[101][101][30];
vector<pair<int, int> > mp[101];
int dfs(int u, int v, int x) {
  if (~dp[u][v][x]) return dp[u][v][x];
  dp[u][v][x] = 0;
  int sz = mp[u].size();
  for (int i = 0; i < sz; ++i) {
    pair<int, int> tmp = mp[u][i];
    if (tmp.second >= x && (!dfs(v, tmp.first, tmp.second))) {
      dp[u][v][x] = 1;
      break;
    }
  }
  return dp[u][v][x];
}
int main(int argc, char const *argv[]) {
  scanf("%d %d", &n, &m);
  for (int i = 1; i <= m; ++i) {
    scanf("%d %d %s", &u, &v, s);
    mp[u].push_back(make_pair(v, s[0] - 'a'));
  }
  memset(dp, -1, sizeof(dp));
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= n; ++j)
      if (dfs(i, j, 0))
        putchar('A');
      else
        putchar('B');
    puts("");
  }
  return 0;
}
