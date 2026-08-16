#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e6 + 7;
const int INF = 1e7;
char s[maxn];
int fa[maxn], siz[maxn];
int l[maxn][2];
int n, k;
int findset(int x) {
  if (fa[x] == x) return x;
  return fa[x] = findset(fa[x]);
}
void Union(int x, int y) {
  int rx = findset(x), ry = findset(y);
  if (!ry) swap(rx, ry);
  if (rx) siz[rx] += siz[ry];
  fa[ry] = rx;
}
int cal(int x) {
  int y = x + k;
  x = findset(x), y = findset(y);
  return min(siz[x], siz[y]);
}
int main() {
  scanf("%d%d", &n, &k);
  scanf("%s", s + 1);
  for (int i = 1; i <= k; i++) {
    int m;
    scanf("%d", &m);
    for (int j = 1; j <= m; j++) {
      int x;
      scanf("%d", &x);
      if (l[x][0] == 0)
        l[x][0] = i;
      else
        l[x][1] = i;
    }
    siz[i] = 1;
    fa[i] = i;
    fa[i + k] = i + k;
  }
  siz[0] = INF;
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    int x = l[i][0], y = l[i][1];
    int rx = findset(x), ry = findset(y);
    int rxk = findset(x + k), ryk = findset(y + k);
    if (!y) {
      ans -= cal(x);
      if (s[i] == '1') fa[rx] = 0;
      if (s[i] == '0') fa[rxk] = 0;
      ans += cal(x);
    } else if (s[i] == '0' && rx != ryk) {
      ans -= cal(x);
      ans -= cal(y);
      Union(x, y + k);
      Union(y, x + k);
      ans += cal(x);
    } else if (s[i] == '1' && rx != ry) {
      ans -= cal(x);
      ans -= cal(y);
      Union(x, y);
      Union(x + k, y + k);
      ans += cal(x);
    }
    printf("%d\n", ans);
  }
  return 0;
}
