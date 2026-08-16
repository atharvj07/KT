#include <bits/stdc++.h>
using namespace std;
namespace Sweet {
template <typename T>
inline void read(T &x) {
  char ch;
  int f = 1;
  while (ch = getchar(), ch > '9' || ch < '0')
    if (ch == '-') f = -1;
  x = (ch ^ 48);
  while (ch = getchar(), ch >= '0' && ch <= '9') x = x * 10 + (ch ^ 48);
  x *= f;
}
template <typename T>
inline void write(T x) {
  static int stk[100], top = 0;
  if (x == 0) return (void)putchar('0');
  if (x < 0) x = -x, putchar('-');
  while (x) stk[++top] = x % 10, x /= 10;
  while (top) putchar(stk[top--] + '0');
}
const int N = 5e2 + 10, inf = 0x3f3f3f3f;
int n, v[N], w[N], dp[N], f[N][N][2];
bool vis[N][N][2];
inline void max(int &x, const int &y) { x = x < y ? y : x; }
int solve(int l, int r, bool flag) {
  int &tmp = f[l][r][flag];
  if (vis[l][r][flag]) return tmp;
  tmp = -inf, vis[l][r][flag] = true;
  if (l >= r) return tmp = 0;
  if (flag) {
    if (l == r - 1) return tmp = 0;
    if (w[l] == w[r - 1]) return tmp;
    int delta = (w[l] < w[r - 1]) ? 1 : -1;
    for (int i = l + 1; i < r; ++i) {
      if (w[l] + delta == w[i]) {
        max(tmp, solve(l + 1, i, false) + solve(i, r, true));
      }
    }
  } else {
    for (int i = l + 1; i < r; ++i)
      max(tmp, solve(l, i, false) + solve(i, r, false));
    for (int i = l, t; i < r; ++i) {
      if (w[i] >= w[l] && w[i] >= w[r - 1] &&
          (t = 2 * w[i] - w[l] - w[r - 1]) < n) {
        max(tmp, solve(l, i + 1, true) + solve(i, r, true) + v[t]);
      }
    }
  }
  return tmp;
}
inline void main() {
  read(n);
  for (int i = 0; i < n; ++i) read(v[i]);
  for (int i = 1; i <= n; ++i) read(w[i]);
  memset(vis, false, sizeof(vis));
  memset(dp, 0xcf, sizeof(dp));
  dp[0] = 0;
  for (int i = 1; i <= n; ++i) {
    max(dp[i], dp[i - 1]);
    for (int j = i; j <= n; ++j) {
      max(dp[j], dp[i - 1] + solve(i, j + 1, 0));
    }
  }
  write(dp[n]);
}
}  // namespace Sweet
int main() {
  Sweet::main();
  return 0;
}
