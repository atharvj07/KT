#include <bits/stdc++.h>
using namespace std;
const int MAX = 2005;
const int INF = 0x3f3f3f3f;
int n, m, w, c[MAX], v[MAX], fa[MAX];
long long dp[2][MAX * 100];
vector<int> ve[MAX];
int find(int x) { return x == fa[x] ? x : fa[x] = find(fa[x]); }
void Union(int u, int v) {
  int a = find(u);
  int b = find(v);
  if (a != b) {
    fa[a] = b;
  }
}
int id[MAX];
int main() {
  memset(c, 0, sizeof(c));
  memset(v, 0, sizeof(v));
  scanf("%d%d%d", &n, &m, &w);
  for (int i = 1; i <= n; i++) fa[i] = i;
  for (int i = 1; i <= n; i++) scanf("%d", &c[i]);
  for (int i = 1; i <= n; i++) scanf("%d", &v[i]);
  for (int i = 1; i <= m; i++) {
    int u, v;
    scanf("%d%d", &u, &v);
    Union(u, v);
  }
  int tot = 0;
  memset(id, -1, sizeof(id));
  for (int i = 1; i <= n; i++) {
    int u = find(i);
    if (id[u] == -1) id[u] = tot++;
    ve[id[u]].push_back(i);
    c[n + 1 + id[u]] += c[i];
    v[n + 1 + id[u]] += v[i];
  }
  memset(dp, 0, sizeof(dp));
  int flag = 1;
  for (int i = 0; i < tot; i++) {
    flag = 1 - flag;
    ve[i].push_back(n + 1 + i);
    int size = ve[i].size();
    for (int k = 0; k <= w; k++) dp[flag][k] = dp[1 - flag][k];
    for (int j = 0; j < size; j++) {
      int cost = c[ve[i][j]];
      int val = v[ve[i][j]];
      for (int k = w; k >= cost; k--) {
        dp[flag][k] = max(dp[flag][k], dp[1 - flag][k - cost] + (long long)val);
      }
    }
  }
  long long ans = 0;
  for (int k = 0; k <= w; k++) ans = max(ans, dp[flag][k]);
  printf("%I64d\n", ans);
  return 0;
}
