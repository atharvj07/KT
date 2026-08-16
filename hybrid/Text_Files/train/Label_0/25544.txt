#include <bits/stdc++.h>
using namespace std;
int const maxn = int(1e5 + 5);
int n;
long long dp[3][maxn], a[maxn], b[maxn];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
  }
  for (int i = 1; i <= n; i++) {
    cin >> b[i];
  }
  dp[1][1] = a[1];
  dp[2][1] = b[1];
  for (int i = 2; i <= n; i++) {
    dp[1][i] = max(dp[2][i - 1] + a[i], dp[1][i - 1]);
    dp[2][i] = max(dp[1][i - 1] + b[i], dp[2][i - 1]);
  }
  cout << max(dp[1][n], dp[2][n]);
  return 0;
}
