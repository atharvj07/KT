#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int MOD = 998244353;

ll power(ll x, ll n) {
    x %= MOD;
    //n %= MOD-1;
    int64_t ans = 1;
    while (n > 0) {
        if ((n & 1LL) == 1LL) {
            ans = ans * x % MOD;
        }
        x = x * x % MOD;  //一周する度にx, x^2, x^4, x^8となる
        n >>= 1;          //桁をずらす n = n >> 1
    }
    return ans;
}

ll mod_inv(ll x){
    return power(x, MOD-2);
}


ll factrial[100005], inverse[100005];  //階乗と逆元を保持

void init(ll n) {
    factrial[0] = 1;
    inverse[0] = 1;
    for (ll i = 1; i <= n; i++) {
        factrial[i] = (factrial[i - 1] * i) % MOD;  //階乗を求める
        inverse[i] = power(factrial[i], MOD - 2) % MOD;  //オイラーの定理で逆元を求める
    }
}

ll nCk(ll n, ll k) {
    if(n < 0 || k < 0 || n < k) return 0;
    return factrial[n] * inverse[k] % MOD * inverse[n - k] % MOD;
}


vector<ll> conb;

ll nCkbig(ll n, ll k) {
    if(conb[k] >= 0) return conb[k];
    if (k == 0)
        return 1;
    else
        return conb[k] = nCkbig(n, k - 1) * ((n - k + 1 + MOD)%MOD) % MOD * mod_inv(k) % MOD;
}

ll N, M, K;

ll calc(ll x){
    ll res = 0;
    for(ll i=0;i<x;i++){
        res += power(x-i,N)*nCk(x, x-i)%MOD * (i%2 ? -1 : 1) % MOD;
        res %= MOD;
    }
    return res;
}

int main(){
    cin >> M >> N >> K;
    conb.resize(K+1, -1);
    conb[0] = 1;
    if(M < K){
        cout << 0 << endl;
        return 0;
    }
    init(100001);
    ll ans = power(M,N);
    M %= MOD;
    for(int i=1;i<K;i++){
        ans -= calc(i)*nCkbig(M,i)%MOD;
        ans = (ans%MOD+MOD)%MOD;
    }
    cout << ans << endl;
    return 0;
}

