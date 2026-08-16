#include <bits/stdc++.h>
using namespace std;
int n, m, f[100510][2];
char ch[4][100510];
int main() {
  scanf("%d%d%*d", &n, &m);
  scanf("%s%s%s%s", ch[0] + 1, ch[1] + 1, ch[2] + 1, ch[3] + 1);
  for (int i = 1; i <= m; i++) {
    if (ch[2][i] == 'R')
      f[1][1]++;
    else
      f[1][0]++;
  }
  if (ch[0][1] == 'R')
    f[1][1]++;
  else
    f[1][0]++;
  if (ch[1][1] == 'R')
    f[1][1]++;
  else
    f[1][0]++;
  for (int i = 2; i <= n; i++) {
    int c0 = 0, c1 = 0;
    if (ch[0][i] == 'R')
      c1++;
    else
      c0++;
    if (ch[1][i] == 'R')
      c1++;
    else
      c0++;
    f[i][1] = min(f[i - 1][0] + m, f[i - 1][1]) + c1;
    f[i][0] = min(f[i - 1][1] + m, f[i - 1][0]) + c0;
  }
  for (int i = 1; i <= m; i++) {
    if (ch[3][i] == 'R')
      f[n][1]++;
    else
      f[n][0]++;
  }
  int ans = min(f[n][0], f[n][1]);
  memset(f, 0, sizeof(f));
  for (int i = 1; i <= n; i++) {
    if (ch[0][i] == 'R')
      f[1][1]++;
    else
      f[1][0]++;
  }
  if (ch[2][1] == 'R')
    f[1][1]++;
  else
    f[1][0]++;
  if (ch[3][1] == 'R')
    f[1][1]++;
  else
    f[1][0]++;
  for (int i = 2; i <= m; i++) {
    int c0 = 0, c1 = 0;
    if (ch[2][i] == 'R')
      c1++;
    else
      c0++;
    if (ch[3][i] == 'R')
      c1++;
    else
      c0++;
    f[i][0] = min(f[i - 1][0], f[i - 1][1] + n) + c0;
    f[i][1] = min(f[i - 1][1], f[i - 1][0] + n) + c1;
  }
  for (int i = 1; i <= n; i++) {
    if (ch[1][i] == 'R')
      f[m][1]++;
    else
      f[m][0]++;
  }
  ans = min(ans, min(f[m][0], f[m][1]));
  printf("%d\n", ans);
}
