#include <bits/stdc++.h>
const int MOD = 1000000007;
const int SIZE_N = 2000 + 10;
int n;
int ary[SIZE_N];
int vis[SIZE_N];
int fac[SIZE_N];
int madd(long long a, long long b) { return (a + b) % MOD; }
int mmul(long long a, long long b) { return (a * b) % MOD; }
int dp[SIZE_N][SIZE_N], v[SIZE_N][SIZE_N];
int f(int a, int b) {
  if (v[a][b] == 1) return dp[a][b];
  v[a][b] = 1;
  if (a == 0) return dp[a][b] = fac[b];
  if (a == 1) return dp[a][b] = mmul(b, fac[b]);
  return dp[a][b] = madd(mmul(b, f(a - 1, b)), mmul(a - 1, f(a - 2, b + 1)));
}
int main(void) {
  fac[0] = 1;
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", ary + i);
    vis[ary[i]] = 1;
    fac[i] = mmul(fac[i - 1], i);
  }
  int a = 0, b = 0;
  for (int i = 1; i <= n; ++i) {
    if (vis[i] == 1) continue;
    if (ary[i] == -1)
      ++a;
    else
      ++b;
  }
  int ans = 0;
  ans = f(a, b);
  printf("%d\n", ans);
  return 0;
}
