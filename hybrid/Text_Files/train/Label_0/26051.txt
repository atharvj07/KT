#include <bits/stdc++.h>
using namespace std;
int main() {
  int x1, y1, z1, x2, y2, z2;
  while (scanf("%d%d%d%d%d%d", &x1, &y1, &z1, &x2, &y2, &z2) != EOF) {
    if (x1 == x2 || y1 == y2 || z1 == z2) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }
  return 0;
}
