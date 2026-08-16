#include <bits/stdc++.h>
using namespace std;
struct node {
  long long mi, lzy;
} p[8020020];
long long n, x, y, hi[1005][1005], tot, chk[1002020], ans;
long long Q_y(long long i, long long j) { return x * j - y * i; }
void pushdn(long long i) {
  long long k = p[i].lzy;
  p[i << 1].mi = max(k, p[i << 1].mi);
  p[i << 1].lzy = max(k, p[i << 1].lzy);
  p[(i << 1) | 1].mi = max(k, p[(i << 1) | 1].mi);
  p[(i << 1) | 1].lzy = max(k, p[(i << 1) | 1].lzy);
  p[i].lzy = 0;
}
void in(long long x, long long y, long long k, long long l, long long r,
        long long i) {
  if (x <= l && r <= y) {
    p[i].mi = max(k, p[i].mi);
    p[i].lzy = max(p[i].lzy, k);
    return;
  }
  long long mid = (l + r) >> 1;
  if (p[i].lzy) pushdn(i);
  if (x <= mid) in(x, y, k, l, mid, i << 1);
  if (mid < y) in(x, y, k, mid + 1, r, (i << 1) | 1);
  p[i].mi = min(p[i << 1].mi, p[(i << 1) | 1].mi);
}
long long Q(long long x, long long y, long long l, long long r, long long i) {
  if (x <= l && r <= y) return p[i].mi;
  long long mid = (l + r) >> 1, s = 1000000009;
  if (p[i].lzy) pushdn(i);
  if (x <= mid) s = Q(x, y, l, mid, i << 1);
  if (mid < y) s = min(Q(x, y, mid + 1, r, (i << 1) | 1), s);
  return s;
}
int main() {
  scanf("%lld%lld%lld", &n, &x, &y);
  if (x >= 0) {
    if (y >= 0) {
      for (long long i = 1; i <= n; i++)
        for (long long j = 1; j <= n; j++) scanf("%lld", &hi[i][j]);
    } else {
      for (long long i = 1; i <= n; i++)
        for (long long j = n; j >= 1; j--) scanf("%lld", &hi[i][j]);
    }
  } else {
    if (y >= 0) {
      for (long long i = n; i >= 1; i--)
        for (long long j = 1; j <= n; j++) scanf("%lld", &hi[i][j]);
    } else {
      for (long long i = n; i >= 1; i--)
        for (long long j = n; j >= 1; j--) scanf("%lld", &hi[i][j]);
    }
  }
  x = abs(x);
  y = abs(y);
  for (long long i = 0; i <= n; i++)
    for (long long j = 0; j <= n; j++) chk[++tot] = Q_y(i, j);
  sort(chk + 1, chk + tot + 1);
  tot = unique(chk + 1, chk + tot + 1) - chk - 1;
  for (long long i = 1; i <= n; i++)
    for (long long j = 1; j <= n; j++) {
      long long l = lower_bound(chk + 1, chk + tot + 1, Q_y(i, j - 1)) - chk,
                r = lower_bound(chk + 1, chk + tot + 1, Q_y(i - 1, j)) - chk,
                ss = Q(2 * l, 2 * r - 1, 1, 2 * tot, 1);
      if (hi[i][j] > ss) {
        ans += hi[i][j] - ss;
        in(2 * l, 2 * r - 1, hi[i][j], 1, 2 * tot, 1);
      }
    }
  printf("%lld", ans);
  return 0;
}
