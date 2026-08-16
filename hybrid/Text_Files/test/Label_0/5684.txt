#include <bits/stdc++.h>
#define MOD (long long)(1e9 + 7)
using namespace std;

long long ssize = 0;
long long dp[200005][2] = {0}, sum[200005][2] = {0};
string s, t;

long long solve();

int main() {
  cin >> s >> t;
  cout << solve() << endl;
  return 0;
}

long long solve() {
  ssize = s.size();
  dp[0][0] = 1;
  for(int i = 0; i < ssize; ++i) {
    int nums = s[i] - '0', numt = t[i] - '0';
    if(t[i] != '?') {
      if(nums == numt) {
        (dp[i + 1][1] += dp[i][1]) %= MOD;
        (dp[i + 1][0] += dp[i][0]) %= MOD;

        sum[i + 1][1] +=
            (sum[i][1] * 10 % MOD + dp[i][1] * numt % MOD) %
            MOD;
        sum[i + 1][1] %= MOD;
        sum[i + 1][0] +=
            (sum[i][0] * 10 % MOD + dp[i][0] * numt % MOD) %
            MOD;
        sum[i + 1][0] %= MOD;
      }
      else if(nums < numt) {
        dp[i + 1][1] += dp[i][1];
        dp[i + 1][1] %= MOD;

        sum[i + 1][1] +=
            (sum[i][1] * 10 % MOD + dp[i][1] * numt % MOD) %
            MOD;
        sum[i + 1][1] %= MOD;
      }
      else {
        dp[i + 1][1] += dp[i][1];
        (dp[i + 1][1] += dp[i][0]) %= MOD;

        sum[i + 1][1] +=
            (sum[i][1] * 10 % MOD + dp[i][1] * numt % MOD) %
            MOD;
        sum[i + 1][1] %= MOD;
        sum[i + 1][1] +=
            (sum[i][0] * 10 % MOD + dp[i][0] * numt % MOD) %
            MOD;
        sum[i + 1][1] %= MOD;
      }
    }
    else {
      for(int k = 0; k < 10; ++k) {
        numt = k;
        if(nums == numt) {
          (dp[i + 1][1] += dp[i][1]) %= MOD;
          (dp[i + 1][0] += dp[i][0]) %= MOD;

          sum[i + 1][1] += (sum[i][1] * 10 % MOD +
                            dp[i][1] * numt % MOD) %
                           MOD;
          sum[i + 1][1] %= MOD;
          sum[i + 1][0] += (sum[i][0] * 10 % MOD +
                            dp[i][0] * numt % MOD) %
                           MOD;
          sum[i + 1][0] %= MOD;
        }
        else if(nums < numt) {
          dp[i + 1][1] += dp[i][1];
          dp[i + 1][1] %= MOD;

          sum[i + 1][1] += (sum[i][1] * 10 % MOD +
                            dp[i][1] * numt % MOD) %
                           MOD;
          sum[i + 1][1] %= MOD;
        }
        else {
          dp[i + 1][1] += dp[i][1];
          (dp[i + 1][1] += dp[i][0]) %= MOD;

          sum[i + 1][1] += (sum[i][1] * 10 % MOD +
                            dp[i][1] * numt % MOD) %
                           MOD;
          sum[i + 1][1] %= MOD;
          sum[i + 1][1] += (sum[i][0] * 10 % MOD +
                            dp[i][0] * numt % MOD) %
                           MOD;
          sum[i + 1][1] %= MOD;
        }
      }
    }
  }

  return (sum[ssize][1] + sum[ssize][0]) % MOD;
}
