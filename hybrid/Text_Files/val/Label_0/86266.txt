#include <bits/stdc++.h>
using namespace std;
long long arr[100005];
vector<long long> G[100005];
long long deg[100005];
long long cnt[100005];
vector<long long> gtrs[100005];
inline long long cal(long long u) {
  return deg[u] > 320
             ? (deg[u] - (long long)gtrs[u].size()) * (long long)gtrs[u].size()
             : (deg[u] - cnt[u]) * cnt[u];
}
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  long long n, m;
  cin >> n >> m;
  for (long long i = 1, u, v; i <= m; i++) {
    cin >> u >> v;
    G[u].emplace_back(v);
    G[v].emplace_back(u);
  }
  iota(arr + 1, arr + 1 + n, 1);
  long long ans = 0;
  for (long long u = 1; u <= n; u++) {
    deg[u] = (long long)G[u].size();
    if (deg[u] > 320) {
      for (long long v : G[u])
        if (arr[v] > arr[u]) gtrs[u].emplace_back(v);
    } else {
      for (long long v : G[u])
        if (arr[v] > arr[u]) cnt[u]++;
    }
    ans += cal(u);
  }
  cout << ans << '\n';
  long long q;
  cin >> q;
  for (long long t = 1; t <= q; t++) {
    long long u;
    cin >> u;
    ans -= cal(u);
    vector<long long>& tem = (deg[u] > 320 ? gtrs[u] : G[u]);
    for (long long v : tem)
      if (arr[u] < arr[v]) {
        ans -= cal(v);
        if (deg[v] > 320)
          gtrs[v].emplace_back(u);
        else
          cnt[v]++;
        ans += cal(v);
      }
    if (deg[u] > 320)
      gtrs[u].clear();
    else
      cnt[u] = 0;
    arr[u] = n + t;
    cout << ans << '\n';
  }
  return 0;
}
