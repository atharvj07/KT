#include <bits/stdc++.h>
using namespace std;
long long const MAXN = 2005;
long long l[MAXN], r[MAXN], a[MAXN];
long long C[MAXN][MAXN];
long long R[MAXN][MAXN];
long long f[MAXN];
signed main() {
  long long n, k;
  cin >> n >> k;
  for (register long long i = 1; i <= n; ++i) cin >> l[i] >> r[i] >> a[i];
  l[n + 1] = r[n + 1] = 1e18;
  for (register long long i = 1; i <= n; ++i) {
    long long nowtim = l[i], res = k, cost = 1;
    for (register long long j = i; j <= n; ++j) {
      if (nowtim < l[j] && res == 0) res = k, ++cost;
      nowtim = max(nowtim, l[j]);
      long long tim = (a[j] - res + k - 1) / k;
      cost += tim;
      nowtim += tim;
      res = tim * k + res - a[j];
      if (nowtim > r[j]) break;
      if (nowtim < l[j + 1]) C[i][j] = cost, R[i][j] = res;
    }
  }
  memset(f, 0x3f, sizeof(f));
  f[0] = 0;
  for (register long long i = 1; i < n; ++i)
    for (register long long j = 1; j <= i; ++j)
      if (C[j][i] != 0) f[i] = min(f[i], f[j - 1] + C[j][i] * k);
  for (register long long j = 1; j <= n; ++j)
    if (C[j][n] != 0) f[n] = min(f[n], f[j - 1] + C[j][n] * k - R[j][n]);
  if (f[n] == 0x3f3f3f3f3f3f3f3f)
    cout << -1 << endl;
  else
    cout << f[n] << endl;
  return 0;
}
