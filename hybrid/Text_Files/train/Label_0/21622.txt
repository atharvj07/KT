#include <bits/stdc++.h>
using namespace std;
bool check(long long x, long long y, long long p, long long q, long long t) {
  return p * t >= x && q * t - p * t >= y - x;
}
void solve() {
  long long x, y, p, q;
  scanf("%lld%lld%lld%lld", &x, &y, &p, &q);
  long long l = -1;
  long long r = (long long)1e9;
  if (!check(x, y, p, q, r)) {
    printf("-1\n");
    return;
  }
  while (r - l > 1) {
    long long m = (l + r) / 2;
    if (check(x, y, p, q, m)) {
      r = m;
    } else {
      l = m;
    }
  }
  printf("%lld\n", r * q - y);
}
int main() {
  int t;
  scanf("%d", &t);
  while (t--) {
    solve();
  }
  return 0;
}
