#include <bits/stdc++.h>
using namespace std;
int vis[1000], q[1000], node[1000], n, a[1000][1000], m;
long double ans = 0;
void solve(int u) {
  int l = 0, r = 1;
  q[r] = u;
  int to = 0;
  long double maxn = 0;
  for (int i = 1; i <= n; i++)
    if (a[i][u]) {
      if ((double)(node[u] + node[i] * 1.0) / (double)a[i][u] > maxn) {
        to = i;
        maxn = (double)(node[u] + node[i] * 1.0) / (double)a[i][u];
      }
    }
  if (!to) return;
  long double sumv = node[u] + node[to];
  long double sume = a[u][to];
  vis[u] = 1;
  vis[to] = 1;
  while (l < r) {
    int t = q[++l];
    long double now = 0;
    int tag;
    long double nowv, nowe;
    for (int i = 1; i <= n; i++)
      if (!vis[i] && a[t][i]) {
        long double tmpv = sumv + node[i];
        long double tmpe = sume + a[t][i];
        for (int j = 1; j <= n; j++)
          if (vis[j] && a[i][j]) tmpe += a[i][j];
        if (tmpv / tmpe > now) {
          now = tmpv / tmpe;
          nowv = tmpv;
          nowe = tmpe;
          tag = i;
        }
      }
    if (now > sumv / sume - 0.0000000001) {
      sumv = nowv;
      sume = nowe;
      vis[tag] = 1;
      q[++r] = tag;
    }
  }
  if (sumv / sume > ans) ans = sumv / sume;
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) scanf("%d", &node[i]);
  int flg = 0;
  int x, y, w;
  for (int i = 1; i <= m; i++) {
    scanf("%d%d%d", &x, &y, &w);
    a[x][y] = a[y][x] = w;
    if (w > 0) flg = 1;
  }
  if (!flg) {
    printf("%0.15lf\n", 0);
    return 0;
  }
  for (int i = 1; i <= n; i++) {
    memset(vis, 0, sizeof vis);
    solve(i);
  }
  double tans = (double)ans;
  printf("%0.12lf\n", tans);
  return 0;
}
