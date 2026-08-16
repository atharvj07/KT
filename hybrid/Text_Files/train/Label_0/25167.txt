#include <bits/stdc++.h>
using namespace std;
int n, c[51], pos[2501][3], a[51][51], change[2501][5], sum;
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d", &c[i]);
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= c[i]; j++)
      scanf("%d", &a[i][j]), pos[a[i][j]][1] = i, pos[a[i][j]][2] = j;
  sum = 0;
  int cnt = 0;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= c[i]; j++)
      if (a[i][j] != ++cnt) {
        change[++sum][1] = i;
        change[sum][2] = j;
        change[sum][3] = pos[cnt][1];
        change[sum][4] = pos[cnt][2];
        a[pos[cnt][1]][pos[cnt][2]] = a[i][j];
        pos[a[i][j]][1] = pos[cnt][1];
        pos[a[i][j]][2] = pos[cnt][2];
        a[i][j] = cnt;
        pos[cnt][1] = i;
        pos[cnt][2] = j;
      }
  printf("%d\n", sum);
  for (int i = 1; i <= sum; i++)
    printf("%d %d %d %d\n", change[i][1], change[i][2], change[i][3],
           change[i][4]);
}
