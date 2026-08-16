#include <bits/stdc++.h>
using namespace std;
set<pair<long long, long long>> dp;
long long a[200200];
void add(long long u, long long y) {
  auto it = dp.lower_bound(make_pair(u, -1));
  if (it == dp.end() || it->first != u) {
    dp.insert({u, y});
    return;
  }
  long long x = it->second;
  if (x >= y) return;
  dp.erase(it);
  dp.insert({u, y});
}
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) scanf("%lld", a + i);
  dp.insert({a[0] - 1, 0});
  for (int i = 1; i < n; i++) {
    long long t = -1, x, y, u;
    while (dp.rbegin()->first >= a[i]) {
      x = dp.rbegin()->first;
      y = dp.rbegin()->second;
      u = x % a[i];
      add(u, y + x / a[i] * a[i] * i);
      t = max(t, y + (x / a[i] - 1) * a[i] * i);
      dp.erase(*dp.rbegin());
    }
    if (t >= 0) add(a[i] - 1, t);
  }
  long long ans = -1;
  for (auto a : dp) ans = max(ans, a.first * n + a.second);
  cout << ans << endl;
  return 0;
}
