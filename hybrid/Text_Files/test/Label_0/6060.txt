#include <bits/stdc++.h>
#pragma GCC optimize(3)
#pragma GCC optimize(2)
#pragma GCC optimize("Ofast")
using namespace std;
const int inf = 0x3f3f3f3f;
const int Maxn = 10005;
int a[Maxn], dist[30][30];
int vis[Maxn], ways[105];
int n, k, l;
pair<int, int> q[Maxn << 1];
int bfs(int s, int e) {
  memset(vis, 0, sizeof(vis));
  vis[s] = 1;
  int head = 0, tail = 1;
  q[head] = pair<int, int>(s, 0);
  while (head < tail) {
    pair<int, int> t = q[head++];
    int u = t.first, dist = t.second + 1;
    for (int i = 0; i < (l); ++i) {
      int v = u + ways[i];
      if (v == e) return dist;
      if (v <= n + 1 && !vis[v])
        vis[v] = 1, q[tail++] = pair<int, int>(v, dist);
      v = u - ways[i];
      if (v == e) return dist;
      if (v > 0 && !vis[v]) vis[v] = 1, q[tail++] = pair<int, int>(v, dist);
    }
  }
  return -1;
}
vector<int> v[30];
int dp[1 << 21];
int main() {
  scanf("%d%d%d", &n, &k, &l);
  for (int i = 0; i < (k); ++i) {
    int t;
    scanf("%d", &t);
    a[t] = 1;
  }
  for (int i = 0; i < (l); ++i) scanf("%d", &ways[i]);
  vector<int> all;
  for (int i = 1; i <= (n + 1); ++i)
    if (a[i] != a[i - 1]) all.push_back(i);
  for (int i = 0; i < (all.size()); ++i)
    for (int j = (i + 1); j <= (all.size() - 1); ++j)
      dist[i][j] = dist[j][i] = bfs(all[i], all[j]);
  for (int p = 0; p < (1 << all.size()); ++p) {
    int t = __builtin_popcount(p);
    if (!(t & 1)) v[t].push_back(p);
  }
  memset(dp, inf, sizeof(dp));
  dp[0] = 0;
  for (int x = 2; x <= all.size(); x += 2)
    for (int y = 0; y < (v[x].size()); ++y) {
      int p = v[x][y];
      for (int i = 0; i < (all.size()); ++i) {
        if (!(p & (1 << i))) continue;
        for (int j = (i + 1); j <= (all.size() - 1); ++j) {
          if (!(p & (1 << j)) || dist[i][j] == -1) continue;
          int np = p ^ (1 << i) ^ (1 << j);
          dp[p] = min(dp[p], dp[np] + dist[i][j]);
        }
      }
    }
  printf("%d\n",
         dp[(1 << all.size()) - 1] == inf ? -1 : dp[(1 << all.size()) - 1]);
  return 0;
}
