#include <bits/stdc++.h>
using namespace std;
const int N = 1 << 18;
int a[N], pre[N], p[N], pos[N];
int fa[N][20], dp[N][20];
int rmq(int l, int r) {
  int k = 31 - __builtin_clz(r - l + 1);
  return max(dp[l][k], dp[r - (1 << k) + 1][k]);
}
int main() {
  int n, m, q;
  scanf("%d%d%d", &n, &m, &q);
  for (int i = 1; i <= n; i++) scanf("%d", &p[i]), pre[p[i]] = p[i - 1];
  pre[p[1]] = p[n];
  for (int i = 1, x; i <= m; i++) {
    scanf("%d", &x);
    fa[i][0] = pos[pre[x]];
    for (int j = 1; j < 20; j++) fa[i][j] = fa[fa[i][j - 1]][j - 1];
    pos[x] = i;
  }
  for (int i = 1; i <= m; i++) {
    int x = i, k = n - 1;
    for (int j = 19; j >= 0; j--)
      if (k >> j & 1) x = fa[x][j];
    dp[i][0] = x;
  }
  for (int j = 1; (1 << j) <= m; j++)
    for (int i = 1; i + (1 << j) - 1 <= m; i++)
      dp[i][j] = max(dp[i][j - 1], dp[i + (1 << (j - 1))][j - 1]);
  for (int i = 0, l, r; i < q; i++) {
    scanf("%d%d", &l, &r);
    putchar(rmq(l, r) >= l ? '1' : '0');
  }
}
