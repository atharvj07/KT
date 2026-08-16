#include<bits/stdc++.h>
using namespace std;

#define int long long

#define rep(i,n) for(int i=0;i<(n);i++)
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define fi first
#define se second
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;

template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

typedef bitset<300>bs;

const int mod=1000000007;
inline void add(int &a,int b){
    a+=b;
    if(a>=mod)a-=mod;
}
int mpow(int n,int m){
    int ret=1;
    while(m){
        if(m&1)ret=ret*n%mod;
        n=n*n%mod;
        m>>=1;
    }
    return ret;
}

int dp[333][333];

int po[333];
signed main(){
    po[0]=1;
    for(int i=1;i<333;i++)po[i]=po[i-1]*2%mod;
    int N;
    cin>>N;
    vector<bs>C(N);
    rep(i,N){
        rep(j,N){
            int c;cin>>c;C[i][j]=c;
        }
    }

    int r=0;
    rep(j,N){
        int k=-1;
        for(int i=r;i<N;i++)if(C[i][j]){
            k=i;
            break;
        }
        if(k==-1)continue;
        if(k!=r)swap(C[r],C[k]);
        for(int i=k+1;i<N;i++)if(C[i][j])C[i]^=C[r];
        r++;
    }



    int ans=0;
    for(int k=r;k<=N;k++){
        memset(dp,0,sizeof(dp));
        dp[0][0]=1;
        for(int i=0;i<N;i++){
            for(int j=0;j<=k;j++){
                add(dp[i+1][j],dp[i][j]*po[j]%mod);
                if(j+1<=k)add(dp[i+1][j+1],dp[i][j]*(po[k]-po[j]+mod)%mod);
            }
        }

        int tmp=1;
        for(int i=0;i<k-r;i++)tmp=tmp*(po[N-r-i]-1)%mod;
        for(int i=0;i<k-r;i++)tmp=tmp*mpow(po[k-r-i]-1,mod-2)%mod;
        tmp=tmp*dp[N][k]%mod;
        tmp=tmp*mpow(po[N-k],N)%mod;
        ans=(ans+tmp)%mod;
    }
    cout<<ans<<endl;
    return 0;
}
