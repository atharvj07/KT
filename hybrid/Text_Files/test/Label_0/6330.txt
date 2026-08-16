#include <bits/stdc++.h>
using namespace std;
const int MAX = 40;
unsigned long long f[40][40];
unsigned long long st[40];
unsigned long long func(int n, int h) {
  if (f[n][h] != -1) return f[n][h];
  if (n < h || n > st[h] - 1) {
    f[n][h] = 0;
    return f[n][h];
  }
  unsigned long long ans = 0;
  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j <= min(i, h - 1); ++j)
      ans += func(i - 1, j) * func(n - i, h - 1);
    for (int j = 0; j <= min(n - 1, h - 1); ++j)
      ans += func(i - 1, h - 1) * func(n - i, j);
    ans -= func(i - 1, h - 1) * func(n - i, h - 1);
  }
  f[n][h] = ans;
  return f[n][h];
}
int main() {
  for (int i = 0; i < MAX; ++i)
    for (int j = 0; j < MAX; ++j) f[i][j] = -1;
  f[1][1] = 1;
  for (int i = 1; i < MAX; ++i) f[1][0] = 0;
  for (int i = 0; i < MAX; ++i) f[0][0] = 0;
  f[0][0] = 1;
  st[0] = 1;
  for (int i = 1; i < 40; ++i) st[i] = st[i - 1] * 2;
  unsigned long long ans = 0;
  int n, h;
  cin >> n >> h;
  for (int i = h; i <= n; ++i) func(n, i);
  for (int i = h; i <= n; ++i) ans += f[n][i];
  cout << ans << endl;
  return 0;
}
