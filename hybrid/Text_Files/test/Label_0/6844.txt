#include <bits/stdc++.h>
using namespace std;
int main() {
  int r, g, b;
  scanf("%d%d%d", &r, &g, &b);
  int ans = 0;
  if (r < g) swap(r, g);
  if (g < b) swap(g, b);
  if (r < g) swap(r, g);
  if (b) {
    ans += b;
    r -= b;
    g -= b;
  }
  int te = min(r / 2, g);
  ans += te;
  r -= te * 2;
  g -= te;
  if (r == 1 && g >= 2) {
    ans += 1;
    r -= 1;
    g -= 2;
  }
  if (r < g) {
    ans += min(g / 3, te);
    g -= 3 * min(g / 3, te);
    swap(r, g);
  }
  if (r >= 3) ans += min(r / 3, b);
  printf("%d\n", ans);
}
