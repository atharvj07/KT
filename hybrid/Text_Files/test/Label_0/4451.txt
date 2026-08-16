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
#define bcnt __builtin_popcountll

#define INF 1e16

ll N,K,mod;
ll dp[2][101][(1<<10)];

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin>>N>>K>>mod;
  ll T=(1<<K);
  ll crt=0,nxt=1;
  dp[crt][0][0]=1;
  rep(i,2*N){
    rep(j,N+1)rep(S,T)dp[nxt][j][S]=0;
    rep(j,N+1){
      rep(S,T){
        if(dp[crt][j][S]==0)continue;
        ll k=i-j;
        if(j-k<0||bcnt(S)<j-k)continue;

        vector<ll> us,ls;
        if(j==0)us.push_back(INF);
        if(k==0)ls.push_back(INF);
        repl(v,max(0LL,i-K),i){
          if((S>>(i-v-1))&1LL) us.push_back(v);
          else ls.push_back(v);
        }

        if(us.size()>0&&i-us.back()<=K&&j<N){
          (dp[nxt][j+1][((S<<1LL)&(T-1))|1LL]+=dp[crt][j][S])%=mod;
        }
        if(ls.size()>0&&i-ls.back()<=K&&j>k&&i-us[us.size()-(j-k)]<=K&&k<N){
          (dp[nxt][j][(S<<1LL)&(T-1)]+=dp[crt][j][S])%=mod;
        }
      }
    }
    swap(crt,nxt);
  }

  ll res=0;
  rep(S,T)(res+=dp[crt][N][S])%=mod;
  cout<<res<<endl;

  return 0;
}

