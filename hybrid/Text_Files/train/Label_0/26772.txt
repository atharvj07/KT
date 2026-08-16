#include <bits/stdc++.h>
using namespace std;
const int N = 300005;
const long long inf = 5e17, mx = 6e15;
inline long long read() {
  long long x = 0, f = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') x = x * 10 + ch - '0', ch = getchar();
  return x * f;
}
long long n, m, k, a[N], f[N][11], s[N], g[N][11];
void chkmax(long long &x, long long y) {
  if (x < y) x = y;
}
void solve() {
  n = read();
  m = read();
  k = read();
  for (int i = 1; i <= n; i++) {
    a[i] = read();
    s[i] = s[i - 1] + a[i];
  }
  long long ans = 0;
  for (int i = 1; i <= n; i++)
    for (int j = 0; j < m; j++) f[i][j] = -mx;
  for (int i = 1; i < m; i++)
    for (int j = i; j < m; j++) f[i][j] = -inf;
  for (int i = 1; i <= n; i++) {
    chkmax(f[i][0], max(f[i - 1][m - 1] + a[i] - k, a[i] - k));
    for (int j = 1; j < m && j < i; j++) {
      chkmax(f[i][j], f[i - 1][j - 1] + a[i]);
    }
    for (int j = 0; j < m; j++) ans = max(ans, f[i][j]);
  }
  cout << ans << endl;
}
int main() { solve(); }
