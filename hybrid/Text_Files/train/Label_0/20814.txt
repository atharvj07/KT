#include <bits/stdc++.h>
using namespace std;
int main() {
  int x, y, x1, x2, y1, y2;
  scanf("%d %d", &x, &y);
  if (x > 0 && y > 0) {
    x1 = 0;
    x2 = x + y;
    y2 = 0;
    y1 = x + y;
  } else if (x < 0 && y > 0) {
    x = -1 * x;
    x1 = -1 * (x + y);
    y1 = 0;
    x2 = 0;
    y2 = x + y;
  } else if (x < 0 && y < 0) {
    x = -1 * x;
    y = -1 * y;
    x1 = -1 * (x + y);
    x2 = 0;
    y1 = 0;
    y2 = -1 * (x + y);
  } else {
    y = y * -1;
    x1 = 0;
    x2 = x + y;
    y1 = -1 * (x + y);
    y2 = 0;
  }
  printf("%d %d %d %d\n", x1, y1, x2, y2);
  return 0;
}
