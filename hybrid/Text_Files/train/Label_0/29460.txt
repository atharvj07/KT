#include <bits/stdc++.h>
using namespace std;
bool comp(const pair<long long, long long> &a,
          const pair<long long, long long> &b) {
  return a.second < b.second;
}
long long bs(pair<long long, long long> a[], long long l, long long r,
             long long &srch) {
  long long ans = -1, m;
  while (l <= r) {
    m = (l + r) / 2;
    if (a[m].second < srch)
      ans = m, l = m + 1;
    else
      r = m - 1;
  }
  return ans;
}
int32_t main() {
  ios_base ::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  long long n;
  cin >> n;
  pair<long long, long long> a[n + 1];
  a[0].first = a[0].second = 0;
  for (long long i = 1; i <= n; i++) cin >> a[i].first >> a[i].second;
  sort(a, a + n + 1, comp);
  long long dp[n + 1];
  dp[0] = 0;
  for (long long i = 1; i <= n; i++) {
    long long idx = bs(a, 0, i - 1, a[i].first);
    dp[i] = max(dp[i - 1], dp[idx] + 1);
  }
  cout << dp[n] << endl;
  return 0;
}
