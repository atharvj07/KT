#include <bits/stdc++.h>
using namespace std;
char mat[1005][1005];
int op[4][2] = {1, 0, -1, 0, 0, 1, 0, -1};
int m, n;
int checkrow(int i) {
  int flag = 0;
  for (int j = 1; j <= m; j++) {
    if (flag == 0) {
      if (mat[i][j] == '#') flag++;
    } else if (flag == 1) {
      if (mat[i][j] == '.') flag++;
    } else if (flag == 2) {
      if (mat[i][j] == '#') return -1;
    }
  }
  if (flag == 0)
    return 0;
  else
    return 1;
}
int checkcol(int j) {
  int flag = 0;
  for (int i = 1; i <= n; i++) {
    if (flag == 0) {
      if (mat[i][j] == '#') flag++;
    } else if (flag == 1) {
      if (mat[i][j] == '.') flag++;
    } else if (flag == 2) {
      if (mat[i][j] == '#') return -1;
    }
  }
  if (flag == 0)
    return 0;
  else
    return 1;
}
bool check(int i, int j) { return (i > 0 && i <= n && j > 0 && j <= m); }
void dfs(int i, int j) {
  for (int k = 0; k < 4; k++) {
    if (!check(i + op[k][0], j + op[k][1])) continue;
    if (mat[i + op[k][0]][j + op[k][1]] == '#') {
      mat[i + op[k][0]][j + op[k][1]] = '*';
      dfs(i + op[k][0], j + op[k][1]);
    }
  }
  return;
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) {
    scanf("%s", mat[i] + 1);
  }
  int fl = 1;
  int colblank = 0;
  int rowblank = 0;
  for (int i = 1; i <= n; i++) {
    int p = checkrow(i);
    if (p == 0)
      rowblank++;
    else if (p == -1)
      fl = -1;
  }
  for (int j = 1; j <= m; j++) {
    int p = checkcol(j);
    if (p == 0)
      colblank++;
    else if (p == -1)
      fl = -1;
  }
  if (fl == -1 || (colblank && !rowblank) || (!colblank && rowblank)) {
    printf("-1\n");
  } else {
    int ans = 0;
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        if (mat[i][j] == '#') {
          ans++;
          mat[i][j] = '*';
          dfs(i, j);
        }
      }
    }
    printf("%d\n", ans);
  }
  return 0;
}
