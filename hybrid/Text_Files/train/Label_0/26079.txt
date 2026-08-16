#include <bits/stdc++.h>
using namespace std;
char maze[2005][2005];
int cnt = 0, n, m;
bool check(int x, int y, int sz) {
  int i, num = 0;
  for (i = 0; i < sz; ++i)
    if (maze[x + i][y] == 'w') num++;
  for (i = 1; i < sz; ++i) {
    if (maze[x][y + i] == 'w') num++;
    if (maze[x + sz - 1][y + i] == 'w') num++;
  }
  for (i = 1; i < sz - 1; ++i)
    if (maze[x + i][y + sz - 1] == 'w') num++;
  return num == cnt;
}
void output(int x, int y, int sz) {
  int i;
  for (i = 0; i < sz; ++i)
    if (maze[x + i][y] != 'w') maze[x + i][y] = '+';
  for (i = 1; i < sz; ++i) {
    if (maze[x][y + i] != 'w') maze[x][y + i] = '+';
    if (maze[x + sz - 1][y + i] != 'w') maze[x + sz - 1][y + i] = '+';
  }
  for (i = 1; i < sz - 1; ++i)
    if (maze[x + i][y + sz - 1] != 'w') maze[x + i][y + sz - 1] = '+';
  for (i = 0; i < n; ++i) printf("%s\n", maze[i]);
}
int main() {
  int i, j;
  scanf("%d%d", &n, &m);
  for (i = 0; i < n; ++i) scanf("%s", maze[i]);
  for (i = 0; i < n; ++i)
    for (j = 0; j < m; ++j)
      if (maze[i][j] == 'w') cnt++;
  int up = -1, down = -1;
  for (i = 0; i < n && up == -1; ++i) {
    for (j = 0; j < m; ++j)
      if (maze[i][j] == 'w') {
        up = i;
        break;
      }
  }
  for (i = n - 1; i >= 0 && down == -1; --i) {
    for (j = 0; j < m; ++j)
      if (maze[i][j] == 'w') {
        down = i;
        break;
      }
  }
  int left = -1, right = -1;
  for (j = 0; j < m && left == -1; ++j) {
    for (i = 0; i < n; ++i)
      if (maze[i][j] == 'w') {
        left = j;
        break;
      }
  }
  for (j = m - 1; j >= 0 && right == -1; --j) {
    for (i = 0; i < n; ++i)
      if (maze[i][j] == 'w') {
        right = j;
        break;
      }
  }
  int sz = max(down - up + 1, right - left + 1);
  int x, y;
  if (down - up > right - left) {
    x = up;
    for (y = 0; y + sz - 1 < m; ++y)
      if (check(x, y, sz)) {
        output(x, y, sz);
        return 0;
      }
  } else {
    y = left;
    for (x = 0; x + sz - 1 < n; ++x)
      if (check(x, y, sz)) {
        output(x, y, sz);
        return 0;
      }
  }
  puts("-1");
  return 0;
}
