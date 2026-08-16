#include <bits/stdc++.h>
using namespace std;
long long dp[2005][2005] = {};
int main() {
  std::ios_base::sync_with_stdio(0), cin.tie(0);
  int n, m;
  cin >> n >> m;
  string s;
  long long mod = 1e9 + 7;
  cin >> s;
  int d = n - m;
  int bal = 0, mn = 0;
  for (int i = 0; i < m; ++i) {
    if (s[i] == '(')
      bal++;
    else
      bal--;
    mn = min(mn, bal);
  }
  dp[0][0] = 1;
  long long ans = 0;
  for (int i = 1; i <= d; ++i) {
    dp[i][0] = dp[i - 1][1];
    for (int j = 1; j <= d; ++j) {
      dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod;
    }
  }
  for (int i = 0; i <= d; ++i) {
    for (int j = -mn; j <= d && d - i >= bal + j; ++j) {
      ans += dp[i][j] * dp[d - i][j + bal];
      ans %= mod;
    }
  }
  cout << ans;
  return 0;
}
