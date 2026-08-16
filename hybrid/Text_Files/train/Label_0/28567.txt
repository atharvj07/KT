#include <bits/stdc++.h>
using namespace std;
template <class T1, class T2>
int upmax(T1 &x, T2 v) {
  if (x >= v) return 0;
  return x = v, 1;
}
const int MAXN = 5000;
int N;
int A[MAXN];
long long dp[MAXN + 1][4];
pair<int, int> pre[MAXN + 1][4];
int main() {
  ios::sync_with_stdio(false);
  cin >> N;
  for (int i = 0; i < N; ++i) {
    cin >> A[i];
  }
  memset(dp, 0xc0, sizeof(dp));
  dp[0][0] = 0;
  for (int i = 0; i <= N; ++i) {
    for (int j = 0; j < 4; ++j) {
      if (j + 1 < 4) {
        if (upmax(dp[i][j + 1], dp[i][j])) {
          pre[i][j + 1] = make_pair(i, j);
        }
      }
      if (i == N) continue;
      if (~j & 1) {
        if (upmax(dp[i + 1][j], dp[i][j] + A[i])) {
          pre[i + 1][j] = make_pair(i, j);
        }
      } else {
        if (upmax(dp[i + 1][j], dp[i][j] - A[i])) {
          pre[i + 1][j] = make_pair(i, j);
        }
      }
    }
  }
  vector<int> ans;
  for (int i = N, j = 3; i;) {
    int pi, pj;
    tie(pi, pj) = pre[i][j];
    if (j != pj) {
      ans.emplace_back(pi);
    }
    i = pi;
    j = pj;
  }
  for (int i = 0; i < 3 - ans.size(); ++i) {
    cout << 0 << " ";
  }
  for (int i = int(ans.size()) - 1; i >= 0; --i) {
    cout << ans[i] << " \n"[i == 0];
  }
  return 0;
}
