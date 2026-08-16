#include <bits/stdc++.h>
using namespace std;
inline char nc() {
  static char buf[100000], *p1 = buf, *p2 = buf;
  return p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 100000, stdin), p1 == p2)
             ? EOF
             : *p1++;
}
inline void read(int &x) {
  char c = nc(), b = 1;
  for (; !(c >= '0' && c <= '9'); c = nc())
    if (c == '-') b = -1;
  for (x = 0; c >= '0' && c <= '9'; x = x * 10 + c - '0', c = nc())
    ;
  x *= b;
}
const int N = 405;
int n, a[N], v[N];
int f[N][N], g[N][N], h[N][N];
int ans[N];
int main() {
  read(n);
  for (int i = 1; i <= n; i++) read(v[i]);
  for (int i = 1; i <= n; i++) read(a[i]);
  for (int l = 1; l <= n; l++)
    for (int i = 1; i + l - 1 <= n; i++) {
      int j = i + l - 1;
      if (i == j) {
        g[i][j] = 0, h[i][j] = 0;
        f[i][j] = v[1];
        continue;
      }
      g[i][j] = h[i][j] = -1 << 28;
      for (int k = i + 1; k <= j; k++)
        if (a[k] == a[i] + 1)
          g[i][j] = max(g[i][j], f[i + 1][k - 1] + g[k][j]);
        else if (a[k] == a[i] - 1)
          h[i][j] = max(h[i][j], f[i + 1][k - 1] + h[k][j]);
      f[i][j] = -1 << 28;
      for (int k = i; k < j; k++) f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j]);
      for (int k = i; k <= j; k++)
        if (g[i][k] > -1 << 20 && h[k][j] > -1 << 20)
          f[i][j] =
              max(f[i][j], g[i][k] + h[k][j] + v[2 * a[k] - a[i] - a[j] + 1]);
    }
  for (int i = 1; i <= n; i++) {
    ans[i] = ans[i - 1];
    for (int j = 1; j <= i; j++) ans[i] = max(ans[i], ans[j - 1] + f[j][i]);
  }
  printf("%d\n", ans[n]);
  return 0;
}
