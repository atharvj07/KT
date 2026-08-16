#include <bits/stdc++.h>
using namespace std;
int dp[1000010];
int main(void) {
  int N, i, j, x;
  cin >> N;
  for ((i) = 0; (i) < (int)(N); (i)++) {
    scanf("%d", &x);
    dp[x] = 1;
  }
  int M = 1000000;
  for (i = 1; i <= M; i++)
    if (dp[i] != 0)
      for (j = 2 * i; j <= M; j += i)
        if (dp[j] != 0) dp[j] = max(dp[j], dp[i] + 1);
  int ans = 0;
  for (i = 1; i <= M; i++) ans = max(ans, dp[i]);
  cout << ans << endl;
  return 0;
}
