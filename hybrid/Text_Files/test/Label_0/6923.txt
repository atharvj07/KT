#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int n, i;
  cin >> n;
  long long int dp[n + 1][2], m = 1000000007;
  dp[0][0] = 0;
  dp[0][1] = 0;
  for (i = 1; i <= n; i++) {
    dp[i][i % 2] = (dp[i - 1][1 - (i % 2)] + 1 + dp[i - 1][(i % 2)]) % m;
    dp[i][1 - (i % 2)] = dp[i - 1][1 - (i % 2)];
  }
  cout << (dp[n][0] + dp[n][1]) % m;
}
