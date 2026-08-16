#include <bits/stdc++.h>
using namespace std;
mt19937_64 mt(chrono::steady_clock::now().time_since_epoch().count());
const int MOD = 1e9 + 7, MAX = INT_MAX / 100;
const long long INF = 1e18;
const long double PI = 4 * atan((long double)1);
int dp1[1000005], dp2[1000005], mindp[1000005];
int n, m;
int s[1000005], x[1000005];
vector<pair<int, int> > A;
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  ;
  cin >> n >> m;
  for (int i = 1, st, xt; i <= n; i++) {
    cin >> st >> xt;
    A.emplace_back(st, xt);
  }
  sort(begin(A), end(A));
  for (int i = 1; i <= n; i++) s[i] = A[i - 1].first, x[i] = A[i - 1].second;
  for (int i = 0; i <= n + 5; i++)
    for (int j = 0; j < m + 5; j++) dp1[j] = dp2[j] = mindp[j] = MAX;
  dp1[0] = mindp[0] = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j <= m; j++) dp2[j] = min(dp2[j], dp1[j]);
    for (int j = x[i]; j <= m; j++) {
      int r = min(s[i] + j, m), l = max(s[i] - j, 1);
      dp2[r] = min(dp2[r], mindp[l - 1] + (j - x[i]));
    }
    for (int j = m + 1; j >= 0; j--) {
      mindp[j] = j == m + 1 ? MAX : min(mindp[j + 1], dp2[j]);
      dp1[j] = dp2[j];
      dp2[j] = MAX;
    }
  }
  cout << dp1[m];
}
