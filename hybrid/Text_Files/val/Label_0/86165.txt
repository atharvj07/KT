#include <bits/stdc++.h>

using namespace std;

const int N = 256;
const int MOD = 1e9 + 7;

int n, k, a[N], f[N][N][N], fac[N];

int main() {
  fac[0] = 1;
  for (int i = 1; i < N; ++i) {
    fac[i] = (long long) i * fac[i - 1] % MOD;
  }
  cin >> n >> k;
  for (int i = 1; i <= n; ++i) {
    scanf("%d", a + i);
  }
  f[0][0][0] = 1;
  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j <= i; ++j) {
      for (int x = 0; x < N; ++x) {
        f[i][j][x] = f[i - 1][j][x];
        if (j) f[i][j][x] += f[i - 1][j - 1][x ^ a[i]];
        if (f[i][j][x] >= MOD) f[i][j][x] -= MOD;
      }
    }
  }
  int ans = 0;
  for (int i = 1; i <= n; ++i) {
    int cur = (long long) fac[i] * f[n][i][k] % MOD;
    ans += cur; if (ans >= MOD) ans -= MOD; 
  }
  cout << ans << '\n';
  return 0;
}

