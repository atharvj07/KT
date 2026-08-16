#include <bits/stdc++.h>
using namespace std;
long long dp[5007];
long long dp2[5007][5007];
long long a, b, c;
long long chooseSum(long long c1, long long c2) {
  long long ans = 0;
  for (int i = 0; i <= min(c1, c2); i++) {
    long long aux = dp[i];
    aux = (aux * dp2[c1][i]) % 998244353;
    aux = (aux * dp2[c2][i]) % 998244353;
    ans = (ans + aux) % 998244353;
  }
  return ans;
}
int main() {
  cin >> a >> b >> c;
  for (int i = 0; i < 5007; i++) {
    dp[i] = 0;
    for (int j = 0; j < 5007; j++) {
      dp2[i][j] = 0;
    }
  }
  dp2[0][0] = 1;
  for (int i = 1; i <= 5000; i++) {
    dp2[i][0] = 1;
    for (int j = 1; j <= i; j++)
      dp2[i][j] = (dp2[i - 1][j - 1] + dp2[i - 1][j]) % 998244353;
  }
  dp[0] = 1;
  for (int i = 1; i <= 5000; i++) dp[i] = (dp[i - 1] * i) % 998244353;
  long long ans = 1;
  ans = (ans * chooseSum(a, b)) % 998244353;
  ans = (ans * chooseSum(b, c)) % 998244353;
  ans = (ans * chooseSum(a, c)) % 998244353;
  cout << ans;
  return 0;
}
