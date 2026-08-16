#include <bits/stdc++.h>
using namespace std;
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, -1, 0, 1};
const int dx8[] = {-1, 0, 1, 0, 1, 1, -1, -1};
const int dy8[] = {0, -1, 0, 1, 1, -1, 1, -1};
long long min(long long a, long long b) {
  if (a < b) return a;
  return b;
}
vector<pair<int, int>> arr;
vector<vector<long long>> dp;
long long solve(long long pos, long long stamp) {
  if (pos == arr.size()) return 0;
  if (dp[pos][stamp] != -1) return dp[pos][stamp];
  long long ans = INT_MAX;
  ans = min(ans, arr[pos].second + solve(pos + 1, pos));
  ans = min(ans, arr[pos].first - arr[stamp].first + solve(pos + 1, stamp));
  dp[pos][stamp] = ans;
  return ans;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long n;
  cin >> n;
  arr.clear();
  for (int i = 0; i < n; ++i) {
    long long x, y;
    cin >> x >> y;
    arr.push_back({x, y});
  }
  dp.clear();
  dp.resize(n, vector<long long>(n, -1));
  sort(arr.begin(), arr.end());
  cout << arr[0].second + solve(1, 0) << '\n';
}
