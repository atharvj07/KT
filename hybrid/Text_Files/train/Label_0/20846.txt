#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5 + 100;
int T;
int n, m, k;
int deg[maxn], vis[maxn], del[maxn], now;
vector<int> g[maxn], clique;
queue<int> q;
void init() {
  now = n;
  for (int i = 1; i <= n; i++) g[i].clear(), deg[i] = 0, vis[i] = 0, del[i] = 0;
  while (!q.empty()) q.pop();
}
void solve() {
  scanf("%d%d%d", &n, &m, &k);
  init();
  for (int i = 0, u, v; i < m; i++) {
    scanf("%d%d", &u, &v);
    g[u].push_back(v), g[v].push_back(u);
    deg[u]++, deg[v]++;
  }
  for (int i = 1; i <= n; i++)
    if (deg[i] < k) q.push(i), vis[i] = true;
  for (int i = 1; i <= n; i++) sort(g[i].begin(), g[i].end());
  while (!q.empty()) {
    int top = q.front();
    q.pop();
    now--;
    if (deg[top] == k - 1) {
      clique.clear();
      clique.push_back(top);
      for (int nxt : g[top])
        if (!del[nxt]) clique.push_back(nxt);
      int have_ans = 1;
      for (int i : clique) {
        for (int j : clique) {
          if (i == j) continue;
          if (!binary_search(g[i].begin(), g[i].end(), j)) {
            have_ans = 0;
            goto p1;
          }
        }
      }
    p1:
      if (have_ans) {
        printf("2\n");
        bool first = true;
        for (int i : clique) {
          if (first)
            printf("%d", i), first = false;
          else
            printf(" %d", i);
        }
        printf("\n");
        return;
      } else
        del[top] = 1;
    }
    del[top] = 1;
    for (int nxt : g[top]) {
      deg[nxt]--;
      if (deg[nxt] < k && !vis[nxt]) q.push(nxt), vis[nxt] = true;
    }
  }
  if (now) {
    printf("1 %d\n", now);
    for (int i = 1, cnt = 1; i <= n; i++, cnt++)
      if (!vis[i]) printf("%d%c", i, cnt == now ? '\n' : ' ');
  } else
    printf("-1\n");
}
int main() {
  cin >> T;
  while (T--) solve();
  return 0;
}
