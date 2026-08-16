#include <bits/stdc++.h>
using namespace std;
inline int read() {
  int ret = 0, f = 1;
  char ch = getchar();
  while (ch > '9' || ch < '0') {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    ret = (ret << 1) + (ret << 3) + ch - '0';
    ch = getchar();
  }
  return ret * f;
}
int n, ans[51][51][51];
void solve(int n) {
  if (n == 1) {
    ans[0][0][0] = 0;
    ans[0][1][0] = 1;
    return;
  }
  solve(n - 1);
  static int a[51][51][51];
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      for (int k = 0; k < n; k++) a[i][j][k] = ans[i][j][k];
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (i & 1)
        ans[i][0][n - 1 - j] = cnt++;
      else
        ans[i][0][j] = cnt++;
    }
  }
  if (n & 1) {
    for (int i = 0; i < n - 1; i++)
      for (int j = 0; j < n; j++)
        for (int k = 0; k < n - 1; k++)
          ans[n - 1 - k][i + 1][n - 1 - j] = a[i][j][k] + cnt;
    cnt += n * (n - 1) * (n - 1);
    for (int i = 1; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (i & 1)
          ans[0][i][j] = cnt++;
        else
          ans[0][i][n - 1 - j] = cnt++;
      }
    }
    for (int i = 0; i < n; i++) ans[i][n][0] = cnt++;
    for (int i = n - 1; i >= 0; i--) {
      for (int j = 1; j < n; j++) {
        if (~i & 1)
          ans[i][n][j] = cnt++;
        else
          ans[i][n][n - j] = cnt++;
      }
    }
  } else {
    for (int i = 0; i < n - 1; i++)
      for (int j = 0; j < n; j++)
        for (int k = 0; k < n - 1; k++)
          ans[n - 1 - k][i + 1][j] = a[i][j][k] + cnt;
    cnt += n * (n - 1) * (n - 1);
    for (int i = 1; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (~i & 1)
          ans[0][i][j] = cnt++;
        else
          ans[0][i][n - 1 - j] = cnt++;
      }
    }
    for (int j = 0; j < n; j++) {
      for (int i = 0; i < n; i++) {
        if (~j & 1)
          ans[i][n][j] = cnt++;
        else
          ans[n - 1 - i][n][j] = cnt++;
      }
    }
  }
}
int main() {
  n = read();
  solve(n);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      for (int k = 0; k < n; k++) {
        printf("%d", ans[i][j][k] + 1);
        putchar((k == n - 1) ? '\n' : ' ');
      }
    }
    if (i + 1 < n) puts("");
  }
  return 0;
}
