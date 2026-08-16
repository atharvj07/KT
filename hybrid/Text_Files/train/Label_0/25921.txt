#include <bits/stdc++.h>
using namespace std;
struct edge {
  int u, v;
  long long w;
};
long long MOD = 1000000007;
long long _MOD = 1000000009;
double EPS = 1e-10;
int main() {
  int N;
  cin >> N;
  vector<vector<double> > p(N, vector<double>(N));
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++) cin >> p[i][j];
  vector<vector<double> > dp(1 << N, vector<double>(N));
  dp[0][0] = 1;
  for (int S = 1; S < 1 << N; S++)
    for (int i = 0; i < N; i++) {
      if (S >> i & 1) continue;
      for (int j = 0; j < N; j++) {
        if (!(S >> j & 1)) continue;
        int _S = S - (1 << j);
        dp[S][i] = max(dp[S][i], dp[_S][i] * p[i][j] + dp[_S][j] * p[j][i]);
      }
    }
  double ma = 0;
  for (int i = 0; i < N; i++) ma = max(ma, dp[(1 << N) - 1 - (1 << i)][i]);
  printf("%.15f\n", ma);
}
