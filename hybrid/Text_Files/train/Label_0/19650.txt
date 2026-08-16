#include <bits/stdc++.h>
using namespace std;
int n;
int c[10];
long long C[105][105];
long long memo[10][105];
long long dp(int dig, int cnt) {
  if (dig == 10) return cnt == 0;
  long long &dev = memo[dig][cnt];
  if (dev == -1) {
    dev = 0LL;
    for (int k = max(0, c[dig]); k <= cnt; ++k)
      dev = (dev + dp(dig + 1, cnt - k) * C[cnt][k] + 1000000007LL) %
            1000000007LL;
  }
  return dev;
}
int main() {
  C[0][0] = 1;
  for (int i = 0; i < 105; i++) C[i][0] = C[i][i] = 1;
  for (int i = 0; i < 105; i++)
    for (int j = 1; j < i; j++)
      C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % 1000000007LL;
  while (cin >> n) {
    for (int i = 0; i < 10; ++i) cin >> c[i];
    long long ans = 0LL;
    for (int dig = 1; dig < 10; ++dig) {
      c[dig]--;
      for (int L = 0; L < n; ++L) {
        memset(memo, -1, sizeof(memo));
        ans = (ans + dp(0, L) + 1000000007LL) % 1000000007LL;
      }
      c[dig]++;
    }
    cout << ans << "\n";
  }
}
