#include <bits/stdc++.h>
using namespace std;
const int N = 2003, inf = 0x3f3f3f3f;
int n, m, s, t, a[N], mp[N][N];
long long da[N], db[N], g[N][N], h[N][N], c[N], la[N], fa[N][N], fb[N][N], tp,
    vis[N];
void D(int S, long long *d) {
  for (int i = 0; i <= n; ++i) d[i] = 1e18, vis[i] = 0;
  d[S] = 0;
  for (int i = 1; i <= n; ++i) {
    int u = 0;
    for (int j = 1; j <= n; ++j)
      if (d[j] < d[u] && !vis[j]) u = j;
    vis[u] = 1;
    for (int j = 1; j <= n; ++j) {
      if (mp[u][j] < inf) d[j] = min(d[j], d[u] + mp[u][j]);
    }
  }
  for (int i = 1; i <= n; ++i) c[i] = d[i];
  sort(c + 1, c + n + 1);
  int tot = unique(c + 1, c + n + 1) - c - 1;
  for (int i = 1; i <= n; ++i) d[i] = lower_bound(c + 1, c + n + 1, d[i]) - c;
}
int main() {
  memset(mp, 0x3f, sizeof mp);
  scanf("%d%d%d%d", &n, &m, &s, &t);
  for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
  for (; m; m--) {
    int x, y, z;
    scanf("%d%d%d", &x, &y, &z);
    mp[x][y] = mp[y][x] = min(z, mp[x][y]);
  }
  D(s, da), D(t, db);
  for (int i = 1; i <= n; ++i)
    g[da[i]][db[i]] += a[i], h[da[i]][db[i]]++, la[i] = n + 1;
  int lb;
  for (int i = n; i; --i) {
    lb = n + 1;
    for (int j = n; j; --j) {
      g[i][j] += g[i + 1][j] + g[i][j + 1] - g[i + 1][j + 1];
      tp = g[i][j];
      h[i][j] += h[i + 1][j] + h[i][j + 1] - h[i + 1][j + 1];
      if (h[i][j] > h[i + 1][j]) la[j] = i + 1;
      if (h[i][j] > h[i][j + 1]) lb = j + 1;
      fa[i][j] = fb[la[j]][j] + tp;
      fb[i][j] = fa[i][lb] - tp;
      if (i > 1 || j > 1)
        fa[i][j] = min(fa[i][j] + tp, fa[i][j + 1]),
        fb[i][j] = max(fb[i][j] - tp, fb[i + 1][j]);
    }
  }
  puts(fa[1][1] ? fa[1][1] > 0 ? "Break a heart" : "Cry" : "Flowers");
  return 0;
}
