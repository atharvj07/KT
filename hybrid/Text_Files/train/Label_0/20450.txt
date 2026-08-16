#include <bits/stdc++.h>
using namespace std;
long long k, a[1000000], n, maxx, ans;
int main() {
  scanf("%lld%lld", &n, &k);
  for (int i = 1; i <= n; i++) {
    scanf("%lld", &a[i]);
    k += a[i];
    maxx = max(maxx, a[i] - 1);
  }
  for (long long l = 1, r; l < maxx; l = r + 1) {
    r = 10000000000000000;
    long long sum = 0;
    for (int i = 1; i <= n; i++)
      if ((a[i] - 1) >= l) {
        sum += (a[i] - 1) / l;
        r = min(r, (a[i] - 1) / ((a[i] - 1) / l));
      }
    if (k / (n + sum) >= l) ans = max(ans, min(r, k / (n + sum)));
  }
  if (k / n > maxx) ans = max(ans, k / n);
  printf("%lld", ans);
}
