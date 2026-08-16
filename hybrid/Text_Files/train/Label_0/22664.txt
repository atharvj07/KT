#include <bits/stdc++.h>
using namespace std;
int n;
const int MAXN = 2e2 + 10;
const long long mod = 1e9 + 7;
long long xi[MAXN];
long long yi[MAXN];
long long dp[MAXN][MAXN];
int lr[MAXN][MAXN][MAXN];
int hefa;
long long check(int i, int j, int k) {
  long long ax = xi[j] - xi[i];
  long long ay = yi[j] - yi[i];
  long long bx = xi[k] - xi[i];
  long long by = yi[k] - yi[i];
  long long sinz = ax * by - bx * ay;
  if (sinz > 0) sinz = 1;
  if (sinz < 0) sinz = -1;
  return sinz;
}
long long cnt(int i, int j) {
  long long ax = xi[i];
  long long ay = yi[i];
  long long bx = xi[j];
  long long by = yi[j];
  long long sinz = ax * by - bx * ay;
  return sinz;
}
long long dfs(int l, int r) {
  if (dp[l][r] >= 0) return dp[l][r];
  if (l == r)
    return dp[l][r] = 0;
  else if (l + 1 == r)
    return dp[l][r] = 1;
  long long res = 0;
  for (int i = l + 1; i < r; ++i) {
    if (!lr[l][r][i]) continue;
    res = (res + dfs(l, i) % mod * dfs(i, r) % mod) % mod;
  }
  return dp[l][r] = res;
}
int main() {
  while (cin >> n) {
    memset(dp, -1, sizeof dp);
    memset(lr, 0, sizeof lr);
    long long sum = 0;
    for (int i = 1; i <= n; ++i) {
      cin >> xi[i] >> yi[i];
      if (i != 1) {
        sum += cnt(i - 1, i);
      }
    }
    sum += cnt(n, 1);
    hefa = sum > 0 ? 1 : -1;
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        if (i == j) continue;
        for (int k = 1; k <= n; ++k) {
          if (k == j || k == i) continue;
          lr[i][j][k] = (check(i, k, j) == hefa) ? 1 : 0;
        }
      }
    }
    cout << dfs(1, n) << endl;
  }
  return 0;
}
