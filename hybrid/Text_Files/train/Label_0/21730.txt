#include <bits/stdc++.h>
using namespace std;
const long long MAXN = 1e6;
const long long MOD = 1e9 + 9;
const long double eps = 1e-6;
const long long INF = 1e15;
int a[300];
double p[300];
int N, L, K;
double dp[202][202][605];
int main() {
  cin >> N >> L >> K;
  for (int i = 0; i < N; ++i) {
    cin >> p[i];
    p[i] /= 100;
  }
  int maxCnt = 0;
  for (int i = 0; i < N; ++i) {
    cin >> a[i];
  }
  dp[0][0][K + 200] = 1;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j <= i; ++j) {
      for (int k = 0; k <= 600; ++k) {
        dp[i + 1][j][k] += dp[i][j][k] * (1 - p[i]);
        int kk = k + a[i];
        if (kk >= 600) kk = 600;
        if (kk < 0) kk = 0;
        dp[i + 1][j + 1][kk] += dp[i][j][k] * p[i];
      }
    }
  }
  double ans = 0;
  for (int i = L; i <= N; ++i) {
    for (int j = 200; j <= 600; ++j) {
      ans += dp[N][i][j];
    }
  }
  cout << fixed << setprecision(10) << ans;
  return 0;
}
