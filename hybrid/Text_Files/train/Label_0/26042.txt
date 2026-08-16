#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
const int MOD = 1e9 + 7;
char s[N];
int dp[N];
int main() {
  scanf("%s", s + 1);
  memset(dp, 0, sizeof(dp));
  int len = strlen(s + 1);
  dp[0] = 1;
  dp[1] = 1;
  for (int i = 2; i <= len; i++) {
    if (s[i] == 'n' || s[i] == 'u') {
      if (s[i] == s[i - 1]) {
        dp[i] = (dp[i - 2] + dp[i - 1]) % MOD;
        continue;
      }
    } else if (s[i] == 'm' || s[i] == 'w') {
      dp[len] = 0;
      break;
    }
    dp[i] = dp[i - 1];
  }
  if (s[1] == 'm' || s[1] == 'w') dp[len] = 0;
  printf("%d\n", dp[len]);
}
