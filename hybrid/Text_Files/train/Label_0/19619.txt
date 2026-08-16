#include <bits/stdc++.h>
int dp[5001][5001];
char s[5001];
int main() {
  scanf("%s", s);
  int n;
  scanf("%d", &n);
  for (int i = 0; *(s + i); i++) {
    dp[i][i] = 1;
    for (int j1 = i - 1, j2 = i + 1; j1 >= 0 && *(s + j2); j1--, j2++)
      if (s[j1] == s[j2])
        dp[j1][j2] = 1;
      else
        break;
    if (s[i] == s[i + 1]) {
      dp[i][i + 1] = 3;
      for (int j1 = i - 1, j2 = i + 2; j1 >= 0 && *(s + j2) && *(s + j2 - 1);
           j1--, j2++)
        if (s[j1] == s[j2])
          dp[j1][j2] = 1;
        else
          break;
    } else
      dp[i][i + 1] = 2;
  }
  for (int k = 2; *(s + k); k++)
    for (int i = 0; *(s + i + k); i++)
      dp[i][i + k] +=
          dp[i][i + k - 1] + dp[i + 1][i + k] - dp[i + 1][i + k - 1];
  while (n--) {
    int i, j;
    scanf("%d%d", &i, &j);
    printf("%d\n", dp[i - 1][j - 1]);
  }
  return 0;
}
