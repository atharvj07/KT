#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < n; i++)
#define rep2(i, x, n) for(int i = x; i < n; i++)
#define elif else if
typedef long long ll;
typedef pair<ll, ll> P;
const ll MOD = 1e9+7;
const ll MOD2 = 998244353;
const ll INF = 1e18;

int main(){
    int N, K;
    cin >> N >> K;
    ll H[N+1];
    H[0] = 0;
    rep2(i, 1, N+1) cin >> H[i];
    ll cost[N+1][N+1];
    rep(i, N+1){
        fill_n(cost[i], N+1, INF);
    }
    cost[0][0] = 0;
    ll zero = 0;
    rep2(i, 1, N+1){
        rep2(j, 1, i+1){
            rep(k, i){
                cost[i][j] = min(cost[i][j], cost[k][j-1] + max(zero, H[i]-H[k]));
            }
        }
    }
    ll ans = INF;
    rep(i, N+1) ans = min(ans, cost[i][N-K]);
    cout << ans << endl;
}