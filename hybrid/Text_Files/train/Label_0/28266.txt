#include <bits/stdc++.h>
using namespace std;
int ans(vector<vector<int> > &dp, int n, int v, int limit, int x) {
  if (dp[n][v] != x) {
    return dp[n][v];
  }
  if (n == 1) {
    return dp[n][v] = v;
  }
  int min_1 = INT_MAX;
  if (v + 1 <= limit) {
    min_1 = min(min_1, 0 + ans(dp, n - 1, v + 1, limit, x));
  }
  for (int i = v; i >= 0; i--) {
    min_1 = min(min_1, n * (v - i + 1) + ans(dp, n - 1, i, limit, x));
  }
  return dp[n][v] = min_1;
}
int main() {
  int n, v;
  cin >> n >> v;
  vector<vector<int> > dp(n + 1, vector<int>(v + 1, (n * v)));
  int min_1 = INT_MAX;
  for (int i = 0; i < v; i++) {
    min_1 = min(min_1, ans(dp, n, i, v, (n * v)));
  }
  cout << min_1 << endl;
  return 0;
}
