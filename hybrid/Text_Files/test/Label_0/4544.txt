#include <bits/stdc++.h>
using namespace std;
long long up(long long a, long long b) { return (a + b - 1) / b; }
long long down(long long a, long long b) { return a / b; }
long long a[400010];
pair<long long, long long> b[400010];
long long mx[400010];
void solve() {
  long long n, k;
  int m;
  scanf("%I64d %d %I64d", &n, &m, &k);
  long long pre = 0;
  for (int i = 1; i <= m; i++) {
    long long x;
    scanf("%I64d", &x);
    a[i] = x - pre;
    pre = x;
  }
  a[++m] = n - pre;
  long long l, r;
  long long L, U;
  l = 1;
  r = n + 1;
  while (l + 1 < r) {
    long long mid = (l + r) >> 1;
    long long cnt = 0;
    for (int i = 1; i <= m; i++) cnt += down(a[i], mid);
    if (m + k <= cnt)
      l = mid;
    else
      r = mid;
  }
  L = l;
  l = 0;
  r = n + 1;
  while (l + 1 < r) {
    long long mid = (l + r) >> 1;
    long long cnt = 0;
    for (int i = 1; i <= m; i++) cnt += up(a[i], mid);
    if (m + k >= cnt)
      r = mid;
    else
      l = mid;
  }
  U = r;
  int num = 0;
  for (int i = 1; i <= m; i++) {
    if (up(a[i], U) <= down(a[i], L)) continue;
    l = 0;
    r = L;
    while (l + 1 < r) {
      long long mid = (l + r) >> 1;
      if (down(a[i], mid) == down(a[i], L))
        r = mid;
      else
        l = mid;
    }
    long long x = L - l;
    l = U;
    r = 1e18;
    while (l + 1 < r) {
      long long mid = (l + r) >> 1;
      if (up(a[i], mid) == up(a[i], U))
        l = mid;
      else
        r = mid;
    }
    long long y = r - U;
    b[++num] = make_pair(x, y);
  }
  sort(b + 1, b + num + 1);
  mx[num + 1] = 0;
  for (int i = num; i >= 1; i--) mx[i] = max(mx[i + 1], b[i].second);
  long long ans = mx[1];
  for (int i = 1; i <= num; i++) ans = min(ans, b[i].first + mx[i + 1]);
  printf("%I64d\n", ans + U - L);
  return;
}
int main() {
  int t;
  scanf("%d", &t);
  while (t--) solve();
  return 0;
}
