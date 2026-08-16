#include<bits/stdc++.h>
using namespace std;

/*
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
*/

/*
unordered_map<int,int>mp;
mp.reserve(1024);
mp.max_load_factor(0.25);
*/

typedef long long ll;

ll pow(ll a,ll b,ll M){
    if(b==0){
        return 1;
    }

    ll t=pow(a,b/2,M);
    t = (t*t)%M;
    if(b%2==1){
        t= (t*a)%M;
    }

    return t;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll n,M;
    cin>>n>>M;

    vector<vector<ll>> ncr(n+1,vector<ll>(n+1));
    for(int i=1;i<=n;i++){
        ncr[i][0]=1;
        for(int j=1;j<i;j++){
            ncr[i][j] = (ncr[i-1][j]+ncr[i-1][j-1])%M;
        }
        ncr[i][i]=1;
    }
    vector<ll> pow(n+1);
    pow[0]=1;
    for(int i=1;i<=n;i++){
        pow[i]=(pow[i-1]*2)%M;
    }

    vector<vector<ll>> dp(n+2,vector<ll>(n+2));
    dp[0][0]=1;
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            for(int k=1;i+k<=n;k++){
                dp[i+k+1][j+k]+= ((dp[i][j]*ncr[j+k][j])%M)*pow[k-1];
                dp[i+k+1][j+k] = dp[i+k+1][j+k]%M;
            }
        }
    }

    ll ans=0;
    for(int i=0;i<=n;i++){
        ans= (ans+dp[n+1][i])%M;
    }

    cout<<ans<<"\n";

    return 0;
}
//6 100000007
