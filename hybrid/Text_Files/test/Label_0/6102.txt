#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define pb push_back

typedef long long LL;
typedef long double LD;

const LL INF = (1LL << 60);

typedef vector<LL> VLL;
LL knapsack_01(VLL& v, VLL& w, int n, LL W);

int main() {

  ios_base::sync_with_stdio(0); cin.tie(0);

  int n; LL W;
  cin >> n >> W;

  VLL v, w;
  v.assign(n + 1, 0);
  w.assign(n + 1, 0);
  for (int i = 1; i <= n; i++) {
    cin >> v[i] >> w[i];
  }

  LL ans = knapsack_01(v, w, n, W);

  cout << ans << endl;

  return 0;
}

/**
 *
 * tested on http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B
 */
LL dp[105][10005];
LL knapsack_01(VLL& v, VLL& w, int n, LL W) {
  LL sum = 0;
  for (int val : v)
    sum += val;

  LL ans = 0;
  for (int j = 1; j <= sum; j++)
    dp[0][j] = INF;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= sum; j++) {
      dp[i][j] = dp[i-1][j];
      if (v[i] <= j)
        dp[i][j] = min(dp[i][j],
                       dp[i-1][j-v[i]] + w[i]);
      if (ans < j && dp[i][j] <= W)
        ans = j;
    }
  }

  return ans;
}
