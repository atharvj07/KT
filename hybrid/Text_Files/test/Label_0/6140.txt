#include <bits/stdc++.h>
using namespace std;
int n, m, xx1, yy1, xx2, yy2;
int main() {
  cin >> n >> m;
  cin >> xx1 >> yy1 >> xx2 >> yy2;
  int dx = abs(xx1 - xx2), dy = abs(yy1 - yy2);
  if (dx > dy) {
    swap(dx, dy);
  }
  int mx;
  if (dx == 0) {
    mx = 4;
  } else if (dx == 1) {
    mx = 5;
  } else {
    mx = 6;
  }
  if (dx + dy <= mx) {
    puts("First");
  } else {
    puts("Second");
  }
  return 0;
}
