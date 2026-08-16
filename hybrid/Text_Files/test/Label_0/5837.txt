#include <bits/stdc++.h>
#pragma GCC optimize(2)
using namespace std;
int n, m, k, dp[300], trans[300], id[10];
vector<pair<pair<int, int>, int> > v;
signed main() {
  ios::sync_with_stdio(false);
  cin >> n >> m >> k;
  for (int i = 1; i <= n; i++) {
    int l, r;
    cin >> l >> r;
    v.push_back(make_pair(make_pair(l, 1), i));
    v.push_back(make_pair(make_pair(r + 1, 0), i));
  }
  sort(v.begin(), v.end());
  for (int i = 1; i < (1 << k); i++) dp[i] = -1000000007;
  for (int i = 1; i <= k; i++) id[i] = -1;
  for (int i = 0; i < v.size(); i++) {
    if (v[i].first.second == 1) {
      int pos = 0;
      for (int j = 1; j <= k; j++) {
        if (id[j] == -1) {
          pos = j;
          break;
        }
      }
      id[pos] = v[i].second;
      for (int j = 0; j < (1 << k); j++) trans[j] = -1000000007;
      for (int j = 0; j < (1 << k); j++) {
        trans[j] = max(trans[j], dp[j]);
        trans[j ^ (1 << (pos - 1))] = max(trans[j ^ (1 << (pos - 1))], dp[j]);
      }
      memcpy(dp, trans, sizeof(trans));
    } else if (v[i].first.second == 0) {
      int pos = 0;
      for (int j = 1; j <= k; j++) {
        if (id[j] == v[i].second) {
          pos = j;
          break;
        }
      }
      id[pos] = -1;
      for (int j = 0; j < (1 << k); j++) trans[j] = -1000000007;
      for (int j = 0; j < (1 << k); j++) {
        if (j & (1 << (pos - 1)))
          trans[j ^ (1 << (pos - 1))] = max(trans[j ^ (1 << (pos - 1))], dp[j]);
        else
          trans[j] = max(trans[j], dp[j]);
      }
      memcpy(dp, trans, sizeof(trans));
    }
    if (i == v.size() - 1) continue;
    for (int j = 0; j < (1 << k); j++) {
      if (__builtin_popcount(j) & 1)
        dp[j] += v[i + 1].first.first - v[i].first.first;
    }
  }
  int maxv = -1000000007;
  for (int i = 0; i < (1 << k); i++) maxv = max(maxv, dp[i]);
  cout << maxv << endl;
  return 0;
}
