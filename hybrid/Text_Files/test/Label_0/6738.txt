#include <bits/stdc++.h>
using namespace std;
inline int read() {
  int ans = 0, fh = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') fh = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9')
    ans = (ans << 1) + (ans << 3) + ch - '0', ch = getchar();
  return ans * fh;
}
const int maxn = 1000;
struct node {
  int x, y;
} p[maxn];
int n, m, a[maxn], b[maxn];
int main() {
  n = read(), m = read();
  memset(b, 0x3f, sizeof(b));
  for (int i = 1; i <= m; i++) {
    int x = read(), y = read();
    a[x]++;
    if (y > x)
      b[x] = min(b[x], y - x);
    else
      b[x] = min(b[x], y + n - x);
  }
  for (int i = 1; i <= n; i++)
    if (!a[i]) b[i] = 0;
  for (int i = 1; i <= n; i++) {
    int ans = 0;
    for (int j = 1; j <= n; j++) {
      int tmp;
      if (j >= i)
        tmp = j - i;
      else
        tmp = j + n - i;
      tmp += (a[j] - 1) * n + b[j];
      ans = max(ans, tmp);
    }
    printf("%d\n", ans);
  }
  return 0;
}
