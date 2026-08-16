#include <bits/stdc++.h>
using namespace std;
long long dp[2][2];
int main() {
  int n;
  cin >> n;
  int cur = 0;
  dp[0][0] = 1;
  dp[0][1] = 0;
  for (int i = 0; i <= n; ++i) {
    dp[cur ^ 1][0] = (3ll * (dp[cur][1]) % 1000000007) % 1000000007;
    dp[cur ^ 1][1] = ((2ll * (dp[cur][1]) % 1000000007) % 1000000007 +
                      1ll * dp[cur][0] % 1000000007) %
                     1000000007;
    cur ^= 1;
  }
  cout << dp[cur ^ 1][0];
}
