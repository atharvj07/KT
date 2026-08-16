#include <bits/stdc++.h>
using namespace std;
const long long INF = 1000000000000000;
const int maxn = 1e5 + 100;
long long dp[maxn][2], c[maxn];
string reverse(string s) {
  string t = "";
  for (int i = s.size() - 1; i >= 0; i--) t += s[i];
  return t;
}
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) cin >> c[i];
  string last;
  cin >> last;
  dp[0][0] = 0;
  dp[0][1] = c[0];
  for (int i = 1; i < n; i++) {
    string now;
    cin >> now;
    dp[i][0] = dp[i][1] = INF;
    if (last <= now) dp[i][0] = min(dp[i][0], dp[i - 1][0]);
    if (reverse(last) <= now) dp[i][0] = min(dp[i][0], dp[i - 1][1]);
    if (last <= reverse(now)) dp[i][1] = min(dp[i][1], dp[i - 1][0] + c[i]);
    if (reverse(last) <= reverse(now))
      dp[i][1] = min(dp[i][1], dp[i - 1][1] + c[i]);
    last = now;
  }
  long long ans = min(dp[n - 1][0], dp[n - 1][1]);
  if (ans >= INF)
    cout << -1 << endl;
  else
    cout << ans << endl;
  return 0;
}
