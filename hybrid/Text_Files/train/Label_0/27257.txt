#include <bits/stdc++.h>
char s[110][110];
int a[1000010];
int d[110][110];
int dp[1000010], pv[1000010];
void go(int x) {
  if (pv[x] != -1) {
    go(pv[x]);
  }
  printf("%d ", a[x] + 1);
}
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%s", s[i]);
    for (int j = 0; j < n; j++) {
      d[i][j] = s[i][j] - '0' ? 1 : 1000000;
      if (i == j) d[i][j] = 0;
    }
  }
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (d[i][j] > d[i][k] + d[k][j]) d[i][j] = d[i][k] + d[k][j];
      }
    }
  }
  int m;
  scanf("%d", &m);
  for (int i = 0; i < m; i++) {
    scanf("%d", &a[i]);
    --a[i];
  }
  dp[0] = 1;
  pv[0] = -1;
  for (int i = 1; i < m; i++) {
    dp[i] = m + 1;
    for (int j = i - 1; j >= 0; j--) {
      if (i - j >= n) break;
      if (d[a[j]][a[i]] == i - j && dp[i] > dp[j] + 1) {
        dp[i] = dp[j] + 1;
        pv[i] = j;
      }
    }
  }
  printf("%d\n", dp[m - 1]);
  go(m - 1);
  return 0;
}
