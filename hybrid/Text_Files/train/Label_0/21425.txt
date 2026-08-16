#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const long long int LINF = 0x3f3f3f3f3f3f3f3fll;
const long double pi = acos(-1);
const int MOD = 1e9 + 7;
long long int dp[20][2][4];
string second;
int n;
int solve(int i, bool menor, int qnt, bool cu) {
  if (qnt == 4) return 0;
  if (i == n) {
    if (cu)
      return menor;
    else
      return 1;
  }
  if (dp[i][menor][qnt] != -1) return dp[i][menor][qnt];
  int ini = 0, fim = 9;
  if (!menor) fim = second[i] - '0';
  long long int &memo = dp[i][menor][qnt];
  memo = 0;
  for (int k = ini; k <= fim; k++) {
    memo += solve(i + 1, menor | (k < fim), qnt + (k != 0), cu);
  }
  return memo;
}
int main() {
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  while (t--) {
    cin >> second;
    n = second.size();
    memset(dp, -1, sizeof(dp));
    long long int m = solve(0, false, 0, true);
    cin >> second;
    n = second.size();
    memset(dp, -1, sizeof(dp));
    long long int M = solve(0, false, 0, false);
    cout << M - m << endl;
  }
  return 0;
}
