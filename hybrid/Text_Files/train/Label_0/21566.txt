#include <bits/stdc++.h>
using namespace std;
const int mod = 1000000007;
int sx = mod, sy = mod, bx, by;
int cnt, n;
int vis[5001], cost[5001][5001], x[5001], y[5001];
bool dfs(int v, int c, int mid) {
  if (vis[v] && c != vis[v]) return 0;
  if (vis[v]) return 1;
  vis[v] = c;
  for (int i = 1; i <= n; i++)
    if (cost[v][i] > mid)
      if (!dfs(i, 3 - c, mid)) return 0;
  return 1;
}
bool check(int mid) {
  cnt = 0;
  for (int i = 1; i <= n; i++)
    if (!vis[i]) {
      if (!dfs(i, 1, mid)) return 0;
      cnt++;
    }
  return 1;
}
void out() {
  int ans = 1;
  for (int i = 1; i <= cnt; i++) ans = ans * 2 % mod;
  cout << ans << endl;
}
int main() {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    scanf("%d%d", &x[i], &y[i]);
    sx = min(x[i], sx);
    sy = min(y[i], sy);
    bx = max(x[i], bx);
    by = max(y[i], by);
  }
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      cost[i][j] = abs(x[j] - x[i]) + abs(y[j] - y[i]);
  int lb = 0, ub = bx + by - sx - sy;
  while (lb <= ub) {
    memset(vis, 0, sizeof(vis));
    int mid = (lb + ub) / 2;
    if (!check(mid))
      lb = mid + 1;
    else
      ub = mid - 1;
  }
  cout << lb << endl;
  memset(vis, 0, sizeof(vis));
  check(lb);
  out();
  return 0;
}
