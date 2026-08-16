#include <bits/stdc++.h>
using namespace std;
long long n, a[200010], cnt, id, k[200010];
double ans = -1, pre[200010];
double f(long long x, long long mid) {
  return ((pre[n] - pre[n - x]) + (pre[mid] - pre[mid - x - 1])) / (x * 2 + 1);
}
signed main() {
  scanf("%lld", &n);
  for (long long i = 1; i <= n; i++) {
    scanf("%lld", &a[i]);
  }
  sort(a + 1, a + 1 + n);
  for (long long i = 1; i <= n; i++) {
    pre[i] = pre[i - 1] + a[i];
  }
  for (long long i = 1; i <= n; i++) {
    long long l = 1, r = min(i - 1, n - i);
    long long num = 0;
    while (l <= r) {
      long long mid = (l + r) / 2;
      if (f(mid, i) >= f(mid - 1, i))
        l = mid + 1, num = mid;
      else
        r = mid - 1;
    }
    if (f(num, i) - (pre[i] - pre[i - 1]) > ans) {
      ans = f(num, i) - (pre[i] - pre[i - 1]);
      cnt = num, id = i;
    }
  }
  printf("%lld\n", 2 * cnt + 1);
  for (long long i = id - cnt; i <= id; i++) printf("%lld ", a[i]);
  for (long long i = n - cnt + 1; i <= n; i++) printf("%lld ", a[i]);
  return 0;
}
