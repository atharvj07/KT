#include <bits/stdc++.h>
using namespace std;
const int maxn = 5e3 + 7;
const int maxa = 1e5 + 7;
int dp[maxn][maxn];
int num[maxn], n;
int get_ans() {
  memset(dp, 0, sizeof(dp));
  int max_mod[7], max_num[maxa];
  memset(max_mod, 0, sizeof(max_mod));
  memset(max_num, 0, sizeof(max_num));
  int ans = 0;
  for (int i = 0; i <= n; ++i) {
    for (int j = 0; j <= n; ++j) {
      if (i == j) continue;
      if (j < i) {
        dp[i][j] = dp[j][i];
        max_mod[num[j] % 7] = max(max_mod[num[j] % 7], dp[i][j]);
        if (j != 0) max_num[num[j]] = max(max_num[num[j]], dp[i][j]);
      } else {
        dp[i][j] = dp[i][0] + 1;
        dp[i][j] = max(max_mod[num[j] % 7] + 1, dp[i][j]);
        dp[i][j] = max(max_num[num[j] + 1] + 1, dp[i][j]);
        dp[i][j] = max(max_num[num[j] - 1] + 1, dp[i][j]);
        max_mod[num[j] % 7] = max(max_mod[num[j] % 7], dp[i][j]);
        max_num[num[j]] = max(max_num[num[j]], dp[i][j]);
      }
      if (i != 0 && j != 0) ans = max(ans, dp[i][j]);
    }
    memset(max_mod, 0, sizeof(max_mod));
    for (int j = 1; j <= n; ++j) {
      max_num[num[j]] = 0;
    }
  }
  return ans;
}
int main() {
  while (cin >> n) {
    for (int i = 1; i <= n; ++i) {
      scanf("%d", num + i);
    }
    int ans = get_ans();
    cout << ans << endl;
  }
  return 0;
}
