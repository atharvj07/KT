#include <bits/stdc++.h>
using namespace std;
const int N = 2e6 + 10, mod = 1e9 + 7;
int rd() {
  int x = 0, w = 1;
  char ch = 0;
  while (ch < '0' || ch > '9') {
    if (ch == '-') w = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    x = x * 10 + (ch ^ 48);
    ch = getchar();
  }
  return x * w;
}
int prm[N], pm[N], tt, n, a[N], c[N][2];
bool v[N];
int main() {
  for (int i = 2; i <= N - 5; ++i) {
    if (!pm[i]) pm[i] = prm[++tt] = i;
    for (int j = 1; i * prm[j] <= N - 5; ++j) {
      pm[i * prm[j]] = prm[j];
      if (i % prm[j] == 0) break;
    }
  }
  n = rd();
  for (int i = 1; i <= n; ++i) a[i] = rd();
  sort(a + 1, a + n + 1), reverse(a + 1, a + n + 1);
  for (int i = 1; i <= n; ++i) {
    if (!c[a[i]][0])
      v[i] = 1, c[a[i]][0] = c[a[i]][1] = 1;
    else {
      int x = a[i] - 1;
      while (x > 1) {
        int np = pm[x], cn = 0;
        while (pm[x] == np) ++cn, x /= np;
        if (c[np][0] < cn)
          c[np][0] = cn, c[np][1] = 1;
        else
          c[np][1] += c[np][0] == cn;
      }
    }
  }
  int ans = 1;
  for (int i = 2; i <= N - 5; ++i)
    for (int j = 1; j <= c[i][0]; ++j) ans = 1ll * ans * i % mod;
  for (int i = 1; i <= n; ++i)
    if (!v[i]) {
      int x = a[i] - 1, o = 1;
      while (x > 1) {
        int np = pm[x], cn = 0;
        while (pm[x] == np) ++cn, x /= np;
        o &= cn < c[np][0] || c[np][1] > 1;
      }
      if (o) {
        ans = (ans + o) % mod;
        break;
      }
    }
  printf("%d\n", ans);
  return 0;
}
