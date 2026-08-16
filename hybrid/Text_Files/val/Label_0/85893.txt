#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int (i)=(0);(i)<(int)(n);++(i))
using ll = long long;
using P = pair< ll, ll >;

int dp[1<<26];
const int INF = 1e8;

int main() {
    string s;
    cin >> s;
    rep(i,(1<<26)) dp[i] = INF;
    dp[0] = 0;
    int stat = 0;
    rep(i, s.size()) {
        stat ^= 1 << (s[i] - 'a');
        rep(j, 26) {
            int tmp = (stat^(1<<j));
            dp[stat] = min(dp[stat], dp[tmp]+1);
            //cout << tmp << " ";
        }
        //cout << endl << stat << ", " << dp[stat] << endl;
    }
    cout << (dp[stat] ? dp[stat] : 1) << endl;
}
