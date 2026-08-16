#include <bits/stdc++.h>
using namespace std;
int n;
char a[55][55];
int f[55][55][55][55], s[55][55];
int black(int x, int y, int u, int v) {
  return s[u][v] - s[x - 1][v] - s[u][y - 1] + s[x - 1][y - 1];
}
int main() {
  cin >> n;
  for (int i = 1; i <= n; ++i) cin >> a[i] + 1;
  for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= n; ++j) {
      s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1];
      s[i][j] += (a[i][j] == '#');
    }
  for (int u = 1; u <= n; ++u)
    for (int v = 1; v <= n; ++v)
      for (int x = u; x >= 1; --x)
        for (int y = v; y >= 1; --y) {
          int ans = 0;
          if (!black(x, y, u, v)) goto L1;
          ans = max(u - x + 1, v - y + 1);
          for (int k = x; k <= u - 1; ++k)
            ans = min(ans, f[x][y][k][v] + f[k + 1][y][u][v]);
          for (int k = y; k <= v - 1; ++k)
            ans = min(ans, f[x][y][u][k] + f[x][k + 1][u][v]);
        L1:;
          f[x][y][u][v] = ans;
        }
  cout << f[1][1][n][n];
}
