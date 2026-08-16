#include <bits/stdc++.h>
using namespace std;
const int max_n = 100111;
const long long inf = 1000111222000111222LL;
int n, x1, yl, x2, y2, x, y, dx[max_n], dy[max_n];
char s[max_n];
bool ok(long long cnt) {
  long long full = cnt / n;
  long long last = cnt % n;
  long long xx = full * dx[n - 1];
  long long yy = full * dy[n - 1];
  if (last) {
    --last;
    xx += dx[last];
    yy += dy[last];
  }
  long long d = (long long)abs(xx - x) + (long long)abs(yy - y);
  return cnt >= d;
}
int main() {
  scanf("%d %d %d %d %d %s", &x1, &yl, &x2, &y2, &n, s);
  for (int i = 0; i < n; i++) {
    if (s[i] == 'U') {
      dy[i] = 1;
    } else if (s[i] == 'D') {
      dy[i] = -1;
    } else if (s[i] == 'L') {
      dx[i] = -1;
    } else {
      dx[i] = 1;
    }
    if (i) {
      dx[i] += dx[i - 1];
      dy[i] += dy[i - 1];
    }
  }
  x = x2 - x1;
  y = y2 - yl;
  long long l = 0, r = inf;
  while (r - l > 1) {
    long long mid = (l + r) / 2;
    if (ok(mid)) {
      r = mid;
    } else {
      l = mid;
    }
  }
  if (r == inf) {
    puts("-1");
    return 0;
  }
  printf("%I64d\n", r);
  return 0;
}
