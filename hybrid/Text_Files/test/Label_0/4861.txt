#include <bits/stdc++.h>
using namespace std;
int dp[111][111][111], fuck[111][111][111], vis1[111], vis2[111];
char s1[111], s2[111], s3[111];
int p[111];
int l1, l2, l3;
struct Pre {
  int x, y, z;
} pre[111][111][111];
int cnt;
void print(int x, int y, int z) {
  if (x == 0) return;
  print(pre[x][y][z].x, pre[x][y][z].y, pre[x][y][z].z);
  if (s1[x] == s2[y] && fuck[x][y][z] && !vis1[x] && !vis2[y])
    cnt++, printf("%c", s1[x]), vis1[x] = vis2[y] = 1;
}
void get_p() {
  int i, j = 0;
  p[1] = 0;
  for (i = 2; i <= l3; i++) {
    while (j && s3[i] != s3[j + 1]) j = p[j];
    if (s3[i] == s3[j + 1]) j++;
    p[i] = j;
  }
}
int main() {
  int i, j, k, l;
  while (scanf("%s%s%s", s1 + 1, s2 + 1, s3 + 1) != EOF) {
    l1 = strlen(s1 + 1);
    l2 = strlen(s2 + 1);
    l3 = strlen(s3 + 1);
    get_p();
    cnt = 0;
    memset(dp, -1, sizeof(dp));
    memset(fuck, 0, sizeof(fuck));
    dp[0][0][0] = 0;
    for (i = 0; i <= l1; i++)
      for (j = 0; j <= l2; j++)
        for (k = 0; k < l3; k++) {
          if (dp[i][j][k] == -1) continue;
          if (i < l1 && j < l2 && s1[i + 1] == s2[j + 1]) {
            if (k + 1 < l3 && s3[k + 1] == s1[i + 1]) {
              dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1;
              fuck[i + 1][j + 1][k + 1] = 1;
              pre[i + 1][j + 1][k + 1].x = i;
              pre[i + 1][j + 1][k + 1].y = j;
              pre[i + 1][j + 1][k + 1].z = k;
            } else if (s3[k + 1] != s1[i + 1]) {
              int t = k;
              while (t && s3[t + 1] != s1[i + 1]) t = p[t];
              if (s3[t + 1] == s1[i + 1]) t++;
              if (dp[i + 1][j + 1][t] < dp[i][j][k] + 1) {
                dp[i + 1][j + 1][t] = dp[i][j][k] + 1;
                fuck[i + 1][j + 1][t] = 1;
                pre[i + 1][j + 1][t].x = i;
                pre[i + 1][j + 1][t].y = j;
                pre[i + 1][j + 1][t].z = k;
              }
            }
            if (dp[i + 1][j + 1][k] < dp[i][j][k]) {
              dp[i + 1][j + 1][k] = dp[i][j][k];
              pre[i + 1][j + 1][k].x = i;
              pre[i + 1][j + 1][k].y = j;
              pre[i + 1][j + 1][k].z = k;
            }
          } else {
            if (i < l1 && dp[i + 1][j][k] < dp[i][j][k]) {
              dp[i + 1][j][k] = dp[i][j][k];
              pre[i + 1][j][k].x = i;
              pre[i + 1][j][k].y = j;
              pre[i + 1][j][k].z = k;
            }
            if (j < l2 && dp[i][j + 1][k] < dp[i][j][k]) {
              dp[i][j + 1][k] = dp[i][j][k];
              pre[i][j + 1][k].x = i;
              pre[i][j + 1][k].y = j;
              pre[i][j + 1][k].z = k;
            }
          }
        }
    int ans = 0;
    for (i = 0; i <= l1; i++)
      for (j = 0; j <= l2; j++)
        for (k = 0; k <= l3; k++) {
        }
    for (i = 1; i < l3; i++)
      if (dp[l1][l2][i] > dp[l1][l2][ans]) ans = i;
    if (dp[l1][l2][ans] <= 0)
      printf("0");
    else
      print(l1, l2, ans);
    puts("");
  }
}
