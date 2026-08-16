#include <bits/stdc++.h>
using namespace std;
long long int arr[100005], dp[100005];
int main() {
  int t, n, k;
  cin >> t;
  while (t--) {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> arr[i];
    long long int res = 0;
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= n; i++) {
      dp[i] = 1;
      long long int ans = 1;
      for (int j = 1; j * j <= i; j++) {
        if (i % j == 0 && arr[j] < arr[i]) {
          ans = max(ans, dp[j] + 1);
        }
        int d = i / j;
        if (d != j) {
          if (i % d == 0 && arr[d] < arr[i]) ans = max(ans, dp[d] + 1);
        }
      }
      dp[i] = max(ans, dp[i]);
      res = max(dp[i], res);
    }
    cout << res << endl;
  }
}
