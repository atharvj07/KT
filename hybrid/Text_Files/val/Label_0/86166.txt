#include <stdio.h>

#define rep(i, n) for(int i = 0; i < n; i++)

using ll = long long;

const ll mod = 1000000007;

ll dp[256][111];
ll dpw[256][111];

int main() {
  int n, k;
  scanf("%d%d", &n, &k);
  rep(i, 256) {
    rep(j, 111) {
      dp[i][j] = 0;
    }
  }
  dp[0][0] = 1;
  rep(ww, n) {
    rep(i, 256) {
      rep(j, 111) {
        dpw[i][j] = dp[i][j];
      }
    }
    int w;
    scanf("%d", &w);
    rep(i, 256) {
      rep(j, 110) {
        dpw[i ^ w][j + 1] += dp[i][j];
      }
    }
    rep(i, 256) {
      rep(j, 111) {
        dp[i][j] = dpw[i][j] % mod;
      }
    }
  }
  ll all = 0;
  ll now = 1;
  for(int i = 1; i < 111; i++) {
    now = (now * i) % mod;
    all = (all + dp[k][i] * now) % mod;
  }
  printf("%lld\n", all);
}
