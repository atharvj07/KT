#include <bits/stdc++.h>
using namespace std;
const int N = 30, mod = int(1e9) + 7;
const double eps = 1e-9;
int k, n;
double p[N];
long double dp[1 << 21], a[N];
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 0; i < n; i++) {
    scanf("%lf", &p[i]);
  }
  dp[0] = 1;
  for (int mask = 0; mask < (1 << n); mask++) {
    long double sum = 0;
    for (int i = 0; i < n; i++) {
      if (mask & (1 << i)) {
        sum += p[i];
      }
    }
    if (__builtin_popcount(mask) == k || abs(sum - 1) < eps) {
      for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) {
          a[i] += dp[mask];
        }
      }
      continue;
    }
    for (int i = 0; i < n; i++) {
      if (!(mask & (1 << i))) {
        int nmask = mask | (1 << i);
        dp[nmask] += dp[mask] * p[i] / (1 - sum);
      }
    }
  }
  for (int i = 0; i < n; i++) {
    printf("%.12lf ", double(a[i]));
  }
  return 0;
}
