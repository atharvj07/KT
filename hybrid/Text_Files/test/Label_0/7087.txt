#include <bits/stdc++.h>
using namespace std;
const long long maxn = 1000010;
long long a[maxn], ans, n, k;
signed main() {
  long long n, k;
  scanf("%I64d%I64d", &n, &k);
  for (long long i = (1), _end_ = (n); i <= _end_; ++i) {
    a[i] = i;
    k -= i;
    ans += i;
  }
  if (k < 0) {
    puts("-1");
    return 0;
  }
  for (long long i = n; i >= 1; --i)
    if (k && i > n - i + 1) {
      long long x = min(k, i + i - 1 - n);
      swap(a[i], a[i - x]);
      k -= x;
      ans += x;
    }
  printf("%I64d\n", ans);
  for (long long i = (1), _end_ = (n); i <= _end_; ++i) printf("%I64d ", i);
  puts("");
  for (long long i = (1), _end_ = (n); i <= _end_; ++i) printf("%I64d ", a[i]);
  puts("");
  return 0;
}
