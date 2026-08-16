#include <bits/stdc++.h>
using namespace std;
int n, m;
long long res, c[2005][2005];
int main() {
  cin >> n >> m;
  long long p, q, s;
  for (int i = 1; i <= n; i++) {
    p = 1, q = 0;
    for (int j = 2; j <= m; j++) {
      q = (q + c[i - 1][j]) % 1000000007;
      p = (p + q) % 1000000007;
      c[i][j] = p;
    }
  }
  res = 0;
  for (int i = 1; i < n; i++) {
    p = 1;
    q = 0;
    for (int j = 2; j <= m; j++) {
      s = m - j + 1;
      p = (p + q) % 1000000007;
      q = (q + c[n - i][j]) % 1000000007;
      res = (res + s * (c[i][j] * p % 1000000007)) % 1000000007;
      p = (p + c[n - i][j]) % 1000000007;
    }
  }
  for (int j = 2; j <= m; j++) {
    s = m - j + 1;
    res = (res + s * c[n][j]) % 1000000007;
  }
  cout << res;
}
