#include <bits/stdc++.h>
void init();
void solve();
int main() {
  init();
  while (scanf("%*[ \t\n]*") != EOF) {
    solve();
  }
  return 0;
}
const int MOD = 998244353;
const int MaxN = 5001;
int a[MaxN], n;
long long dp[2][MaxN];
void init() {}
void solve() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  std::sort(a, a + n);
  std::fill(dp[0], dp[0] + n, 1);
  int fd = 0, nd = 1;
  for (int i = 1; i < n; i++, fd ^= 1, nd ^= 1) {
    std::fill(dp[nd], dp[nd] + n, 0);
    long long sum = 0;
    for (int j = 0, k = 0; j < n; j++) {
      if (dp[fd][j] > 0) {
        while (k < n && a[k] * 2 <= a[j]) {
          sum = (sum + dp[fd][k]) % MOD;
          k++;
        }
        if (k > i - 1) {
          dp[nd][j] = (dp[nd][j] + dp[fd][j] * (k - i + 1)) % MOD;
        }
        dp[nd][j] = (dp[nd][j] + sum) % MOD;
      }
    }
  }
  printf("%lld\n", std::accumulate(dp[fd], dp[fd] + n, 0LL) % MOD);
}
