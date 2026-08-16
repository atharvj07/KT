#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const int inf = 1e9 + 5;
void solve(int tc) {
  string s;
  int n;
  cin >> s >> n;
  s = s;
  int dp[(int)s.size() + 5][n + 5][2];
  for (int i = 0; i < (int)s.size() + 5; ++i)
    for (int j = 0; j < n + 5; ++j) dp[i][j][0] = dp[i][j][1] = -inf;
  dp[0][0][1] = 0;
  for (int i = 0; i < (int)s.size(); ++i) {
    for (int j = 0; j <= n; ++j) {
      if (dp[i][j][0] > -inf) {
        if (s[i] == 'F') {
          dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][0] - 1);
          dp[i + 1][j + 1][1] = max(dp[i + 1][j + 1][1], dp[i][j][0]);
        } else {
          dp[i + 1][j][1] = max(dp[i + 1][j][1], dp[i][j][0]);
          dp[i + 1][j + 1][0] = max(dp[i + 1][j + 1][0], dp[i][j][0] - 1);
        }
        for (int k = j + 2; k <= n; k += 2)
          dp[i][k][0] = max(dp[i][k][0], dp[i][j][0]);
      }
      if (dp[i][j][1] > -inf) {
        if (s[i] == 'F') {
          dp[i + 1][j][1] = max(dp[i + 1][j][1], dp[i][j][1] + 1);
          dp[i + 1][j + 1][0] = max(dp[i + 1][j + 1][0], dp[i][j][1]);
        } else {
          dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][1]);
          dp[i + 1][j + 1][1] = max(dp[i + 1][j + 1][1], dp[i][j][1] + 1);
        }
        for (int k = j + 2; k <= n; k += 2)
          dp[i][k][1] = max(dp[i][k][1], dp[i][j][1]);
      }
    }
  }
  int ans = max({0, dp[(int)s.size()][n][0], dp[(int)s.size()][n][1]});
  for (int i = 0; i < (int)s.size() + 5; ++i)
    for (int j = 0; j < n + 5; ++j) dp[i][j][0] = dp[i][j][1] = inf;
  dp[0][0][1] = 0;
  for (int i = 0; i < (int)s.size(); ++i) {
    for (int j = 0; j <= n; ++j) {
      if (dp[i][j][0] > -inf) {
        if (s[i] == 'F') {
          dp[i + 1][j][0] = min(dp[i + 1][j][0], dp[i][j][0] - 1);
          dp[i + 1][j + 1][1] = min(dp[i + 1][j + 1][1], dp[i][j][0]);
        } else {
          dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][0]);
          dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][0] - 1);
        }
        for (int k = j + 2; k <= n; k += 2)
          dp[i][k][0] = min(dp[i][k][0], dp[i][j][0]);
      }
      if (dp[i][j][1] > -inf) {
        if (s[i] == 'F') {
          dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][1] + 1);
          dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][1]);
        } else {
          dp[i + 1][j][0] = min(dp[i + 1][j][0], dp[i][j][1]);
          dp[i + 1][j + 1][1] = min(dp[i + 1][j + 1][1], dp[i][j][1] + 1);
        }
        for (int k = j + 2; k <= n; k += 2)
          dp[i][k][1] = min(dp[i][k][1], dp[i][j][1]);
      }
    }
  }
  ans = max({ans, -dp[(int)s.size()][n][0], -dp[(int)s.size()][n][1]});
  cout << ans;
}
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int tc = 1;
  for (int i = 1; i <= tc; ++i) solve(i);
  return 0;
}
