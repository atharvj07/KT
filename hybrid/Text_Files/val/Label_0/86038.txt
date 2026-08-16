#include<bits/stdc++.h>
#define INFTY 1<<20
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long int ll;
const int MOD=1000000007;

int main(){

int n;cin>>n;
ll a[n];
rep(i,n)cin>>a[i];
ll sum,ans=0,cnt;
rep(i,60){
    cnt=0;
    rep(j,n){
        if(a[j]>>i&1)cnt++;
    }
    sum= cnt*(n-cnt)%MOD;
    rep(j,i) sum = sum*2%MOD;
    ans += sum;
    ans %= MOD;
}

cout<<ans<<endl;
return 0;
}