#include <bits/stdc++.h>
using namespace std;
const int sx[4] = {1, 0, -1, 0};
const int sy[4] = {0, 1, 0, -1};
int i, n, m, D[111000], f[111000], t[111000], p[111000], ii, fl[111000],
    o[111000], q1, q2, q[111000], vn, qq, v[111000], pr[111000], ret, j,
    a[111][111], c[111][111], k, x2, y2, it;
void addedge(int x, int y, int z) {
  t[++ii] = y;
  p[ii] = f[x];
  f[x] = ii;
  v[ii] = z;
  fl[ii] = 1;
  o[ii] = ii + 1;
  t[++ii] = x;
  p[ii] = f[y];
  f[y] = ii;
  v[ii] = -z;
  fl[ii] = 0;
  o[ii] = ii - 1;
}
void findway() {
  for (i = 0; i <= n * m + 1; i++) D[i] = 1000000000;
  q1 = q2 = 0;
  q[q1++] = 0;
  D[0] = 0;
  while (q1 != q2) {
    vn = q[q2++];
    qq = f[vn];
    while (qq) {
      if (fl[qq] && D[t[qq]] > D[vn] + v[qq]) {
        D[t[qq]] = D[vn] + v[qq];
        q[q1++] = t[qq];
        pr[t[qq]] = qq;
      }
      qq = p[qq];
    }
  }
  ret += D[n * m + 1];
  vn = n * m + 1;
  while (vn) {
    --fl[pr[vn]];
    ++fl[o[pr[vn]]];
    vn = t[o[pr[vn]]];
  }
}
int main() {
  scanf("%d%d", &n, &m);
  for (i = 1; i <= n; i++)
    for (j = 1; j <= m; j++) scanf("%d", &a[i][j]);
  int tt = 0;
  for (i = 1; i <= n; i++)
    for (j = 1; j <= m; j++) {
      c[i][j] = ++tt;
      if ((i + j) % 2)
        addedge(0, tt, 0);
      else
        addedge(tt, n * m + 1, 0);
    }
  for (i = 1; i <= n; i++)
    for (j = 1; j <= m; j++)
      if ((i + j) % 2)
        for (k = 0; k < 4; k++) {
          x2 = i + sx[k];
          y2 = j + sy[k];
          if (!x2 || !y2 || x2 > n || y2 > m) continue;
          addedge(c[i][j], c[x2][y2], 1 - (a[i][j] == a[x2][y2]));
        }
  for (it = 0; it < (n * m) / 2; it++) findway();
  printf("%d\n", ret);
  return 0;
}
