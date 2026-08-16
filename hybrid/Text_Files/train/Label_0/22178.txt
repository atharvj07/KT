#include <bits/stdc++.h>
using namespace std;
int product(int n) {
  int anw = 1;
  while (n > 1) {
    if (n % 10 != 0) anw *= (n % 10);
    n /= 10;
  }
  return anw;
}
int g(int n) {
  while (n >= 10) n = product(n);
  return n;
}
int main() {
  int q;
  cin >> q;
  vector<int> mem((int)1e6 + 3);
  vector<vector<int>> dp(10, vector<int>((int)1e6 + 3));
  for (int i = 1; i < 1e6 + 3; i++) mem[i] = g(i);
  for (int i = 1; i < 10; i++) {
    dp[i][1] = 0;
    for (int j = 2; j < 1e6 + 3; j++) {
      dp[i][j] = dp[i][j - 1];
      if (mem[j - 1] == i) dp[i][j]++;
    }
  }
  int l, r, k;
  for (int i = 0; i < q; i++) {
    cin >> l >> r >> k;
    cout << dp[k][r + 1] - dp[k][l] << "\n";
  }
  return 0;
}
