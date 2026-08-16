#include <bits/stdc++.h>
using namespace std;
const int mod = 998244353;
int n, k;
long long f[2010][2010][5];
int main() {
  cin >> n >> k;
  f[1][2][0] = 1;
  f[1][1][1] = 1;
  f[1][1][2] = 1;
  f[1][2][3] = 1;
  for (int i = 2; i <= n; i++) {
    for (int j = 0; j <= k; j++) {
      f[i][j][0] = (f[i - 1][j][0] + f[i - 1][j - 1][1] + f[i - 1][j - 1][2] +
                    f[i - 1][j - 2][3]) %
                   mod;
      f[i][j][1] = (f[i - 1][j][0] + f[i - 1][j][1] + f[i - 1][j - 1][2] +
                    f[i - 1][j][3]) %
                   mod;
      f[i][j][2] = (f[i - 1][j][0] + f[i - 1][j - 1][1] + f[i - 1][j][2] +
                    f[i - 1][j][3]) %
                   mod;
      f[i][j][3] = (f[i - 1][j - 2][0] + f[i - 1][j - 1][1] +
                    f[i - 1][j - 1][2] + f[i - 1][j][3]) %
                   mod;
    }
  }
  long long ans = (f[n][k][0] + f[n][k][1] + f[n][k][2] + f[n][k][3]) % mod;
  cout << ans << endl;
}
