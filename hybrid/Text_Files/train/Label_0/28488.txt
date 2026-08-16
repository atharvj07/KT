#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using vvvi = vector<vvi>;
using vvvvi = vector<vvvi>;
using pii = pair<int, int>;
using E = pair<pair<int, int>, int>;
using vE = vector<E>;
int main() {
  ios_base::sync_with_stdio(false);
  int n, maxk;
  cin >> n >> maxk;
  int m;
  cin >> m;
  vE edges(m);
  for (int i = 0; i < m; ++i) {
    int ui, vi, ci;
    cin >> ui >> vi >> ci;
    edges[i] = {{ui - 1, vi - 1}, ci};
  }
  if (maxk == 1) {
    cout << "0\n";
    return 0;
  }
  const int INF = 1e6;
  vvvvi dp(maxk, vvvi(n, vvi(n, vi(n, INF))));
  for (int s = 0; s < n; ++s) {
    for (int t = s; t < n; ++t) {
      for (int x = s; x <= t; ++x) {
        dp[0][s][t][x] = 0;
      }
    }
  }
  for (int k = 0; k < maxk - 1; ++k) {
    for (const auto& e : edges) {
      for (int s = 0; s < n; ++s) {
        for (int t = s; t < n; ++t) {
          int ue = e.first.first;
          int ve = e.first.second;
          int ce = e.second;
          if (ve < s || ve > t || ue < s || ue > t) continue;
          if (ve > ue) {
            dp[k + 1][ue + 1][t][ve] =
                min(dp[k + 1][ue + 1][t][ve], dp[k][s][t][ue] + ce);
          } else {
            dp[k + 1][s][ue - 1][ve] =
                min(dp[k + 1][s][ue - 1][ve], dp[k][s][t][ue] + ce);
          }
        }
      }
    }
  }
  int mincost = INF;
  for (int s = 0; s < n; ++s) {
    for (int t = s; t < n; ++t) {
      for (int x = s; x <= t; ++x) {
        mincost = min(mincost, dp[maxk - 1][s][t][x]);
      }
    }
  }
  if (mincost == INF)
    cout << "-1\n";
  else
    cout << mincost << "\n";
}
