#include <bits/stdc++.h>
using namespace std;
const int N = 505;
long long dp[N][N];
int mod, n, m, sum[N];
long long C(int a) { return (long long)a * (a - 1) / 2; }
long long dfs(int a, int b) {
  if (a < 0 || b < 0) return 0;
  if (a == 0 && b == 0) return 1;
  if (~dp[a][b]) return dp[a][b];
  dp[a][b] = 0;
  dp[a][b] += C(a) * dfs(a - 2, b) % mod;
  dp[a][b] += C(b) * dfs(a + 2, b - 2) % mod;
  dp[a][b] += a * b * dfs(a, b - 1) % mod;
  dp[a][b] %= mod;
  return dp[a][b];
}
int main() {
  char s[N];
  memset(dp, -1, sizeof dp);
  while (cin >> n >> m >> mod) {
    memset(sum, 0, sizeof sum);
    for (int i = 0; i < m; i++) {
      scanf("%s", s);
      for (int j = 0; j < n; j++) sum[j] += s[j] - '0';
    }
    int a = 0, b = 0;
    for (int i = 0; i < n; i++)
      if (sum[i] == 1)
        a++;
      else if (sum[i] == 0)
        b++;
    cout << dfs(a, b) << endl;
  }
  return 0;
}
