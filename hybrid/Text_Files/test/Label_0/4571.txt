#include <bits/stdc++.h>
const int maxn = 300005;
const int maxm = maxn;
std::vector<int> G[maxn], G2[maxn];
int low[maxn], dfn[maxn];
int sccno[maxn];
int scc_cnt;
std::stack<int> S;
void tarjan(int x) {
  static int clk = 0;
  low[x] = dfn[x] = ++clk;
  S.push(x);
  for (int i = 0; i < G[x].size(); i++) {
    int v = G[x][i];
    if (dfn[v]) {
      if (!sccno[v]) low[x] = std::min(low[x], dfn[v]);
    } else {
      tarjan(v);
      low[x] = std::min(low[x], low[v]);
    }
  }
  if (low[x] == dfn[x]) {
    scc_cnt++;
    while (true) {
      int u = S.top();
      S.pop();
      sccno[u] = scc_cnt;
      if (u == x) {
        break;
      }
    }
  }
}
int n, m;
void work() {
  scc_cnt = 0;
  for (int i = 1; i <= n; i++) {
    if (!dfn[i]) {
      tarjan(i);
    }
  }
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < G[i].size(); j++) {
      int v = G[i][j];
      int c1 = sccno[i], c2 = sccno[v];
      if (c1 != c2) {
        G2[c1].push_back(c2);
      }
    }
  }
}
int w[maxn];
int d[maxn];
int dp(int x) {
  if (d[x] > -1) {
    return d[x];
  }
  d[x] = w[x];
  for (int i = 0; i < G2[x].size(); i++) {
    int v = G2[x][i];
    d[x] = std::max(d[x], dp(v) + w[x]);
  }
  return d[x];
}
char col[maxn];
int main() {
  scanf("%d%d", &n, &m);
  scanf("%s", col + 1);
  bool fail = false;
  while (m--) {
    int u, v;
    scanf("%d%d", &u, &v);
    if (u == v) fail = true;
    G[u].push_back(v);
  }
  work();
  if (scc_cnt < n || fail) {
    puts("-1");
    return 0;
  }
  int ans = 0;
  for (char c = 'a'; c <= 'z'; c++) {
    memset(w, 0, sizeof(w));
    memset(d, -1, sizeof(d));
    for (int i = 1; i <= n; i++) {
      if (col[i] == c) {
        w[sccno[i]]++;
      }
    }
    for (int i = 1; i <= scc_cnt; i++) {
      ans = std::max(ans, dp(i));
    }
  }
  printf("%d\n", ans);
  return 0;
}
