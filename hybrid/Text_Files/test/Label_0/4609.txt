#include <bits/stdc++.h>
using namespace std;
const int N = 2e3 + 10;
const long long INF = 1e18;
const int B = 998244353;
long long p[N][N];
int main() {
  ios_base ::sync_with_stdio(0);
  cin.tie(0);
  for (int i = int(0); i <= int(N - 1); ++i) {
    p[i][0] = 1;
    for (int j = int(1); j <= int(i); ++j)
      p[i][j] = (p[i - 1][j - 1] + p[i - 1][j]) % B;
  }
  int n, m, k;
  cin >> n >> m >> k;
  long long ans = m;
  for (int i = int(1); i <= int(k); ++i) ans = ans * (m - 1) % B;
  ans = ans * p[n - 1][k] % B;
  cout << ans << "\n";
  return 0;
}
