#include <bits/stdc++.h>
using namespace std;
template <typename T>
ostream& operator<<(ostream& os, const vector<T>& v) {
  for (auto i : v) os << i << " ";
  return os;
}
template <typename T>
ostream& operator<<(ostream& os, const set<T>& v) {
  for (auto i : v) os << i << " ";
  return os;
}
const int M = 1e5 + 5;
const int N = 1000 + 80;
const int MOD = 998244353;
const int INF = 1e9 + 7;
int dp[N][N], Prev[N][N];
int a[N], l[N];
int n, k;
int mod(int x) {
  while (x < 0) x += MOD;
  while (x >= MOD) x -= MOD;
  return x;
}
void output() {
  printf("dp::\n");
  for (int i = 1; i <= k; ++i) {
    for (int j = 1; j <= n; ++j) printf("%d ", dp[i][j]);
    printf("\n");
  }
  printf("\nPrev::\n");
  for (int i = 1; i <= k; ++i) {
    for (int j = 1; j <= n; ++j) printf("%d ", Prev[i][j]);
    printf("\n");
  }
  printf("\n");
}
int main() {
  scanf("%d%d", &n, &k);
  a[0] = -INF;
  for (int i = 1; i <= n; ++i) scanf("%d", a + i);
  sort(a, a + n + 1);
  int max_a = a[n];
  int max_x = max_a / (k - 1);
  int ans = 0;
  for (int x = 1; x * (k - 1) < M; ++x) {
    for (int i = 0; i <= k; ++i)
      for (int j = 0; j <= n; ++j) dp[i][j] = 0;
    l[0] = 0;
    for (int i = 1; i <= n; ++i) {
      l[i] = l[i - 1];
      while (a[i] - a[l[i] + 1] >= x) ++l[i];
    }
    dp[0][0] = 1;
    for (int i = 0; i + 1 <= k; ++i) {
      Prev[i][0] = dp[i][0];
      for (int j = 1; j <= n; ++j)
        Prev[i][j] = (Prev[i][j - 1] + dp[i][j]) % MOD;
      for (int j = 1; j <= n; ++j) dp[i + 1][j] = Prev[i][l[j]];
    }
    int res = 0;
    for (int i = 1; i <= n; ++i) res = (res + dp[k][i]) % MOD;
    ans += res;
    ans %= MOD;
  }
  printf("%d\n", ans);
  return 0;
}
