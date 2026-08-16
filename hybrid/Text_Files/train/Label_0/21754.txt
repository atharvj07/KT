#include <bits/stdc++.h>
using namespace std;
const int M = 1005;
int read() {
  int x = 0, y = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') y = (ch == '-') ? -1 : 1, ch = getchar();
  while (ch >= '0' && ch <= '9') x = x * 10 + ch - '0', ch = getchar();
  return x * y;
}
bitset<M * M / 2> dp[M];
bool check(int n, int v[], int va[], int vb[], int K) {
  va[0] = vb[0] = 0;
  dp[0][0] = 1;
  for (int i = 1; i <= n; i++) dp[i] = dp[i - 1] | dp[i - 1] << v[i];
  if (!dp[n][K]) return 0;
  for (int i = n; i >= 1; i--) {
    if (K >= v[i] && dp[i - 1][K - v[i]])
      va[++va[0]] = v[i], K -= v[i];
    else
      vb[++vb[0]] = v[i];
  }
  sort(va + 1, va + va[0] + 1), sort(vb + 1, vb + vb[0] + 1);
  return 1;
}
int n, m, a[M], b[M], xa[M], xb[M], ya[M], yb[M], x[M], y[M];
void solve() {
  n = read();
  a[0] = b[0] = x[0] = y[0] = 0;
  for (int i = 1; i <= n; i++) a[i] = read(), a[0] += a[i];
  m = read();
  for (int i = 1; i <= m; i++) b[i] = read(), b[0] += b[i];
  if (n != m || a[0] & 1 || b[0] & 1 || !check(n, a, xa, xb, a[0] >> 1) ||
      !check(m, b, ya, yb, b[0] >> 1))
    return (void)(printf("No\n"));
  if (xa[0] > xb[0]) swap(xa, xb);
  if (ya[0] < yb[0]) swap(ya, yb);
  for (int i = xa[0]; i >= 1; i--) x[++x[0]] = xa[i];
  for (int i = xb[0]; i >= 1; i--) x[++x[0]] = -xb[i];
  for (int i = 1; i <= ya[0]; i++) y[++y[0]] = ya[i];
  for (int i = 1; i <= ya[0]; i++) y[++y[0]] = -yb[i];
  int nx = 0, ny = 0;
  printf("Yes\n");
  for (int i = 1; i <= x[0]; i++) {
    nx += x[i];
    printf("%d %d\n", nx, ny);
    ny += y[i];
    printf("%d %d\n", nx, ny);
  }
}
signed main() {
  int T = read();
  while (T--) solve();
}
