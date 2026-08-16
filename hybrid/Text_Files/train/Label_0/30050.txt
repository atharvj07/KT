#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> P;

#define fi first
#define se second
#define repl(i,a,b) for(ll i=(ll)(a);i<(ll)(b);i++)
#define rep(i,n) repl(i,0,n)
#define all(x) (x).begin(),(x).end()
#define dbg(x) cout<<#x"="<<x<<endl
#define mmax(x,y) (x>y?x:y)
#define mmin(x,y) (x<y?x:y)
#define maxch(x,y) x=mmax(x,y)
#define minch(x,y) x=mmin(x,y)
#define uni(x) x.erase(unique(all(x)),x.end())
#define exist(x,y) (find(all(x),y)!=x.end())
#define bcnt __builtin_popcount

#define INF 1e16
#define mod 1000000007

ll N;
ll g[500010][2];
ll dp[500010][2];
ll lcnt[500010];

void predfs(ll v){
  if(v==N-1)return ;
  rep(i,2){
    predfs(g[v][i]);
    lcnt[v]+=lcnt[g[v][i]];
  }
}

void dfs(ll v,ll dep){
  if(v==N-1)return ;
  rep(i,2)dfs(g[v][i],dep+1);

  ll l=g[v][0],r=g[v][1];
  dp[v][0]=dp[l][0]+dp[r][0]+lcnt[v];
  minch(dp[v][1],dp[v][0]);
  minch(dp[v][1],dp[l][0]+lcnt[l]+dp[r][1]+1);
  minch(dp[v][1],dp[l][1]+1+dp[r][0]+lcnt[r]);
  minch(dp[v][1],dp[l][1]+1+dp[r][1]+1+dep);
}

int main(){
  cin>>N;
  memset(g,-1,sizeof(g));
  rep(i,N-1){
    ll a,b;
    cin>>a>>b;
    a--;b--;
    g[i][0]=a;
    g[i][1]=b;
  }
  rep(i,N)rep(j,2)dp[i][j]=INF;
  lcnt[N-1]=1;
  predfs(0);
  dp[N-1][0]=dp[N-1][1]=0;
  dfs(0,0);
  cout<<dp[0][1]<<endl;
  return 0;
}

