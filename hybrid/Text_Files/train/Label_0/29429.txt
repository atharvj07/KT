#include <bits/stdc++.h>
using namespace std;
const int N = 1e2 + 2;
const long double EPS = 1e-9;
long double x[N], y[N];
long double xo, yo;
long double dp[N][N];
long double e;
long double getval(int k, int i, int j, long double mid) {
  long double d = (x[i] - xo) * (x[i] - xo) + (y[i] - yo) * (y[i] - yo);
  long double p = (EPS + mid * mid >= d ? 1 : exp(1.0 - d / (mid * mid)));
  if (k > 0)
    return dp[i - 1][j - 1] * p + dp[i - 1][j] * (1 - p);
  else
    return dp[i - 1][j] * (1 - p);
}
bool ok(long double mid, int k, int n) {
  memset(dp, 0, sizeof(dp));
  dp[0][0] = 1;
  for (int(i) = (1); (i) < (n + 1); (i)++)
    for (int(j) = (0); (j) < (i + 1); (j)++) dp[i][j] = getval(k, i, j, mid);
  long double ans = 0;
  for (int(i) = (n); (i) >= (k); (i)--) ans += dp[n][i];
  return 1 - e <= ans;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  ;
  int n;
  cin >> n;
  int k;
  cin >> k >> e;
  e *= 0.001;
  cin >> xo >> yo;
  for (int(i) = (1); (i) < (n + 1); (i)++) cin >> x[i] >> y[i];
  long double low = 0, high = 1e18;
  for (int(i) = (0); (i) < (100); (i)++) {
    long double mid = (low + high) / 2;
    if (ok(mid, k, n))
      high = mid;
    else
      low = mid;
  }
  cout << fixed << setprecision(10) << high << endl;
  return 0;
}
