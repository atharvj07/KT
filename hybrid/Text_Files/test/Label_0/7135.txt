#include <bits/stdc++.h>
using namespace std;
int g[200005];
int f(int x) {
  return g[x] == x ? x : g[x] = f(g[x]);
}
int main() {
  for (int i = 1; i <= 200000; i++) {
    g[i] = i;
  }
  int n, m, k, x;
  scanf("%d %d", &n, &m);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &k);
    for (int j = 1; j <= k; j++) {
      scanf("%d", &x);
      int y = f(100000 + x);
      int z = f(i);
      if (y != z) {
        g[y] = z;
      }
    }
  }
  for (int i = 1; i <= n; i++) {
    if (f(i) != f(1)) {
      printf("NO\n");
      return 0;
    }
  }
  printf("YES\n");
  return 0;
}
