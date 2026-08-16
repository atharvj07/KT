#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 2;
long long a[N], dp[N], dpp[N];
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long t, i, x, n, ans = 0;
  cin >> n;
  for (i = 1; i <= n; i++) {
    cin >> a[i];
    dp[i] = 1;
    dpp[i] = 1;
  }
  for (i = 2; i <= n; i++) {
    if (a[i] == a[i - 1]) {
      dp[i] += dp[i - 1];
    }
  }
  for (i = n - 1; i > 0; i--) {
    if (a[i] == a[i + 1]) {
      dpp[i] += dpp[i + 1];
    }
  }
  for (i = 1; i < n; i++) {
    if (a[i] != a[i + 1]) {
      ans = max(ans, (min(dp[i], dpp[i + 1])) * 2);
    }
  }
  cout << ans << "\n";
  return 0;
}
