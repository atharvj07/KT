#include <bits/stdc++.h>
using namespace std;
inline void read(int &x) {
  int f = 1;
  x = 0;
  char c = getchar();
  while (c < '0' || c > '9') {
    if (c == '-') f = -1;
    c = getchar();
  }
  while (c >= '0' && c <= '9') {
    x = x * 10 + c - '0';
    c = getchar();
  }
  x *= f;
}
signed main() {
  register int T, x, i, j, n, m;
  read(T);
  while (T--) {
    read(n);
    read(m);
    for (i = 1; i <= n; i++, putchar('\n'))
      for (j = 1; j <= m; j++)
        read(x), printf("%d ", x % 2 == (i + j) % 2 ? x : x + 1);
  }
  return 0;
}
