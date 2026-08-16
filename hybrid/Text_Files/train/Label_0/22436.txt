#include <bits/stdc++.h>
using namespace std;
void init_code() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  ;
}
void solve() {
  long long n;
  cin >> (n);
  vector<long long> b(n + 1), dp(n + 1);
  for (long long(i) = (1); (i) <= (n); (i) += 1) cin >> (b[i]);
  if (n <= 2) {
    cout << (0) << "\n";
    return;
  }
  long long minC = INT_MAX;
  for (long long(d1) = (-1); (d1) <= (1); (d1) += 1) {
    for (long long(d2) = (-1); (d2) <= (1); (d2) += 1) {
      dp[1] = b[1] + d1;
      dp[2] = b[2] + d2;
      long long d = dp[2] - dp[1];
      bool f = false;
      long long tmp = abs(d1) + abs(d2);
      for (long long(i) = (3); (i) <= (n); (i) += 1) {
        dp[i] = dp[i - 1] + d;
        if (abs(dp[i] - b[i]) > 1) {
          f = true;
          break;
        }
        if (dp[i] != b[i]) tmp++;
      }
      if (!f) minC = min(minC, tmp);
    }
  }
  (minC == INT_MAX) ? cout << (-1) << "\n" : cout << (minC) << "\n";
}
int main() {
  init_code();
  solve();
  return 0;
}
