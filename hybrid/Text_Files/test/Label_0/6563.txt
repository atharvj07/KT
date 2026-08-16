#include <bits/stdc++.h>
using namespace std;
#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);++i)
#define rep(i,n) REP(i, 0, n)

int dp[1001];
int main() {
    int W, N; int T = 0;
    while(~scanf("%d%d", &W, &N) && W) {
        memset(dp, 0, sizeof(dp));
        rep(i, N) {
            int v, w; scanf("%d,%d", &v, &w);
            for(int j = W; j - w >= 0; --j)
              dp[j] = max(dp[j], dp[j - w] + v);
        }
        pair<int, int> ans(0, 0);
        rep(i, W + 1) ans = max(ans, make_pair(dp[i], -i));
        printf("Case %d:\n%d\n%d\n", ++T, ans.first, -ans.second);
    }
    return 0;
}