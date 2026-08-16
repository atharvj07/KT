#include <bits/stdc++.h>

using namespace std;

#define sz(a) int((a).size())
#define forn(i, n) for (int i = 0; i < int(n); ++i)

const int N = 250;
const int M = 28;
const int INF = 1e9;

int dp[2][M * 2 + 1][N][N];

int main() {
  string s;
  cin >> s;
  reverse(s.begin(), s.end());
  s += "0";
  
  forn(carry, M * 2 + 1) forn(cp, N) forn(cn, N) dp[0][carry][cp][cn] = INF;
  dp[0][M][N - 1][N - 1] = 0;
  
  forn(i, sz(s)) {
    forn(carry, M * 2 + 1) forn(cp, N) forn(cn, N) dp[1][carry][cp][cn] = INF;
    forn(carry, M * 2 + 1) for (int cp = N - 1; cp >= 0; --cp) for (int cn = N - 1; cn >= 0; --cn) if (dp[0][carry][cp][cn] != INF) {
      if (cp > 0) dp[0][carry][cp - 1][cn] = min(dp[0][carry][cp - 1][cn], dp[0][carry][cp][cn]);
      if (cn > 0) dp[0][carry][cp][cn - 1] = min(dp[0][carry][cp][cn - 1], dp[0][carry][cp][cn]);
      int rcarry = carry - M;
      int val = rcarry + cp - cn;
      int digit = val % 10;
      if (digit < 0) digit += 10;
      int ncarry = val / 10;
      if (val < 0 && digit != 0) --ncarry;
      if (digit == s[i] - '0') dp[1][ncarry + M][cp][cn] = min(dp[1][ncarry + M][cp][cn], dp[0][carry][cp][cn] + cp + cn);
    }
    swap(dp[0], dp[1]);
  }
  
  int ans = INF;
  forn(i, N) forn(j, N) ans = min(ans, dp[0][M][i][j]);
  cout << ans << endl;
}