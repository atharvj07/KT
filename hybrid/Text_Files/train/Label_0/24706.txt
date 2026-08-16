#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

constexpr ll MOD = 998244353;

ll power(ll x, ll n){
    x %= MOD;
    ll res = 1;
    while(n > 0){
        if(n&1){
            res *= x;
            res %= MOD;
        }
        x *= x;
        x %= MOD;
        n >>= 1;
    }
    return res;
}

ll mod_inv(ll x){
    return power(x, MOD-2);
}

vector<ll> factrial, inverse;

void init(ll n) {
    factrial.resize(n+1);
    inverse.resize(n+1);
    factrial[0] = 1;
    inverse[0] = 1;
    for (ll i = 1; i <= n; i++) {
        factrial[i] = (factrial[i - 1] * i) % MOD;
        inverse[i] = mod_inv(factrial[i]);
    }
}

ll nCk(ll n, ll k) {
    if(n < 0 || k < 0 || n < k) return 0;
    return factrial[n] * inverse[k] % MOD * inverse[n - k] % MOD;
}

ll nCk_big(ll n, ll k){
    if(k == 0) return 1;
    else return nCk_big(n, k-1) * ((n-k+1)%MOD) % MOD * mod_inv(k) % MOD;
}

// x種類の文字ですべての文字が少なくとも1回現れる長さnの文字列の数
ll calc(ll x, ll n){
    ll res = 0;
    for(int i=0;i<x;i++){
        res += power(x-i,n)*nCk(x,x-i)%MOD*(i%2?-1:1);
        res = (res%MOD+MOD)%MOD;
    }
    return res;
}

int main(){
    ll m, n, k, ans;
    cin >> m >> n >> k;
    init(k);
    ans = power(m,n);
    for(int i=1;i<k;i++){
        ans -= calc(i,n)*nCk_big(m,i)%MOD;
        ans = (ans%MOD+MOD)%MOD;
    }
    cout << ans << endl;
    return 0;
}
