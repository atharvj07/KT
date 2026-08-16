#include <bits/stdc++.h>
using namespace std;
const int maxn = 1000 + 10;
const int Mod = 1e9 + 7;
const int N = 2;
string s1, s2;
int bits[maxn];
int n, k;
long long dp[maxn][1010][2];
long long dfs(int pos, bool flags, int pre, bool flag) {
  if (pos < 0) return flags;
  if (!flag && dp[pos][pre][flags] != -1) return dp[pos][pre][flags];
  int up = flag ? bits[pos] : 9;
  long long ret = 0;
  for (int i = 0; i <= up; i++) {
    if (i == 4 || i == 7) {
      ret = (ret + dfs(pos - 1, flags || (pre != -1 && (abs(pre - pos) <= k)),
                       pos, flag && i == up)) %
            Mod;
    } else
      ret = (ret + dfs(pos - 1, flags, pre, flag && i == up)) % Mod;
  }
  if (!flag) dp[pos][pre][flags] = ret;
  return ret;
}
long long calc(string t) {
  int len = 0;
  for (int i = t.size() - 1; i >= 0; i--) bits[len++] = t[i] - '0';
  return dfs(len - 1, false, -1, true);
}
int main() {
  memset(dp, -1, sizeof dp);
  while (~scanf("%d%d", &n, &k)) {
    for (int i = 1; i <= n; i++) {
      cin >> s1 >> s2;
      int flag = 0;
      int len = s1.size(), temp = -k - 2;
      for (int i = 0; i < len; i++)
        if (s1[i] == '4' || s1[i] == '7') {
          if (abs(i - temp) <= k) {
            flag = 1;
            break;
          } else
            temp = i;
        }
      printf("%I64d\n", ((calc(s2) - calc(s1) + flag) % Mod + Mod) % Mod);
    }
  }
  return 0;
}
