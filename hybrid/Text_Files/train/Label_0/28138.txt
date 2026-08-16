#include<bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define Rep(i,sta,n) for(int i=sta;i<n;i++)

const int mod=1000000007;
int dp[70][70][6100];
void solve(){
    int n,k;cin>>n>>k;
    vector<int> ra(n+1);
    vector<int> rr(k+1);
    vector<int> rb(k+1);
    vector<int> a(n);
    vector<int> r(k),b(k);
    rep(i,n){
        cin>>a[i];
    }
    rep(i,k){
        cin>>r[i];
    }
    rep(i,k){
        cin>>b[i];
    }
    sort(a.begin(),a.end(),greater<int>());
    sort(r.begin(),r.end(),greater<int>());
    sort(b.begin(),b.end(),greater<int>());
    rep(i,n){
        ra[i+1]=ra[i]+a[i];
    }
    rep(i,k){
        rr[i+1]=rr[i]+r[i];
        rb[i+1]=rb[i]+b[i];
    }
    rep(i,n+1){
        rep(j,k+1){
            rep(l,6100){
                dp[i][j][l]=mod;
            }
        }
    }
    dp[0][0][3010]=0;
    rep(i,n){
        rep(j,k+1){
            int rest=i-j;
            if(rest<0||rest>k)continue;
            rep(l,6100){
                if(dp[i][j][l]==mod)continue;
                //take red
                if(j<k){
                    int dif=r[j]-a[i];
                    int cost=max(0,-dif);
                    dp[i+1][j+1][l+dif]=min(dp[i+1][j+1][l+dif],dp[i][j][l]+cost);
                }
                //take blue
                if(rest<k){
                    int dif=b[rest]-a[i];
                    int cost=max(0,-dif);
                    dp[i+1][j][l]=min(dp[i+1][j][l],dp[i][j][l]+cost);
                }
            }
        }
    }
    int ans=mod;
    rep(j,k+1){
        int rest=n-j;
        if(rest<0)continue;
        if(rest>k)continue;
        rep(l,6100){
            int x=l-3010;
            if(x+rr[k]-rr[j]<0)continue;
            int bb=rr[j]-x+rb[rest]-ra[n];
            if(bb+rb[k]-rb[rest]<0)continue;

            ans=min(ans,dp[n][j][l]);

        }
    }
    if(ans==mod)ans=-1;
    cout<<ans<<endl;

}
int main(){
    solve();
    return 0;
}
