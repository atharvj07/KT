#include <bits/stdc++.h>
using namespace std;
const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
struct Point {
  int x, y;
} Q[2000 * 2000], P, np;
int n, m;
int b[2000][2000];
int mark[2000][2000], T;
int L[2000 * 2000];
int flag[2000][2000];
bool out(int x, int y) { return x < 0 || y < 0 || x >= n || y >= m; }
void Mark(int x, int y) {
  int head, tail;
  int d, i, j, k;
  head = tail = 0;
  Q[tail].x = x;
  Q[tail].y = y;
  tail++;
  while (head < tail) {
    P = Q[head++];
    for (d = 0; d < 4; d++) {
      np.x = P.x + dx[d];
      np.y = P.y + dy[d];
      if (out(np.x, np.y) || b[np.x][np.y] == 0) continue;
      if (mark[np.x][np.y] != T) {
        mark[np.x][np.y] = T;
        Q[tail++] = np;
      }
    }
  }
}
int count(int x, int y) {
  int i, j, nx, ny;
  int cnt(0);
  int dx, dy;
  for (i = -2; i <= 2; i++)
    for (j = -2; j <= 2; j++) {
      nx = x + i;
      ny = y + j;
      if (out(nx, ny)) continue;
      if (mark[nx][ny] == mark[x][y]) cnt++;
    }
  if (cnt != 9) return false;
  for (dx = -1; dx <= 1; dx += 2)
    for (dy = -1; dy <= 1; dy += 2) {
      for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
          nx = x + dx * i;
          ny = y + dy * j;
          if (out(nx, ny) || b[nx][ny] == 0) break;
          if (mark[nx][ny] != mark[x][y]) break;
        }
        if (j < 3) break;
      }
      if (i == 3) return true;
    }
  return false;
}
int remove(int x, int y) {
  int head, tail;
  int d, i, j, k;
  head = tail = 0;
  Q[tail].x = x;
  Q[tail].y = y;
  tail++;
  flag[x][y] = true;
  for (k = 0; k < 10; k++) {
    for (i = tail; head < i; head++) {
      P = Q[head];
      for (d = 0; d < 4; d++) {
        np.x = P.x + dx[d];
        np.y = P.y + dy[d];
        if (out(np.x, np.y) || b[np.x][np.y] == 0) continue;
        if (mark[np.x][np.y] != mark[x][y]) continue;
        if (flag[np.x][np.y] == false) {
          flag[np.x][np.y] = true;
          Q[tail++] = np;
        }
      }
    }
  }
  return tail <= 40;
}
int main() {
  int i, j, k, d;
  int cnt, x, y;
  scanf("%d%d", &n, &m);
  for (i = 0; i < n; i++)
    for (j = 0; j < m; j++) scanf("%d", b[i] + j);
  for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++) {
      if (b[i][j] == 0 || mark[i][j]) continue;
      T++;
      Mark(i, j);
    }
  }
  printf("%d\n", T);
  for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++) {
      cnt = 0;
      if (!mark[i][j] || flag[i][j]) continue;
      for (d = 0; d < 4; d++) {
        x = i + dx[d];
        y = j + dy[d];
        if (out(x, y)) continue;
        cnt += b[x][y];
      }
      if (cnt >= 3) continue;
      if (count(i, j) && remove(i, j)) {
        L[mark[i][j]]++;
      }
    }
  }
  sort(L + 1, L + T + 1);
  for (i = 1; i <= T; i++) {
    if (i > 1) printf(" ");
    printf("%d", L[i]);
  }
  printf("\n");
}
