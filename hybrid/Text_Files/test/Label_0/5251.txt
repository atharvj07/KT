#include <bits/stdc++.h>
using namespace std;
inline int rd() {
  char c = getchar();
  while (!isdigit(c)) c = getchar();
  int x = c - '0';
  while (isdigit(c = getchar())) x = x * 10 + c - '0';
  return x;
}
inline void upmax(int& a, int b) {
  if (a < b) a = b;
}
const int maxn = 403;
int n, m;
int a[maxn][maxn], f[maxn][maxn], pre[maxn][maxn * maxn + 1];
void input() {
  n = rd(), m = rd();
  for (int i = 1, _ = n; i <= _; i++)
    for (int j = 1, _ = m; j <= _; j++) a[i][j] = rd();
}
void solve() {
  int ans = 0;
  for (int i = 1, _ = n; i <= _; i++) {
    for (int j = 1, _ = m; j <= _; j++) {
      upmax(f[j][j], pre[j][a[i][j]]);
      upmax(ans, i - f[j][j]);
    }
    for (int len = 1, _ = m - 1; len <= _; len++)
      for (int l = 1, _ = m - len; l <= _; l++) {
        int r = l + len;
        if (a[i][l] == a[i][r]) f[l][r] = i;
        upmax(f[l][r], max(f[l + 1][r], f[l][r - 1]));
        upmax(f[l][r], max(pre[r][a[i][l]], pre[l][a[i][r]]));
        upmax(ans, (i - f[l][r]) * (len + 1));
      }
    for (int j = 1, _ = m; j <= _; j++) pre[j][a[i][j]] = i;
  }
  printf("%d\n", ans);
}
int main() {
  input();
  solve();
  return 0;
}
