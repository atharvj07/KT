#include <bits/stdc++.h>
using namespace std;
long long n;
bool cau(long long k) {
  if (k * (k - 1) / 2 > n - k)
    return true;
  else
    return false;
}
long long ternsearch(long long l, long long r) {
  long long mid = (l + r) >> 1;
  long long sum = 0;
  if (cau(mid))
    sum = 2 * n - 2 * mid;
  else
    sum = n - mid + mid * (mid - 1) / 2;
  while (l <= r) {
    mid = (l + r) >> 1;
    long long midl = (l + mid) >> 1;
    long long midr = (r + mid) >> 1;
    long long now = 0, sum1 = 0, sum2 = 0;
    if (cau(mid))
      now = 2 * n - 2 * mid;
    else
      now = n - mid + mid * (mid - 1) / 2;
    sum = max(sum, now);
    if (cau(midl))
      sum1 = 2 * n - 2 * midl;
    else
      sum1 = n - midl + midl * (midl - 1) / 2;
    sum = max(sum1, sum);
    if (cau(midr))
      now = 2 * n - 2 * midr;
    else
      now = n - midr + midr * (midr - 1) / 2;
    sum = max(sum2, sum);
    if (cau(midl) && cau(midr))
      r = mid - 1;
    else if (!cau(midl) && !cau(midr))
      l = mid + 1;
    else {
      if (sum1 < sum2)
        r = midr - 1;
      else
        l = midl + 1;
    }
  }
  return sum;
}
int main() {
  int q;
  scanf("%d", &q);
  while (q--) {
    scanf("%lld", &n);
    printf("%lld\n", ternsearch(1, n));
  }
  return 0;
}
