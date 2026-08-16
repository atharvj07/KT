#include <bits/stdc++.h>
using namespace std;
int n, m;
string a[1007];
long long mask[1007];
long long dp[1007][1007];
long long hh[1007];
void input() {
  cin >> m >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    for (int j = 0; j < m; ++j) {
      if (a[i][j] == '1') {
        mask[j] += (1LL << i);
      }
    }
  }
}
void solve() {
  dp[0][0] = 1;
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j <= i; ++j) {
      dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % 1000000007;
      dp[i + 1][j] = (dp[i + 1][j] + (dp[i][j] * j) % 1000000007) % 1000000007;
    }
  }
  for (int i = 1; i <= m; ++i) {
    for (int j = 1; j <= i; ++j) {
      hh[i] = (hh[i] + dp[i][j]) % 1000000007;
    }
  }
  sort(mask, mask + m);
  long long ans = 1;
  int len = 1;
  for (int i = 1; i < m; ++i) {
    if (mask[i] == mask[i - 1]) {
      ++len;
    } else {
      ans = (ans * hh[len]) % 1000000007;
      len = 1;
    }
  }
  ans = (ans * hh[len]) % 1000000007;
  cout << ans << "\n";
}
int main() {
  ios_base ::sync_with_stdio(false);
  cin.tie(NULL);
  input();
  solve();
  return 0;
}
