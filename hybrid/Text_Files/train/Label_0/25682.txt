#include <bits/stdc++.h>
#pragma GCC target("avx2")
#pragma GCC optimization("O3")
#pragma GCC optimization("unroll-loops")
using namespace std;
long long a[10][10];
long double dp[10][10];
bool vis[10][10];
long double solve(long long i, long long j) {
  if (i == 9 && j == 9) return 0;
  if (vis[i][j]) return dp[i][j];
  long long cord = i * 10 + j;
  vis[i][j] = 1;
  long double cur = 0;
  long long cnt = 0;
  for (long long k = 1; k < 7; k++) {
    long long x = (cord + k) / 10, y = (cord + k) % 10;
    if (x <= 9)
      if (a[x][y]) {
        int t = a[x][y] % 2;
        if (t)
          cur = cur + (min(solve(x, y), solve(x + a[x][y], 9 - y)) + 1.0) / 6.0;
        else
          cur = cur + (min(solve(x, y), solve(x + a[x][y], y)) + 1.0) / 6.0;
      } else
        cur = cur + (solve(x, y) + 1.0) / 6.0;
    else
      cnt++;
  }
  cur = ((cur + ((cnt * 1.0) / 6.0)) * 6.0) / (6.0 - cnt);
  return dp[i][j] = cur;
}
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int TESTS = 1;
  while (TESTS--) {
    for (long long i = 0LL; i < 10LL; i++)
      for (long long j = 0LL; j < 10LL; j++) cin >> a[i][j];
    reverse(a, a + 10);
    for (long long i = 1; i < 10; i++) reverse(a[i], a[i] + 10), i++;
    int cur = 0;
    cout << setprecision(14);
    cout << fixed << solve(0, 0);
  }
  return 0;
}
