#include <bits/stdc++.h>
using namespace std;
const int N = 210;
const int M = 300005;
const int mod = 1e9 + 7;
const int inf = 0x3f3f3f3f;
const long long oo = 0x3f3f3f3f3f3f3f3fll;
const double eps = 1e-6;
int n, k;
long long C[N][N], dp[N][N][5][3];
int getNum(int cur) {
  if (cur == 4) return 2;
  return 4 - cur;
}
int getCon(int cur) {
  if (cur == 0) return 4;
  if (cur == 1) return 2;
  if (cur == 2) return 1;
  return 0;
}
long long dfs(int n, int k, int cur, int type) {
  if (k == 0) return 1;
  long long& ret = dp[n][k][cur][type];
  if (ret + 1) return ret;
  ret = 0;
  if (type == 0) {
    int num = getNum(cur);
    for (int i = 0; i <= k && i <= num; i++) {
      (ret += dfs(n - 1, k - i, cur, 2) * C[num][i]) %= mod;
    }
  }
  if (type == 1) {
    if (n == 0) return ret = 0;
    int num = getNum(cur) * 2;
    int con = getCon(cur);
    for (int i = 0; i <= con && i <= k; i++)
      for (int j = 0; j <= num - i * 2 && j + i <= k; j++) {
        (ret += dfs(n, k - i - j, cur, 0) * C[con][i] * C[num - i * 2][j]) %=
            mod;
      }
  }
  if (type == 2) {
    (ret += dfs(n, k, cur, 1)) %= mod;
    if (cur == 0) {
      if (k >= 1) {
        (ret += dfs(n, k - 1, 1, 1) * 4) %= mod;
        (ret += dfs(n, k - 1, 2, 1) * 4) %= mod;
      }
      if (k >= 2) {
        (ret += dfs(n, k - 2, 2, 1) * 4) %= mod;
        (ret += dfs(n, k - 2, 3, 1) * 8) %= mod;
        (ret += dfs(n, k - 2, 4, 1) * 2) %= mod;
        if (k == 2) ret += 2, ret %= mod;
      }
      if (k >= 3) {
        (ret += dfs(n, k - 3, 3, 1) * 4) %= mod;
        if (k == 3) ret += 4, ret %= mod;
      }
      if (k == 4) ret++, ret %= mod;
    }
    if (cur == 1) {
      if (k >= 1) {
        (ret += dfs(n, k - 1, 2, 1) * 2) %= mod;
        (ret += dfs(n, k - 1, 3, 1) * 2) %= mod;
        (ret += dfs(n, k - 1, 4, 1) * 1) %= mod;
      }
      if (k >= 2) {
        if (k == 2) ret += 2, ret %= mod;
        (ret += dfs(n, k - 2, 3, 1) * 3) %= mod;
      }
      if (k == 3) ret++, ret %= mod;
    }
    if (cur == 2) {
      if (k >= 1) {
        (ret += dfs(n, k - 1, 3, 1) * 2) %= mod;
        if (k == 1) ret++, ret %= mod;
      }
      if (k == 2) ret++, ret %= mod;
    }
    if (cur == 3) {
      if (k == 1) ret++, ret %= mod;
    }
    if (cur == 4) {
      if (k >= 1) {
        (ret += (dfs(n, k - 1, 3, 1) * 2)) %= mod;
      }
      if (k >= 2) {
        if (k == 2) ret++, ret %= mod;
      }
    }
  }
  return ret;
}
int main() {
  for (int i = 0; i < N; i++) {
    C[i][0] = C[i][i] = 1;
    for (int j = 1; j < i; j++) C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod;
  }
  memset(dp, -1, sizeof(dp));
  scanf("%d%d", &n, &k);
  long long ret = 1;
  for (int i = 1; i <= k; i++) (ret *= i) %= mod;
  ret = ret * dfs(n, k, 0, 2) % mod;
  cout << ret << endl;
  return 0;
}
