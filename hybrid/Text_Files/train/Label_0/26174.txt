#include <bits/stdc++.h>
const int kN = 1000000 + 5;
using LL = long long;
const LL inf = 1e18;
int k;
int f[6];
LL dp[kN];
int ten[6] = {1, 10, 100, 1000, 10000, 100000};
int main() {
  scanf("%d", &k);
  for (int i = 0; i < 6; ++i) {
    scanf("%d", &f[i]);
  }
  std::fill(dp, dp + kN, -inf);
  dp[0] = 0;
  for (int b = 0; b < 6; ++b) {
    int cnt = 3 * (k - 1);
    for (int c = 1; cnt > 0; cnt -= c, c = std::min(cnt, c << 1)) {
      LL w = c * 1LL * 3 * ten[b];
      for (LL i = kN - 1 - w; i >= 0; --i)
        if (dp[i] != -inf) {
          dp[i + w] = std::max(dp[i + w], dp[i] + f[b] * 1LL * c);
        }
    }
  }
  for (int b = 0; b < 6; ++b) {
    for (int i = kN - 1; i >= 0; --i)
      if (dp[i] != -inf) {
        for (int r = 1; r < 10; ++r) {
          LL w = r * ten[b];
          if (i + w < kN) {
            dp[i + w] =
                std::max(dp[i + w], dp[i] + (r % 3 == 0) * r / 3 * 1LL * f[b]);
          }
        }
      }
  }
  int q;
  scanf("%d", &q);
  while (q--) {
    int n;
    scanf("%d", &n);
    printf("%lld\n", dp[n]);
  }
}
