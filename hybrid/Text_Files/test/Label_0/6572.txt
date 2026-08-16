#include <bits/stdc++.h>
using namespace std;
bool was[2010];
long long n, ans, minEdge = 1e9;
long long toPer[2010], a[2010][2010];
signed main() {
  ios_base::sync_with_stdio(0);
  cout.tie(0);
  cin.tie(0);
  cin >> n;
  for (long long i = 1; i <= n; ++i) {
    for (long long j = 1; j <= n - i; ++j) {
      cin >> a[i][j + i];
      a[i + j][i] = a[i][i + j];
      minEdge = min(minEdge, a[i][i + j]);
    }
  }
  for (long long i = 1; i <= n; ++i) {
    for (long long j = 1; j <= n; ++j) {
      if (i != j) {
        a[i][j] -= minEdge;
      }
    }
  }
  for (long long i = 1; i <= n; ++i) {
    toPer[i] = 2e9;
    for (long long j = 1; j <= n; ++j) {
      if (i != j) {
        toPer[i] = min(toPer[i], 2 * a[i][j]);
      }
    }
  }
  for (long long i = 1; i <= n; ++i) {
    long long tmpMin = 2e9, cur;
    for (long long j = 1; j <= n; ++j) {
      if (!was[j] and tmpMin > toPer[j]) {
        tmpMin = toPer[j];
        cur = j;
      }
    }
    was[cur] = 1;
    for (long long j = 1; j <= n; ++j) {
      toPer[j] = min(toPer[cur] + a[cur][j], toPer[j]);
    }
  }
  for (long long i = 1; i <= n; ++i) {
    cout << toPer[i] + (n - 1) * minEdge << '\n';
  }
}
