#include <bits/stdc++.h>
using namespace std;
long long int xo(long long int x, long long int y) {
  return (x | y) & (~x | ~y);
}
long long int bin_Expo(long long int x, long long int n) {
  if (x == 0) return 0;
  if (n == 0)
    return 1;
  else if (n % 2 == 0)
    return bin_Expo(x * x, n / 2);
  else
    return x * bin_Expo(x * x, (n - 1) / 2);
}
long long int mod_Expo(long long int x, long long int n, long long int M) {
  if (x == 0) return 0;
  if (n == 0)
    return 1;
  else if (n % 2 == 0)
    return mod_Expo((x * x) % M, n / 2, M);
  else
    return (x * mod_Expo((x * x) % M, (n - 1) / 2, M)) % M;
}
bool prime_check(long long int x) {
  bool prime = (x >= 2);
  for (long long int i = 2; i * i <= x; i++) {
    if (x % i == 0) {
      prime = false;
      break;
    }
  }
  return prime;
}
long long int logg(long long int base, long long int x) {
  return (long long int)(log(x) / log(base));
}
long long int a[501], dp[501][501], dp1[501];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int TESTS = 1;
  while (TESTS--) {
    long long int n, m, k, l, h, g, i, j;
    cin >> n;
    for (long long int i = 0; i < n; i++) cin >> a[i];
    for (long long int i = 0; i <= n; i++) {
      for (long long int j = 0; j <= n; j++) dp[i][j] = -1;
      dp1[i] = 1000000007;
    }
    for (l = 1; l <= n; l++) {
      for (i = 0; i < n - l + 1; i++) {
        j = i + l - 1;
        if (i == j)
          dp[i][j] = a[i];
        else {
          for (k = i; k < j; k++) {
            if (dp[i][k] != -1 && dp[i][k] == dp[k + 1][j])
              dp[i][j] = dp[i][k] + 1;
          }
        }
      }
    }
    for (long long int i = 0; i < n; i++) {
      for (long long int k = 0; k <= i; k++) {
        if (dp[k][i] != -1) {
          if (k == 0)
            dp1[i] = 1;
          else
            dp1[i] = min(dp1[i], dp1[k - 1] + 1);
        }
      }
    }
    cout << dp1[n - 1];
  }
  return 0;
}
