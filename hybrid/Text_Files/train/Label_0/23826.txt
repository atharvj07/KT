#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
using vi = vector<int>;
using vl = vector<ll>;

using _loop_int = int;
#define REP(i,n) for(_loop_int i=0; i<(_loop_int)(n); i++)
#define FOR(i,a,b) for(_loop_int i=(_loop_int)(a); i<(_loop_int)(b); i++)
#define FORR(i,a,b) for(_loop_int i=(_loop_int)(b)-1; i>=(_loop_int)(a); i--)

#define CHMIN(a,b) (a)=min((a),(b))
#define CHMAX(a,b) (a)=max((a),(b))
#define ALL(v) (v).begin(),(v).end()

#define DEBUG(x) cerr<<#x<<": "<<(x)<<endl
#define DEBUG_VEC(v) cerr<<#v<<": ";REP(__i,(v).size())cerr<<((v)[__i])<<", ";cerr<<endl

const ll MOD = 1000000007ll;

int n;
int k;
int a[25];

ll comb[1252][1252];
ll dp[25][1252];    // dp[i][j] := i日見た 残りj人

ll modpow(ll a, ll b){
    ll r = 1;
    while(b){
        if(b&1)r=r*a%MOD;
        a=a*a%MOD;
        b>>=1;
    }
    return r;
}
ll modinv(ll a){
    return modpow(a, MOD-2);
}
ll invcombn[1252];

int main(){
    scanf("%d%d",&n,&k);
    REP(i,k)scanf("%d",a+i);

    REP(i,1252)REP(j,1252){
        if(j==0 || j==i){
            comb[i][j] = 1;
        }else if(j>i){
            comb[i][j] = 0;
        }else{
            comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % MOD;
        }
    }
    // REP(i,10){
    //     REP(j,10)printf("%lld ",comb[i][j]);puts("");
    // }
    REP(i,1252)invcombn[i] = modinv(comb[n][i]);

    dp[0][n] = 1;
    REP(i,k){
        REP(j,n+1)if(dp[i][j]){
            REP(y,min(j,a[i])+1){
                ll add = dp[i][j];
                add = add * comb[j][y] % MOD;
                add = add * comb[n-y][a[i]-y] % MOD;
                add = add * invcombn[a[i]] % MOD;

                (dp[i+1][j-y] += add) %= MOD;
            }
        }
    }
    // REP(i,k+1){
    //     REP(j,n+1)printf("%lld ",dp[i][j]); puts("");
    // }

    ll ans = dp[k][0];
    REP(i,k)ans = ans * comb[n][a[i]] % MOD;
    printf("%lld\n",ans);
    return 0;
}
