#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:100000000000000")
using namespace std;
int n, col[500001], k;
string st;
int dp[500001][26], pa[500001][26];
int rec(int p, int bef) {
  if (p == n) return 0;
  if (~dp[p][bef]) return dp[p][bef];
  int ret = 0;
  int nx = 0;
  for (int j = 0; j < 3; j++)
    if ((p == 0 || bef != j) && (p == n - 1 || col[p + 1] != j)) {
      nx = j;
      break;
    }
  if (p == 0) {
    ret = rec(p + 1, col[p]);
    int ret2 = rec(p + 1, nx) + 1;
    if (ret2 > ret)
      pa[p][bef] = col[p];
    else
      pa[p][bef] = nx, ret = ret2;
    return dp[p][bef] = ret;
  }
  ret = 1 + rec(p + 1, nx);
  pa[p][bef] = nx;
  if (bef != col[p]) {
    int ret2 = rec(p + 1, col[p]);
    if (ret2 < ret) pa[p][bef] = col[p], ret = ret2;
  }
  return dp[p][bef] = ret;
}
int main() {
  cin >> n >> k >> st;
  for (int i = 0; i < n; i++) col[i] = st[i] - 'A';
  if (k == 2) {
    int ans = 0;
    for (int i = 0; i < n; i++)
      if (col[i] != (i & 1)) ans++;
    int ans2 = 0;
    for (int i = 0; i < n; i++)
      if (col[i] == (i & 1)) ans2++;
    cout << min(ans, ans2) << endl;
    if (ans <= ans2) {
      for (int i = 0; i < n; i++)
        if (i & 1)
          st[i] = 'B';
        else
          st[i] = 'A';
    } else
      for (int i = 0; i < n; i++)
        if (i & 1)
          st[i] = 'A';
        else
          st[i] = 'B';
    cout << st << endl;
    return 0;
  }
  memset((dp), (-1), sizeof(dp));
  int ans = rec(0, 0);
  cout << ans << endl;
  int p = 0, c = 0;
  while (p < n) {
    cout << char('A' + pa[p][c]);
    c = pa[p][c];
    p++;
  }
  return 0;
}
