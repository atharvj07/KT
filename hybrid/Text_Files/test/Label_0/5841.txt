#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("Ofast")
const int MAXN = 2048;
const int MOD = 1e6 + 3;
char s[MAXN], S[MAXN], *ch = s;
int dp[MAXN][MAXN], n = -1;
int sign_l[MAXN], num_p[MAXN], sign_p[MAXN];
inline char getnext() {
  if (*ch == 0) return 0;
  if (*ch == '+' || *ch == '-') {
    ++ch;
    return '+';
  } else if (*ch == '*' || *ch == '/') {
    ++ch;
    return '*';
  } else {
    while ('0' <= *ch && *ch <= '9') ++ch;
    return '0';
  }
}
inline bool check() {
  if (S[0] == '*' || S[0] == '/' || S[n - 1] != '0') {
    return false;
  }
  for (register int i = (0); i < (n); ++i) {
    if (S[i] != '0' && S[i + 1] == '*') {
      return false;
    }
  }
  return true;
}
inline int Mod(long long x) { return x - x / MOD * MOD; }
inline int dfs(int l, int r) {
  if (r < 0) return 0;
  if (~dp[l][r]) return dp[l][r];
  if (l == n) return dp[l][r] = (r == 0);
  if (S[l] != '0')
    return dp[l][r] = dfs(l + 1, r + 1);
  else
    return dp[l][r] = Mod(dfs(l + 1, r) + dfs(l, r - 1));
}
int main() {
  gets(s);
  while ((S[++n] = getnext()))
    ;
  if (!check()) {
    puts("0");
    return 0;
  }
  memset(dp, -1, sizeof(dp));
  cout << dfs(0, 0) << '\n';
  return 0;
}
