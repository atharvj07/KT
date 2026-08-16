#include <bits/stdc++.h>
using namespace std;
struct E {
  int next, to;
} e[210];
int head[110];
int cnt;
void add(int u, int v) {
  e[++cnt].to = v;
  e[cnt].next = head[u];
  head[u] = cnt;
}
int dp[200][200];
int k;
int f[200];
void dfs(int u, int fa) {
  dp[u][0] = dp[u][k + 1] = 1;
  for (int i = head[u]; i; i = e[i].next) {
    int v = e[i].to;
    if (v == fa) continue;
    dfs(v, u);
    memset(f, 0, sizeof(f));
    for (int j = 0; j <= 2 * k; j++) {
      for (int jj = 0; jj <= 2 * k; jj++) {
        if (jj + j <= 2 * k)
          (f[min(jj + 1, j)] += 1ll * dp[u][j] * dp[v][jj] % 1000000007) %=
              1000000007;
        else
          (f[max(jj + 1, j)] += 1ll * dp[u][j] * dp[v][jj] % 1000000007) %=
              1000000007;
      }
    }
    for (int j = 0; j <= 2 * k + 1; j++) {
      dp[u][j] = f[j];
    }
  }
}
int n;
int main() {
  cin >> n >> k;
  int u, v;
  for (int i = 1; i < n; i++) {
    scanf("%d%d", &u, &v);
    add(u, v), add(v, u);
  }
  dfs(1, 0);
  int ans = 0;
  for (int i = 0; i <= k; i++) (ans += dp[1][i]) %= 1000000007;
  cout << ans;
  return 0;
}
