#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  int now = 0, nxt = 1;
  long long dp[2][10];
  memset(dp, -1, sizeof(dp));
  dp[0][0] = 0;
  while (n--) {
    int k;
    cin >> k;
    vector<long long> v[4];
    for (int i = 0; i < k; i++) {
      long long c, d;
      cin >> c >> d;
      v[c].push_back(d);
    }
    sort(v[1].begin(), v[1].end(), greater<long long>());
    sort(v[2].begin(), v[2].end(), greater<long long>());
    sort(v[3].begin(), v[3].end(), greater<long long>());
    memcpy(dp[nxt], dp[now], sizeof(dp[now]));
    for (int i = 0; i < 10; i++) {
      if (dp[now][i] == -1) continue;
      for (int j = 1; j <= 3; j++) {
        if ((int)v[j].size() != 0) {
          dp[nxt][(i + 1) % 10] =
              max(dp[nxt][(i + 1) % 10],
                  dp[now][i] + v[j][0] * (1 + ((i + 1) == 10)));
        }
      }
      if ((int)v[1].size() >= 3)
        dp[nxt][(i + 3) % 10] = max(
            dp[nxt][(i + 3) % 10],
            dp[now][i] + v[1][0] * (1 + ((i + 3) >= 10)) + v[1][1] + v[1][2]);
      if ((int)v[1].size() >= 2)
        dp[nxt][(i + 2) % 10] =
            max(dp[nxt][(i + 2) % 10],
                dp[now][i] + v[1][0] * (1 + ((i + 2) >= 10)) + v[1][1]);
      if ((int)v[2].size() != 0 && (int)v[1].size() != 0)
        dp[nxt][(i + 2) % 10] = max(
            dp[nxt][(i + 2) % 10], dp[now][i] + v[2][0] + v[1][0] +
                                       max(v[1][0], v[2][0]) * ((i + 2) >= 10));
    }
    swap(now, nxt);
  }
  long long ans = 0;
  for (int i = 0; i < 10; i++) ans = max(ans, dp[now][i]);
  cout << ans << '\n';
  return 0;
}
