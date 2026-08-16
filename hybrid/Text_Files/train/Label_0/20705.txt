#include <bits/stdc++.h>
using namespace std;
const int maxn = 1000007;
char s[maxn];
int n, cnt, a[maxn];
bool check(int p, bool need_touch) {
  int x = 0, maxv = 0;
  bool touched = 0;
  for (int i = 1, _c = cnt; i <= _c; i++) {
    maxv = max(maxv, x);
    x += a[i];
    if (x <= p) {
      x = p + 1;
      touched = 1;
    }
  }
  return (x > maxv) && (!need_touch || touched);
}
int main() {
  cnt = 0;
  gets(s + 1);
  n = strlen(s + 1);
  int x = 1;
  while (x <= n) {
    int y = x;
    while (y < n && s[y + 1] == s[x]) ++y;
    a[++cnt] = y - x + 1;
    if (s[x] == 'L') a[cnt] *= -1;
    x = y + 1;
  }
  if (a[cnt] < 0)
    for (int i = 1, _c = cnt; i <= _c; i++) a[i] *= -1;
  if (check(-n - 1, 0)) {
    puts("1");
    return 0;
  }
  int res = 0;
  int l = -n, r = -1, mid, pos = 0;
  while (l <= r) {
    mid = (l + r) / 2;
    if (check(mid, 1)) {
      pos = mid;
      r = mid - 1;
    } else
      l = mid + 1;
  }
  res -= pos;
  printf("%d\n", res);
  return 0;
}
