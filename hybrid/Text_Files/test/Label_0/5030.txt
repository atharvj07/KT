#include <bits/stdc++.h>
using namespace std;
long long mod = 1e9 + 7, n, a[505][505], f[505][505], g[505][505];
int main() {
  scanf("%lld", &n);
  for (register int i = 1; i <= n; i++) {
    for (register int j = 1; j <= n; j++) {
      scanf("%lld", &a[i][j]);
    }
  }
  for (register int i = 1; i <= n; i++) {
    f[i][i] = 1;
  }
  for (register int len = 2; len <= n; len++) {
    for (register int l = 1; l + len - 1 <= n; l++) {
      int r = l + len - 1;
      if (a[l][r]) {
        for (register int k = l; k < r; k++) {
          f[l][r] = (f[l][r] +
                     (f[l][k] + g[l][k]) * (f[k + 1][r] + g[k + 1][r]) % mod) %
                    mod;
        }
      }
      for (register int k = l + 1; k < r; k++) {
        if (a[l][k]) {
          g[l][r] = (g[l][r] + f[l][k] * (g[k][r] + f[k][r]) % mod) % mod;
        }
      }
    }
  }
  printf("%lld\n", (f[1][n] + g[1][n]) % mod);
  return 0;
}
