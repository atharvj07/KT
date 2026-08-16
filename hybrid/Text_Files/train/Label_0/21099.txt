#include <bits/stdc++.h>
using namespace std;
bool debug = false;
int n, m, k;
int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};
long long ln, lk, lm;
vector<int> sc[100005];
long long dp[2][100005];
long long sss(int c, int num) {
  if (sc[c].empty()) return 0;
  return upper_bound(sc[c].begin(), sc[c].end(), num) - sc[c].begin();
}
void cal() {
  for (int(i) = 0; (i) < (int)(2); (i)++)
    for (int(j) = 0; (j) < (int)(100005); (j)++) dp[i][j] = 3 * k;
  if (!sc[n].empty() && sc[n].back() == n)
    dp[1][0] = 3;
  else
    dp[1][0] = 0;
  dp[1][1] = 0;
  long long M = sqrt(k * 6);
  int T = 1;
  for (int i = 2; i <= n; i++) {
    T ^= 1;
    dp[T][0] = 3 * k;
    for (int kk = 0; kk <= i; kk++) {
      long long tmp = kk >= 1 ? dp[T ^ 1][kk - 1] : dp[T ^ 1][0];
      if (kk) {
        long long y = kk * (kk + 1) / 2 + 2;
        if (y > 3 * k) break;
        tmp += y;
      }
      tmp += sss(n + 1 - i, n - kk) * 3;
      dp[T][0] = min(dp[T][0], tmp);
    }
    for (int j = 1; j <= i && j <= M; j++) {
      dp[T][j] = 3 * k;
      dp[T][j] =
          min(dp[T][j - 1], dp[T ^ 1][j - 1] + sss(n + 1 - i, n - j) * 3);
    }
  }
  cout << dp[T][0] << endl;
}
int main() {
  scanf("%d%d", &n, &k);
  int r, c;
  for (int(i) = 0; (i) < (int)(k); (i)++) {
    scanf("%d%d", &r, &c);
    sc[c].push_back(r);
  }
  for (int(i) = 1; (i) <= (int)(n); (i)++)
    if (!sc[i].empty()) {
      sort(sc[i].begin(), sc[i].end());
    }
  cal();
  return 0;
}
