#include <bits/stdc++.h>
using namespace std;
int n, s, e, dp[5100], x[5100], a[5100], b[5100], c[5100], d[5100];
inline long long calc(int i, int j) {
  if (i < j) return (long long)abs(x[i] - x[j]) + d[i] + a[j];
  if (i > j) return (long long)abs(x[i] - x[j]) + c[i] + b[j];
  return 0;
}
void init() {
  cin >> n >> s >> e;
  for (int i = 1; i <= n; ++i) cin >> x[i];
  for (int i = 1; i <= n; ++i) cin >> a[i];
  for (int i = 1; i <= n; ++i) cin >> b[i];
  for (int i = 1; i <= n; ++i) cin >> c[i];
  for (int i = 1; i <= n; ++i) cin >> d[i];
  dp[e] = 0;
  dp[s] = e;
}
void solve() {
  int id, t;
  long long ans, min, td;
  ans = calc(s, e);
  for (int i = 1; i <= n; ++i) {
    if (i == s || i == e) continue;
    min = id = -1, t = s;
    while (dp[t]) {
      td = calc(t, i) + calc(i, dp[t]) - calc(t, dp[t]);
      if (min == -1 || min > td) {
        min = td;
        id = t;
      }
      t = dp[t];
    }
    dp[i] = dp[id];
    dp[id] = i;
    ans += min;
  }
  cout << ans << endl;
}
int main() {
  init();
  solve();
  return 0;
}
