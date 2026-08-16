#include <bits/stdc++.h>
using namespace std;
const int N = 100005, D = 50;
const int V = N * D;
vector<int> g[N];
int S[V], ssz;
int low[V], num[V], cnt, vis[V];
int scc[V], scc_cnt;
int all[V], sz;
int n, m, d;
long long val[N];
void push(int i, int j) {
  if (val[i] >> j & 1) {
    all[sz++] = i;
    while (sz >= V) sz++;
  }
}
int dp[V];
void tarjanSCC(int u) {
  low[u] = num[u] = ++cnt;
  vis[u] = 1;
  S[ssz++] = u;
  while (ssz >= V) {
    ssz++;
  }
  for (int w : g[u / d]) {
    int v = w * d + (u % d + 1) % d;
    while (v >= V) v++;
    if (!num[v]) tarjanSCC(v);
    if (vis[v]) low[u] = min(low[u], low[v]);
  }
  if (low[u] == num[u]) {
    scc[u] = ++scc_cnt;
    int v;
    sz = 0;
    push(u / d, u % d);
    do {
      v = S[--ssz];
      vis[v] = 0;
      push(v / d, v % d);
      scc[v] = scc_cnt;
      for (int wver : g[v / d]) {
        int ver = wver * d + (v % d + 1) % d;
        if (scc[ver]) {
          dp[scc_cnt] = max(dp[scc_cnt], dp[scc[ver]]);
        }
      }
    } while (u != v);
    sort(all, all + sz);
    dp[scc_cnt] += int(unique(all, all + sz) - all);
  }
}
int main() {
  scanf("%d %d %d", &n, &m, &d);
  for (int i = 0; i < m; i++) {
    int u, v;
    scanf("%d %d", &u, &v);
    u--, v--;
    g[u].push_back(v);
  }
  char str[100];
  for (int i = 0; i < n; i++) {
    scanf(" %s", str);
    for (int j = 0; j < d; j++) {
      if (str[j] == '1') {
        val[i] |= 1LL << j;
      }
    }
  }
  tarjanSCC(0);
  printf("%d\n", dp[scc[0]]);
}
