#include <bits/stdc++.h>
using namespace std;
const int N = 210;
char s[N][N];
char str[3][N][N];
int main() {
  int n, m;
  scanf("%d%d", &m, &n);
  for (int i = 1; i <= n; i++) scanf("%s", s[i] + 1);
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++) str[0][j][n - i + 1] = s[i][j];
  swap(n, m);
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++) str[1][i][m - j + 1] = str[0][i][j];
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) printf("%c%c", str[1][i][j], str[1][i][j]);
    printf("\n");
    for (int j = 1; j <= m; j++) printf("%c%c", str[1][i][j], str[1][i][j]);
    printf("\n");
  }
  return 0;
}
