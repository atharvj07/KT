#include <bits/stdc++.h>
using namespace std;
const int maxn = 5e3 + 70;
const int INF = 2.1e9;
const long long inf = 1e18;
const int MOD = 1e9 + 7;
int n, m, k, x;
int a[maxn];
long long dp[maxn][maxn];
int Q[maxn], front, tail;
long long solve() {
  for (int i = 1; i <= n; i++) dp[i][1] = (i > k ? -inf : a[i]);
  for (int j = 2; j <= x; j++) {
    front = tail = 0;
    Q[tail++] = 0;
    for (int i = 1; i <= n; i++) {
      while (Q[front] < i - k) front++;
      dp[i][j] = dp[Q[front]][j - 1] + a[i];
      while (front < tail && dp[Q[tail - 1]][j - 1] <= dp[i][j - 1]) tail--;
      Q[tail++] = i;
    }
  }
  if (dp[n - k + 1][x] <= 0) return -1;
  long long ans = 0;
  for (int i = n - k + 1; i <= n; i++) ans = max(ans, dp[i][x]);
  return ans;
}
int main() {
  while (cin >> n >> k >> x) {
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    long long ans = solve();
    cout << ans << endl;
  }
  return 0;
}
