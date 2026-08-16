#include <bits/stdc++.h>
using namespace std;
long long n, k, m, d;
int main() {
  scanf("%lld%lld%lld%lld", &n, &k, &m, &d);
  long long ans = 0;
  ans = min(m, n);
  for (int i = 1; i <= d; ++i) {
    long long x = min(m, n / k);
    x = min(x, n / ((i - 1) * k + 1));
    if (!x) break;
    ans = max(ans, x * i);
  }
  printf("%lld\n", ans);
}
