#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const int NINF = 0xc0c0c0c0;
const int maxn = 1e6 + 5;
struct Edge {
  int u, v, w;
};
Edge edges[maxn];
long long dp[maxn];
long long val[maxn];
int scc, Index, top;
vector<pair<int, int> > G_new[maxn];
vector<int> G[maxn];
int Stack[maxn], low[maxn], dfn[maxn], belong[maxn];
int maps[maxn];
long long cost[maxn];
bool instack[maxn], vis[maxn];
void Tarjan(int u) {
  dfn[u] = low[u] = ++Index;
  instack[u] = true;
  Stack[top++] = u;
  for (int i = 0; i < G[u].size(); i++) {
    register int v = G[u][i];
    if (!dfn[v]) {
      Tarjan(v);
      low[u] = min(low[u], low[v]);
    } else if (instack[v]) {
      low[u] = min(low[u], dfn[v]);
    }
  }
  if (dfn[u] == low[u]) {
    ++scc;
    while (top > 0) {
      int now = Stack[--top];
      belong[now] = u;
      instack[now] = false;
      if (now == u) {
        maps[u] = scc;
        break;
      }
    }
  }
}
void solve(int n) {
  memset(dfn, 0, sizeof(dfn));
  memset(instack, 0, sizeof(instack));
  scc = Index = top = 0;
  for (int i = 1; i <= n; i++) {
    if (!dfn[i]) Tarjan(i);
  }
}
long long dfs(int pos) {
  if (~dp[pos]) return dp[pos];
  dp[pos] = 0;
  for (auto e : G_new[pos]) {
    register int v = e.first, w = e.second;
    long long temp = dfs(v) + w;
    if (dp[pos] < temp) {
      dp[pos] = temp;
    }
  }
  return dp[pos] += cost[pos];
}
void init() {
  val[0] = 0;
  long long temp = 0;
  for (int i = 1; i < maxn; i++) {
    temp += i;
    val[i] = val[i - 1] + temp;
  }
}
int main() {
  int n, m, s;
  init();
  while (~scanf("%d%d", &n, &m)) {
    for (int i = 1; i <= n; i++) {
      G[i].clear();
      G_new[i].clear();
    }
    for (int i = 0; i < m; ++i) {
      int u, v, w;
      scanf("%d%d%d", &u, &v, &w);
      edges[i] = {u, v, w};
      G[edges[i].u].push_back(edges[i].v);
    }
    solve(n);
    memset(dp, -1, sizeof(dp));
    memset(cost, 0, sizeof(cost));
    for (int i = 0; i < m; i++) {
      register int u, v, w;
      u = maps[belong[edges[i].u]];
      v = maps[belong[edges[i].v]];
      w = edges[i].w;
      if (u != v) {
        G_new[u].push_back(make_pair(v, w));
      } else {
        int l = 0, r = w;
        int pos;
        while (l <= r) {
          long long mid = (l + r) >> 1;
          if ((mid + 1) * mid / 2 <= w) {
            pos = mid;
            l = mid + 1;
          } else
            r = mid - 1;
        }
        cost[u] += (long long)w * (pos + 1) - val[pos];
      }
    }
    memset(vis, 0, sizeof(vis));
    scanf("%d", &s);
    s = maps[belong[s]];
    printf("%I64d\n", dfs(s));
  }
}
