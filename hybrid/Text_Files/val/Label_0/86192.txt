#include <bits/stdc++.h>
using namespace std;
constexpr long long MOD = 1e9 + 7;
const long long INF = 1e10;
int n;
int b[1010], a[10];
long long dp[1010][1 << 12];
int clear(int s, int row, int k) {
  for (int i = 0; i < k; ++i) {
    for (int j = row; j < row + k; ++j) {
      s &= ~(1 << (4 * i + j));
    }
  }
  return s;
}
void solve() {
  for (int s = 0; s < (1 << 12); ++s) dp[0][s] = INF;
  dp[0][0] = 0;
  for (int k = 1; k <= 3; ++k) {
    for (int s = 0; s < (1 << (4 * k)); ++s) {
      int S = s << (4 * (3 - k));
      for (int row = 0; row < 4; ++row) {
        for (int sz = 1; sz <= k; ++sz) {
          if (row + sz - 1 >= 4) break;
          dp[0][S] =
              min(dp[0][S], dp[0][clear(s, row, sz) << (4 * (3 - k))] + a[sz]);
        }
      }
    }
  }
  for (int i = 1; i <= n - 3; ++i) {
    for (int s = 0; s < (1 << 12); ++s) {
      dp[i][s] = dp[i - 1][0] + a[4];
      if (!(s & ((1 << 4) - 1))) {
        dp[i][s] = min(dp[i][s], dp[i - 1][(s >> 4) | (b[i] << 8)]);
      }
      for (int row = 0; row < 4; ++row) {
        for (int k = 1; k <= 3; ++k) {
          if (row + k - 1 >= 4) break;
          dp[i][s] = min(dp[i][s], dp[i][clear(s, row, k)] + a[k]);
        }
      }
    }
  }
  cout << dp[n - 3][(b[n - 2] << 8) | (b[n - 1] << 4) | b[n]] << endl;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin >> n;
  for (int i = 1; i <= 4; ++i) cin >> a[i];
  string s[4];
  for (int i = 0; i < 4; ++i) cin >> s[i];
  for (int j = 0; j < n; ++j) {
    for (int i = 0; i < 4; ++i) {
      if (s[i][j] == '*') {
        b[j + 1] ^= (1 << i);
      }
    }
  }
  solve();
  return 0;
}
