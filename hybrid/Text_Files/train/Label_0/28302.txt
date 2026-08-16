#include <bits/stdc++.h>
using namespace std;
int n, m, q, p, a, b, c, d, f[100000];
int max(int x, int y) {
  if (x > y)
    return x;
  else
    return y;
}
int main() {
  scanf("%d%d%d%d", &n, &m, &q, &p);
  for (int i = q; i <= n; i++) f[i] = i / q * p;
  for (int i = 1; i <= m; i++) {
    scanf("%d%d%d%d", &a, &b, &c, &d);
    for (int j = 1; j <= (a / b); j++)
      for (int k = n; k >= c; k--) f[k] = max(f[k], f[k - c] + d);
  }
  printf("%d", f[n]);
}
