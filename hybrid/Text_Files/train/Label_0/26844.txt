#include <bits/stdc++.h>
using namespace std;
int n;
char s[51][51];
int ans[51][51][51][51];
int solve(int r1, int c1, int r2, int c2) {
  if (r1 == r2 && c1 == c2) ans[r1][c1][r2][c2] = (s[r1][c1] == '#');
  if (ans[r1][c1][r2][c2] != -1) return ans[r1][c1][r2][c2];
  ans[r1][c1][r2][c2] = max(r2 - r1 + 1, c2 - c1 + 1);
  int cans = ans[r1][c1][r2][c2];
  for (int i = r1 + 1; i <= r2; i++) {
    cans = min(cans, solve(r1, c1, i - 1, c2) + solve(i, c1, r2, c2));
  }
  for (int i = c1 + 1; i <= c2; i++) {
    cans = min(cans, solve(r1, c1, r2, i - 1) + solve(r1, i, r2, c2));
  }
  ans[r1][c1][r2][c2] = cans;
  return ans[r1][c1][r2][c2];
}
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%s", s[i]);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      for (int k = 0; k < n; k++)
        for (int l = 0; l < n; l++) ans[i][j][k][l] = -1;
  int ans = solve(0, 0, n - 1, n - 1);
  printf("%d\n", ans);
}
