#include <bits/stdc++.h>
using namespace std;
long long power(long long a, long long b, long long m) {
  long long x = 1 % m;
  a %= m;
  while (b) {
    if ((1 & b)) x = x * a % m;
    a = a * a % m;
    b >>= 1;
  }
  return x;
}
int a[2005];
int n, k;
long long dp[2005];
long long solve(long long x) {
  for (int i = 1; i <= n + 1; i++) {
    dp[i] = i - 1;
    if (i != n + 1) {
      for (int j = i - 1; j > 0; j--) {
        if (abs(a[i] - a[j]) <= x * (i - j)) {
          dp[i] = min(dp[i], dp[j] + (i - j - 1));
        }
      }
    } else {
      for (int j = i - 1; j > 0; j--) {
        dp[i] = min(dp[i], dp[j] + (i - j - 1));
      }
    }
  }
  return dp[n + 1];
}
int main() {
  scanf("%d", &n);
  scanf("%d", &k);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  if (n == 1) {
    printf("0");
    return 0;
  }
  int mx = 0;
  for (int i = 2; i <= n; i++) {
    mx = max(mx, abs(a[i] - a[i - 1]));
  }
  long long l = 0, r = mx;
  while (l < r) {
    long long mid = (l + r) >> 1;
    if (solve(mid) <= k)
      r = mid;
    else
      l = mid + 1;
  }
  printf("%lld\n", l);
}
