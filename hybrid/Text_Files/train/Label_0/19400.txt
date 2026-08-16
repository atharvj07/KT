#include <bits/stdc++.h>
using namespace std;
const int NMAX = 333333;
const int WMAX = 111111;
int dp[NMAX];
int n, m;
vector<pair<int, int> > e[WMAX];
int main() {
  cin.sync_with_stdio(0);
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    e[w].push_back(pair<int, int>(u, v));
  }
  for (int w = 1; w < WMAX; w++) {
    vector<pair<int, int> > query;
    for (int j = 0; j < e[w].size(); j++) {
      pair<int, int> road = e[w][j];
      query.push_back(pair<int, int>(road.second, dp[road.first] + 1));
    }
    for (int i = 0; i < query.size(); i++) {
      dp[query[i].first] = max(dp[query[i].first], query[i].second);
    }
  }
  cout << *max_element(dp + 1, dp + 1 + n);
}
