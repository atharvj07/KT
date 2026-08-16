#include <bits/stdc++.h>
using namespace std;
const int N = 100005;
int n, m, q, x, y, z, fi[N], from[N], ne[N], zz[N], sl[N], f[N], g[N], a[N],
    dis2[N], opt, l, tot;
long long dis[N];
vector<int> v[N];
void jb(int x, int y, int z) {
  from[++tot] = x;
  ne[tot] = fi[x];
  fi[x] = tot;
  zz[tot] = y;
  sl[tot] = z;
}
void down(int x) {
  int i = x;
  if (x * 2 <= l && dis[f[x * 2]] < dis[f[i]]) i = x * 2;
  if (x * 2 < l && dis[f[x * 2 + 1]] < dis[f[i]]) i = x * 2 + 1;
  if (i != x) {
    swap(f[x], f[i]);
    swap(g[f[x]], g[f[i]]);
    down(i);
  }
}
void up(int x) {
  if (x == 1) return;
  if (dis[f[x / 2]] > dis[f[x]]) {
    swap(f[x], f[x / 2]);
    swap(g[f[x]], g[f[x / 2]]);
    up(x / 2);
  }
}
int main() {
  scanf("%d%d%d", &n, &m, &q);
  for (int i = 1; i <= m; i++) {
    scanf("%d%d%d", &x, &y, &z);
    jb(x, y, z);
  }
  l = n;
  for (int i = 1; i <= n; i++) f[i] = g[i] = i;
  memset(dis, 0x3f, sizeof dis);
  dis[1] = 0;
  for (int i = 1; i <= n; i++) {
    int k = f[1];
    f[1] = f[l--];
    g[f[1]] = 1;
    down(1);
    for (int j = fi[k]; j; j = ne[j])
      if (dis[zz[j]] > dis[k] + sl[j]) {
        dis[zz[j]] = dis[k] + sl[j];
        up(g[zz[j]]);
      }
  }
  while (q--) {
    scanf("%d", &opt);
    if (opt == 1) {
      scanf("%d", &x);
      if (dis[x] > 1e18)
        puts("-1");
      else
        printf("%lld\n", dis[x]);
    } else {
      scanf("%d", &x);
      while (x--) scanf("%d", &y), sl[y]++;
      for (int i = 1; i <= m; i++) a[i] = dis[from[i]] - dis[zz[i]] + sl[i];
      v[0].push_back(1);
      memset(dis2, 0x3f, sizeof dis2);
      dis2[1] = 0;
      for (int i = 0; i < n; i++) {
        for (int l = 0; l < (int)v[i].size(); l++) {
          int j = v[i][l];
          if (dis2[j] == i)
            for (int k = fi[j]; k; k = ne[k])
              if (dis2[zz[k]] > dis2[j] + a[k]) {
                dis2[zz[k]] = dis2[j] + a[k];
                if (dis2[zz[k]] < n) v[dis2[zz[k]]].push_back(zz[k]);
              }
        }
        v[i].clear();
      }
      for (int i = 1; i <= n; i++) dis[i] += dis2[i];
    }
  }
  return 0;
}
