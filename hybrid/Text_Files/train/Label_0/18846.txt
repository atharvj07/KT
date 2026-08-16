#include <bits/stdc++.h>
using namespace std;
const int maxN = 26, maxE = 13e5;
int ans[2][maxN], a[2 * maxN];
long long dp[maxN][maxE];
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < 2 * n; i++) cin >> a[i];
  sort(a, a + 2 * n);
  ans[0][0] = a[0];
  ans[1][n - 1] = a[1];
  for (int i = 0; i < 2 * n - 2; i++) a[i] = a[i + 2];
  n--;
  int sum = 0;
  for (int i = 0; i < 2 * n; i++) sum += a[i];
  memset(dp, -1, sizeof dp);
  dp[0][0] = 0;
  for (int i = 0; i < 2 * n; i++)
    for (int k = maxN - 1; k >= 0; k--)
      for (int x = a[i]; x < maxE; x++)
        if (k && dp[k - 1][x - a[i]] != -1)
          dp[k][x] = dp[k - 1][x - a[i]] + (1LL << i);
  long long best = 1e18;
  for (int i = 0; i < maxE; i++)
    if (dp[n][i] != -1)
      if (max(i, sum - i) <= max(best, sum - best)) best = i;
  vector<int> v1;
  for (int j = 0; j < 2 * n; j++)
    if (dp[n][best] & (1LL << j)) v1.push_back(a[j]);
  vector<int> v2;
  for (int j = 0; j < 2 * n; j++)
    if ((dp[n][best] & (1LL << j)) == 0) v2.push_back(a[j]);
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());
  reverse(v2.begin(), v2.end());
  for (int j = 0; j < n; j++) {
    ans[0][j + 1] = v1[j];
    ans[1][j] = v2[j];
  }
  for (int i = 0; i < 2; i++, cout << endl)
    for (int j = 0; j < n + 1; j++) cout << ans[i][j] << " ";
}
