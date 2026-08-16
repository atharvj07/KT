#include <bits/stdc++.h>
using namespace std;
vector<pair<int, int> > v[200000];
int dp[400000], d[400000];
int main() {
  ios_base::sync_with_stdio(0);
  int n, m, i, j, x, y, l, mx = -1;
  cin >> n >> m;
  for (i = 1; i <= m; i++) {
    cin >> x >> y >> l;
    v[l].push_back(make_pair(x, y));
  }
  for (i = 1; i <= 100001; i++) {
    for (j = 0; j < v[i].size(); j++) x = v[i][j].second, d[x] = 0;
    for (j = 0; j < v[i].size(); j++)
      x = v[i][j].second, d[x] = max(d[x], dp[v[i][j].first] + 1);
    for (j = 0; j < v[i].size(); j++)
      x = v[i][j].second, dp[x] = max(dp[x], d[x]);
  }
  for (i = 1; i <= n; i++) mx = max(mx, dp[i]);
  cout << mx;
}
