#include <bits/stdc++.h>
using namespace std;
const int INF = 1000000001;
const long double EPS = 1e-9;
const int MOD = 1000000007;
const long long LLINF = 1000000000000000001;
int n;
const int maxn = 100;
long long dp[maxn][2][2];
long long a[maxn];
int main() {
  ios_base::sync_with_stdio(false);
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> a[i];
  for (int t = n; t >= 1; t--)
    for (int p = 0; p <= 1; p++) {
      dp[t][p][p] = max(dp[t + 1][p][p], dp[t + 1][p ^ 1][p] + a[t]);
      dp[t][p][p ^ 1] =
          min(dp[t + 1][p][p ^ 1] + a[t], dp[t + 1][p ^ 1][p ^ 1]);
    }
  cout << dp[1][0][1] << ' ' << dp[1][1][1] << endl;
}
