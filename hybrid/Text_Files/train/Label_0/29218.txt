#include <bits/stdc++.h>
using namespace std;
const double eps = 1.0e-11;
const double pi = acos(-1.0);
const int INF = 1000000000;
const int N = 110;
vector<pair<int, int> > pe;
int dp[N][N][N];
int n, k;
int solve(int pt) {
  if (pt > n) return INF;
  for (long long i = 0; i < N; i++)
    for (long long j = 0; j < N; j++)
      for (long long t = 0; t < N; t++) dp[i][j][t] = INF;
  dp[0][0][pe[0].first + 1 < pt] = 0;
  dp[0][1][pe[0].first <= pt] = pe[0].second;
  for (long long i = 1; i <= n - 1; i++) {
    for (long long j = 0; j < n + 1; j++)
      for (long long t = 0; t < n + 1; t++) {
        dp[i][j + 1][t + (pe[i].first <= pt)] =
            min(dp[i][j + 1][t + (pe[i].first <= pt)],
                dp[i - 1][j][t] + pe[i].second);
        dp[i][j][t + (pe[i].first + 1 < pt)] =
            min(dp[i][j][t + (pe[i].first + 1 < pt)], dp[i - 1][j][t]);
      }
  }
  int need = n + 1 - k;
  int res = INF;
  for (long long pos = need; pos <= n; pos++)
    res = min(res, dp[n - 1][pt][pos]);
  return res;
}
int main() {
  cin >> n >> k;
  pe.resize(n);
  for (long long i = 0; i < n; i++) {
    cin >> pe[i].first >> pe[i].second;
  }
  if (k == n + 1) {
    cout << "0\n";
    return 0;
  }
  sort((pe).begin(), (pe).end());
  reverse((pe).begin(), (pe).end());
  int res = INF;
  for (long long pt = pe[k - 1].first; pt <= pe[k - 1].first + 2; pt++)
    res = min(res, solve(pt));
  if (res == INF)
    cout << "-1\n";
  else
    cout << res << endl;
  return 0;
}
