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

const int INF=1001001001001001001ll;

int par[20][111111];
int A[111111];

int N;
vint G[111111];

int dep[111111];
int latte[111111];
int dp[20][111111];
vint lis[111111];
void dfs(int v,int p,int d){
    dep[v]=d;
    par[0][v]=p;
    latte[v]=A[v];
    lis[v].pb(0);
    lis[v].pb(0);
    for(auto u:G[v]){
        if(u==p)continue;
        dfs(u,v,d+1);
        latte[v]+=latte[u];
        lis[v].pb(latte[u]);
    }
}

int lca(int a,int b){
    if(dep[a]<dep[b])swap(a,b);
    rep(i,20)if((dep[a]-dep[b])>>i&1)a=par[i][a];
    if(a==b)return a;
    for(int i=19;i>=0;i--)if(par[i][a]!=par[i][b])a=par[i][a],b=par[i][b];
    return par[0][a];
}

signed main(){
    cin>>N;
    rep(i,N)cin>>A[i];
    rep(i,N-1){
        int a,b;
        cin>>a>>b;
        a--;b--;
        G[a].pb(b);G[b].pb(a);
    }

    dfs(0,-1,0);

    rep(i,N){
        sort(all(lis[i]));
        reverse(all(lis[i]));
    }
    for(int i=1;i<N;i++){
        int p=par[0][i];
        if(lis[p][0]==latte[i]){
            dp[0][i]=lis[p][1];
        }
        else{
            dp[0][i]=lis[p][0];
        }
    }


    rep(i,19){
        rep(j,N){
            if(par[i][j]==-1){
                par[i+1][j]=-1;
                dp[i+1][j]=dp[i][j];
            }
            else{
                par[i+1][j]=par[i][par[i][j]];
                dp[i+1][j]=max(dp[i][par[i][j]],dp[i][j]);
            }
        }
    }


    int sumall=accumulate(A,A+N,0ll);


    int Q;cin>>Q;
    while(Q--){
        int a,b;
        cin>>a>>b;a--;b--;
        int p=lca(a,b);
        int ans=0;
        rep(lattemalta,2){
            swap(a,b);
            int x=a;
            if(a==p)continue;
            chmax(ans,lis[a][0]);
            int d=dep[x]-dep[p]-1;
            rep(i,20){
                if(d>>i&1){
                    chmax(ans,dp[i][x]);
                    x=par[i][x];
                }
            }
            a=x;



        }

        {
            bool flaga=false,flagb=false;
            for(auto x:lis[p]){
                if(!flaga&&x==latte[a]){
                    flaga=true;
                    continue;
                }
                if(!flagb&&x==latte[b]){
                    flagb=true;
                    continue;
                }
                chmax(ans,x);
                break;
            }
        }
        chmax(ans,sumall-latte[p]);
        cout<<ans<<endl;
    }
    return 0;
}

