#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100010;
char s[MAXN];
int n, q;
unsigned int dp[2][MAXN];
int main() {
  cin >> n;
  scanf("%s", s);
  for (int i = 0; s[i]; i++)
    if (s[i] == '?') q++;
  if ((n & 1) || (q < n / 2)) {
    printf("0\n");
    return 0;
  }
  memset(dp, 0, sizeof(dp));
  int cur = 0;
  dp[cur][0] = 1;
  int L = n >> 1;
  for (int i = 0; i < n; i++) {
    int l = max(0, i + 1 - L), r = (i + 1) / 2;
    cur ^= 1;
    int las = cur ^ 1;
    for (int j = l; j <= r; j++) dp[cur][j] = dp[las][j];
    for (int j = 0; j < l; j++) dp[cur][j] = 0;
    for (int j = r + 1; j <= L; j++) dp[cur][j] = 0;
    if (s[i] == '?')
      for (int j = max(1, l); j <= r; j++) dp[cur][j] += dp[las][j - 1];
    if (1 == 2) i++;
  }
  unsigned int ans = dp[cur][L];
  int t = (q - L);
  while (t) ans = ans * 25, t--;
  cout << ans << endl;
  return 0;
}
