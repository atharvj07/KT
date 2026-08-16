#include <bits/stdc++.h>
using namespace std;
int n, x, l, ans;
int dp[100010], a[100010];
int main() {
  int i, j;
  cin >> n;
  for (i = 1; i <= n; i++) {
    scanf("%d", a + i);
  }
  for (i = 1; i <= n; i++) {
    dp[a[i]] = dp[a[i] - 1] + 1;
    ans = max(ans, dp[a[i]]);
  }
  cout << n - ans << endl;
}
