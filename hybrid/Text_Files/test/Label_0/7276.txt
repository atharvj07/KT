#include <bits/stdc++.h>
using namespace std;
const long long mod = (long long)1e9 + 7;
signed main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  long long n, m;
  cin >> n >> m;
  long long a[n][m];
  for (long long i = 0; i < n; ++i) {
    for (long long j = 0; j < m; ++j) {
      char now;
      cin >> now;
      if (now == '.')
        a[i][j] = 0;
      else
        a[i][j] = 1;
    }
  }
  long long up[n][m];
  long long left[n][m];
  long long cntd[n][m];
  long long cntr[n][m];
  for (long long i = 0; i < n; ++i) {
    for (long long j = 0; j < m; ++j)
      up[i][j] = left[i][j] = cntd[i][j] = cntr[i][j] = 0;
  }
  for (long long i = 0; i < n; ++i) {
    if (a[i][m - 1]) cntr[i][m - 1] = 1;
    for (long long j = m - 2; j >= 0; --j) {
      cntr[i][j] += cntr[i][j + 1];
      if (a[i][j]) ++cntr[i][j];
    }
  }
  for (long long j = 0; j < m; ++j) {
    if (a[n - 1][j]) cntd[n - 1][j] = 1;
    for (long long i = n - 2; i >= 0; --i) {
      cntd[i][j] += cntd[i + 1][j];
      if (a[i][j]) ++cntd[i][j];
    }
  }
  for (long long j = 1; j < m - cntr[0][0]; ++j) left[0][j] = 1;
  for (long long i = 0; i < n - cntd[0][0]; ++i) up[i][0] = 1;
  vector<long long> ui(n), uj(m);
  vector<long long> nowi(n), nowj(m);
  for (long long i = 1; i < n; ++i) {
    nowi[i] = up[i][0];
  }
  for (long long j = 1; j < m; ++j) {
    nowj[j] = left[0][j];
  }
  for (long long d = 2; d <= n + m - 2; ++d) {
    for (long long i = 1; i < n; ++i) {
      long long j = d - i;
      if (j >= m || j <= 0) continue;
      while (uj[j] < i && cntd[uj[j]][j] > n - (a[uj[j]][j] ? 0 : 1) - i) {
        nowj[j] = (nowj[j] - left[uj[j]][j] + mod) % mod;
        uj[j]++;
      }
      if (uj[j] < i) up[i][j] = nowj[j];
      while (ui[i] < j && cntr[i][ui[i]] > m - (a[i][ui[i]] ? 0 : 1) - j) {
        nowi[i] = (nowi[i] - up[i][ui[i]] + mod) % mod;
        ui[i]++;
      }
      if (ui[i] < j) left[i][j] = nowi[i];
      nowi[i] = (nowi[i] + up[i][j]) % mod;
      nowj[j] = (nowj[j] + left[i][j]) % mod;
    }
  }
  cout << (up[n - 1][m - 1] + left[n - 1][m - 1]) % mod;
  return 0;
}
