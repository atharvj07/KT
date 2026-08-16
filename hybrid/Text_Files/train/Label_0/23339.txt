#include <bits/stdc++.h>
using namespace std;
#define int long long
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)

template <class T>
bool chmax(T &a, const T &b) {
    if (a < b) {
        a = b;
        return 1;
    }
    return 0;
}

signed main() {
    int n;
    cin >> n;
    vector<int> a(n);
    REP(i, n) cin >> a[i];
    sort(begin(a), end(a));

    vector<vector<int>> dp(n + 1, vector<int>(n + 1));
    REP(i, n) dp[i][n] = 1;
    REP(i, n) {
        for (int j = i + 1; j < n; ++j) {
            chmax(dp[j][i], dp[i][n] + 1);
        }
        REP(j, i + 1) {
            int d = a[i] - a[j];
            auto itr = lower_bound(begin(a), end(a), a[i] + d);
            if (itr == end(a) || *itr != a[i] + d) {
                continue;
            }
            int idx = itr - begin(a);
            chmax(dp[idx][i], dp[i][j] + 1);
        }
    }
    int ans = 0;
    REP(i, n) {
        REP(j, n) {
            chmax(ans, dp[i][j]);
        }
    }
    cout << ans << endl;
    return 0;
}

