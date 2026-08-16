#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL 
#include "e:/Codes/lib/prettyprint.hpp"
#else
#define debug(...) 
#endif

int32_t main() {
  ios::sync_with_stdio(0);
  cout.tie(0);
  cin.tie(0);

  int tc;
  cin >> tc;

  while (tc--) {
    int n, k;
    string s;

    cin >> n >> k >> s;
    vector<string> dp(n+1);
  
    auto c = [&](char c, int x) {
      return string () = ('a' + (c - 'a' + x + k) % k);
    };

    for (int i = 0; i < n; ++i) {
      if (dp[i+1].size() == 0) dp[i+1] = dp[i] + s[i];
      for (int j = -1; j <= 1; ++j) {
        dp[i+1] = min(dp[i+1], dp[i] + c(s[i], j));
      }
  
      if (i > 0) {
        string tmp = dp[i] + s[i];
        swap(tmp[i], tmp[i-1]);
        dp[i+1] = min(dp[i+1], tmp);
      }

      if (i+2 > n) continue;
      if (dp[i+2].size() == 0) dp[i+2] = dp[i] + s[i] + s[i+1]; 
      for (int j = -1; j <= 1; ++j) {
        dp[i+2] = min(dp[i+2], dp[i] + c(s[i+1], j) + s[i]);
      }
      if (i > 0 && i+1 < n) {
        string tmp = dp[i] + s[i+1];
        swap(tmp[i], tmp[i-1]);
        dp[i+2] = min(dp[i+2], tmp + s[i]);
      }
    }
  
    debug(dp);
    cout << dp[n] << '\n';
  }
}
