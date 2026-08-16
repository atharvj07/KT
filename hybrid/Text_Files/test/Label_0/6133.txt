#include <bits/stdc++.h>
using namespace std;
int n, m, k, mod, f[1010], g[1010], con[1010][1010];
int expmod(int a, int b) {
  int rlt = 1, x = a;
  while (b) {
    if (b & 1) rlt = 1ll * rlt * x % mod;
    x = 1ll * x * x % mod, b >>= 1;
  }
  return rlt;
}
int calc() {
  if ((n + m) & 1) return 0;
  int x = 0, rlt = 1;
  for (int i = 1; i <= n; i++) {
    f[i] = 1;
    g[i] = m;
    for (int j = 1; j <= m; j++)
      if (con[i][j]) g[i]--, f[i] *= con[i][j];
    if (!x && g[i] == m) x = i;
  }
  for (int i = 1; i <= n; i++)
    if (i != x) {
      if (!g[i]) {
        if (f[i] == 1)
          return 0;
        else
          continue;
      }
      rlt = 1ll * rlt * expmod(2, g[i] - 1) % mod;
    }
  return rlt;
}
int main() {
  scanf("%d %d %d", &n, &m, &k);
  for (int i = 1; i <= k; i++) {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (n >= m)
      con[a][b] = c;
    else
      con[b][a] = c;
  }
  if (n < m) swap(n, m);
  scanf("%d", &mod);
  printf("%d\n", calc());
  return 0;
}
