#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
char s[N], t[N];
int n, m;
int ch[N][26];
int lps[N];
void calcLps() {
  memset(lps, 0, sizeof(lps));
  int i = 1;
  int len = 0;
  lps[0] = 0;
  while (i < m) {
    if (t[i + 1] == t[len + 1]) {
      len++;
      lps[i] = len;
      i++;
    } else {
      if (len == 0) {
        lps[i] = 0;
        i++;
      } else {
        len = lps[len - 1];
      }
    }
  }
}
int main() {
  scanf("%s", s + 1);
  scanf("%s", t + 1);
  n = strlen(s + 1), m = strlen(t + 1);
  for (int i = 1; i <= m; i++) ch[i - 1][t[i] - 'a'] = i;
  calcLps();
  for (int i = 1; i <= m; i++) {
    for (int j = 0; j < 26; j++) {
      if (!ch[i][j]) {
        ch[i][j] = ch[lps[i - 1]][j];
      }
    }
  }
  vector<vector<int> > dp(n + 1, vector<int>(m + 1, -1));
  dp[0][0] = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= m; j++) {
      if (dp[i][j] == -1) continue;
      if (s[i + 1] == '?') {
        for (int c = 0; c < 26; c++) {
          dp[i + 1][ch[j][c]] =
              max(dp[i + 1][ch[j][c]], dp[i][j] + (ch[j][c] == m));
        }
      } else {
        int c = s[i + 1] - 'a';
        dp[i + 1][ch[j][c]] =
            max(dp[i + 1][ch[j][c]], dp[i][j] + (ch[j][c] == m));
      }
    }
  }
  int ans = 0;
  for (int i = 0; i <= m; i++) {
    ans = max(ans, dp[n][i]);
  }
  printf("%d\n", ans);
  return 0;
}
