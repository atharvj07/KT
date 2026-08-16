#include <bits/stdc++.h>
using namespace std;
struct Point {
  Point(int _x = 0, int _y = 0) : x(_x), y(_y) {}
  int x, y;
};
int table[8][8];
int dirx[4] = {-1, 0, 0, 1};
int diry[4] = {0, -1, 1, 0};
int main() {
  Point a[4];
  for (int i = 0; i < 4; ++i) {
    char x, y;
    scanf(" %c%c", &x, &y);
    a[i] = Point(x - 'a', y - '1');
  }
  swap(a[2], a[3]);
  Point a2 = a[2];
  bool checkmate = true;
  for (int dx = -1; dx <= 1; ++dx)
    for (int dy = -1; dy <= 1; ++dy) {
      a[2] = Point(a2.x + dx, a2.y + dy);
      if (a[2].x < 0 || a[2].x > 7 || a[2].y < 0 || a[2].y > 7) continue;
      memset(table, 0, sizeof(table));
      for (int i = 0; i < 4; ++i) {
        if (a[i].x == a[2].x && a[i].y == a[2].y) continue;
        table[a[i].x][a[i].y] = 1;
      }
      for (int i = 0; i < 4; ++i) {
        if (a[i].x == a[2].x && a[i].y == a[2].y) continue;
        if (i == 3) {
          for (int dx = -1; dx <= 1; ++dx)
            for (int dy = -1; dy <= 1; ++dy) {
              int xx = dx + a[i].x, yy = dy + a[i].y;
              if (xx < 0 || yy < 0 || xx > 7 || yy > 7) continue;
              table[xx][yy] = 1;
            }
        } else {
          for (int j = 0; j < 4; ++j) {
            int xx = a[i].x, yy = a[i].y;
            while (true) {
              xx += dirx[j], yy += diry[j];
              if (xx < 0 || yy < 0 || xx > 7 || yy > 7) break;
              if (table[xx][yy] == 1) break;
              table[xx][yy] = 2;
            }
          }
        }
      }
      if (table[a[2].x][a[2].y] == 0) checkmate = false;
    }
  if (checkmate)
    printf("CHECKMATE\n");
  else
    printf("OTHER\n");
}
