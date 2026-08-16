#include <bits/stdc++.h>
using namespace std;
const int N = 41414;
bool a[N][320], as[N][320];
int n, m, k, ty, tl, t, z, mx;
bool pd(int k) {
  if (k < 0 || k == 1 || k == 2 || k == 5 || k == 4 ||
      k == 8 && n != 3 && m != 3)
    return 1;
  return 0;
}
void dfs(int x, int y, int ct) {
  if (tl) return;
  if ((x != 1 || y != 1) && ct == k) {
    tl = 1;
    for (int i = (1); i <= (n); i++)
      for (int j = (1); j <= (m); j++) as[i][j] = a[i][j];
    return;
  }
  if (x > n) return;
  if (y > m) return dfs(x + 1, 1, ct);
  if (++z > mx) return;
  t = 0;
  if (a[x - 1][y]) t += a[x][y + 1] + a[x - 1][y - 1] + a[x - 1][y + 1];
  if (a[x + 1][y]) t += a[x][y - 1] + a[x + 1][y - 1] + a[x + 1][y + 1];
  if (a[x][y - 1]) t += a[x - 1][y] + a[x - 1][y - 1] + a[x + 1][y - 1];
  if (a[x][y + 1]) t += a[x - 1][y + 1] + a[x + 1][y] + a[x + 1][y + 1];
  if (ct + t <= k && (x < 2 || y < 2 || a[x - 1][y] || a[x][y - 1])) {
    a[x][y] = 1;
    dfs(x, y + 1, ct + t);
    a[x][y] = 0;
  }
  dfs(x, y + 1, ct);
}
int main() {
  int t;
  cin >> t;
  while (t--) {
    scanf("%d%d%d", &n, &m, &k);
    z = tl = ty = 0;
    if (n < m) ty = 1, swap(n, m);
    if (pd((n - 1) * (m - 1) * 4 - k) && n > 5 && m > 5) {
      puts("-1");
      continue;
    }
    mx = 8 * n * m, dfs(1, 1, 0);
    if (!tl)
      puts("-1");
    else if (ty)
      for (int j = (1); j <= (m); j++) {
        for (int i = (1); i <= (n); i++) putchar(as[i][j] ? '*' : '.');
        puts("");
      }
    else
      for (int i = (1); i <= (n); i++) {
        for (int j = (1); j <= (m); j++) putchar(as[i][j] ? '*' : '.');
        puts("");
      }
    puts("");
  }
}
