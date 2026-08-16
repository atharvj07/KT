#include <bits/stdc++.h>
using namespace std;
long long n, k, a[110], b[110], dp[110][101000][2];
long long Rec(int i, int sum, bool take) {
  if (i == n) return (sum == 1e4 && take ? 0 : -1e9);
  if (dp[i][sum][take] != -1) return dp[i][sum][take];
  long long Res = -1e9;
  Res = max(Res, a[i] + Rec(i + 1, (sum + a[i]) - b[i] * k, 1));
  Res = max(Res, Rec(i + 1, sum, take));
  return dp[i][sum][take] = Res;
}
int main() {
  memset(dp, -1, sizeof(dp));
  cin >> n >> k;
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < n; i++) cin >> b[i];
  cout << (Rec(0, 1e4, 0) < 0 ? -1 : Rec(0, 1e4, 0));
  return 0;
}
