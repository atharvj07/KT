#include <bits/stdc++.h>
using namespace std;
int n, k;
long long a[500005];
long long dp[5005][5005];
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; i++) scanf("%I64d", &a[i]);
  sort(a + 1, a + 1 + n);
  int len1 = n / k + 1, num1 = n % k;
  int len2 = n / k, num2 = k - n % k;
  memset(dp, 0x3f, sizeof(dp));
  dp[0][0] = 0;
  for (int i = 0; i <= num1; i++) {
    for (int j = 0; j <= num2; j++) {
      if (i) {
        int s = (i - 1) * len1 + j * len2 + 1;
        int e = s + len1 - 1;
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + a[e] - a[s]);
      }
      if (j) {
        int s = i * len1 + (j - 1) * len2 + 1;
        int e = s + len2 - 1;
        dp[i][j] = min(dp[i][j], dp[i][j - 1] + a[e] - a[s]);
      }
    }
  }
  printf("%I64d\n", dp[num1][num2]);
}
