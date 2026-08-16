#include <bits/stdc++.h>
using namespace std;
int k, n;
char s[1000013];
long long int dp1[1000013];
long long int dp2[1000013];
long long int calc[1000013];
int main() {
  scanf("%d%d%s", &n, &k, s + 1);
  int form = n + 1;
  dp2[n + 1] = 1;
  calc[n + 1] = 1;
  for (int i = n; i >= 1; i--) {
    if (s[i] == 'X') {
      dp2[i] = dp2[i + 1] << 1;
      calc[i] = calc[i + 1] << 1;
    } else {
      dp2[i] = dp2[i + 1];
      calc[i] = calc[i + 1];
    }
    dp2[i] = dp2[i] % 1000000007;
    calc[i] = calc[i] % 1000000007;
    if (s[i] == 'B') form = i;
    if (form >= i + k && (i + k == n + 1 || s[i + k] != 'W'))
      dp2[i] = (dp2[i] - (i + k == n + 1 ? 1 : dp2[i + k + 1]) + 1000000007) %
               1000000007;
  }
  form = 0;
  dp1[0] = 1;
  long long int ans = 0;
  for (int i = 1; i <= n; i++) {
    if (s[i] == 'X')
      dp1[i] = dp1[i - 1] << 1;
    else
      dp1[i] = dp1[i - 1];
    dp1[i] = dp1[i] % 1000000007;
    if (s[i] == 'W') form = i;
    if (form <= i - k && (i - k == 0 || s[i - k] != 'B')) {
      dp1[i] = (dp1[i] - (i - k == 0 ? 1 : dp1[i - k - 1]) + 1000000007) %
               1000000007;
      if (i >= k && i + k - 1 <= n)
        ans = (ans +
               (i - k == 0 ? 1 : dp1[i - k - 1]) * (calc[i + 1] - dp2[i + 1]) +
               1000000007) %
              1000000007;
    }
  }
  cout << (ans + 1000000007) % 1000000007 << endl;
  return 0;
}
