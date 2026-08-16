#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const int N = 505;
int f[2][N][N], p_2[N];
int main() {
  auto pow = [&](int a, int n) {
    int ans = 1;
    for (; n; n >>= 1, a = a * 1ll * a % mod)
      if (n & 1) ans = ans * 1ll * a % mod;
    return ans;
  };
  auto add = [&](int &x, int y) {
    x += y;
    if (x >= mod) x -= mod;
    return x;
  };
  int n, m;
  scanf("%d %d", &n, &m);
  p_2[0] = 1;
  for (int i = 1; i <= n; i++) p_2[i] = p_2[i - 1] * 2ll % mod;
  f[0][0][0] = 1;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= i + 1; j++) {
      for (int k = 0; k <= i + 1; k++) {
        f[(i + 1) & 1][j][k] = 0;
      }
    }
    for (int j = 0; j <= i; j++) {
      for (int k = 0; k <= i; k++) {
        add(f[(i + 1) & 1][j][k], f[i & 1][j][k] * 1ll * p_2[k] % mod);
        add(f[(i + 1) & 1][j + 1][i + 1],
            f[i & 1][j][k] * 1ll * p_2[k] % mod * (p_2[i + 1 - k] - 1) % mod);
      }
    }
  }
  int ans = 0;
  for (int i = 0; i <= n; i++) add(ans, f[n & 1][m][i]);
  cout << ans;
}
