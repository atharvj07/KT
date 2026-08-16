#include <bits/stdc++.h>
using namespace std;
inline int read() {
  int x = 0, d = 1;
  char y = getchar();
  while (y < '0' || y > '9') {
    if (y == '-') d = -1;
    y = getchar();
  }
  while (y >= '0' && y <= '9') {
    x = (x << 3) + (x << 1) + (y ^ '0');
    y = getchar();
  }
  return x * d;
}
struct vec {
  int v[510];
} x[510], y[510];
int T, n, m, kk, ins[250010];
bool cmp(vec p, vec q) { return p.v[1] < q.v[1]; }
int main() {
  T = read();
  while (T--) {
    n = read();
    m = read();
    for (register int i = 1; i <= n; i++) {
      for (register int j = 1; j <= m; j++) x[i].v[j] = read();
      ins[x[i].v[1]] = 1;
    }
    sort(x + 1, x + n + 1, cmp);
    for (register int i = 1; i <= m; i++) {
      for (register int j = 1; j <= n; j++) y[i].v[j] = read();
      if (ins[y[i].v[1]]) kk = i;
    }
    for (register int i = 1; i <= n; i++) ins[x[i].v[1]] = 0;
    for (register int i = 1; i <= n; i++) {
      int c = y[kk].v[i];
      int l = 1, r = n, mid;
      while (l < r) {
        mid = (l + r) >> 1;
        if (x[mid].v[1] >= c)
          r = mid;
        else
          l = mid + 1;
      }
      for (register int j = 1; j <= m; j++) printf("%d ", x[l].v[j]);
      putchar('\n');
    }
  }
  return 0;
}
