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

#define INF INT_MAX/3
#define mod 1000000007

int H,W,K;
int s,t,Tm,Tc;
string b[50];
int rm[12];
int cost[50][50][50][50];
int di[]={0,-1,0,+1};
int dj[]={+1,0,-1,0};
vector<int> is[12],js[12];
int unit[12][12][12];
int totunit[1<<12];

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cin>>H>>W>>K;
  cin>>s>>t>>Tm>>Tc;
  s--;t--;
  rep(i,H)cin>>b[i];

  rep(si,H)rep(sj,W){
    queue<P> que;
    rep(i,H)rep(j,W)cost[si][sj][i][j]=INF;
    que.push(P(si,sj)); cost[si][sj][si][sj]=0;
    while(que.size()){
      P p=que.front(); que.pop();
      rep(dir,4){
        int ni=p.fi+di[dir],nj=p.se+dj[dir];
        if(ni<0||ni>=H||nj<0||nj>=W||b[ni][nj]=='.'||cost[si][sj][ni][nj]!=INF)continue;
        cost[si][sj][ni][nj]=cost[si][sj][p.fi][p.se]+Tm;
        que.push(P(ni,nj));
      }
    }
  }

  rep(c,12){
    int counter=0;
    rep(i,H)rep(j,W){
      if(b[i][j]=='A'+c){
        int cnt=0;
        rep(dir,4){
          int ni=i+di[dir],nj=j+dj[dir];
          if(ni<0||ni>=H||nj<0||nj>=W||b[ni][nj]=='.')continue;
          cnt++;
        }
        if(cnt==1){
          is[c].push_back(i); js[c].push_back(j);
          counter++;
        }
      }
    }
    rm[c]=counter;
  }
  rep(c,12){
    if(rm[c]==0)continue;
    vector<vector<vector<int> > > dp(1<<rm[c],vector<vector<int> >(rm[c],vector<int>(rm[c],INF)));
    rep(r,rm[c])dp[1<<r][r][r]=Tc;
    rep(S,1<<rm[c]){
      rep(i,rm[c])rep(st,rm[c]){
        if(dp[S][st][i]==INF)continue;
        rep(j,rm[c]){
          if((S>>j)&1)continue;
          int mv=cost[is[c][i]][js[c][i]][is[c][j]][js[c][j]];
          minch(dp[S|1<<j][st][j],dp[S][st][i]+mv+Tc);
        }
      }
    }
    rep(i,rm[c])rep(j,rm[c]){
      unit[c][i][j]=dp[(1<<rm[c])-1][i][j];
    }
  }

  int mask=0;
  rep(i,12)if(rm[i]==0)mask|=1<<i;

  {
    vector<vector<vector<int> > > dp(1<<12,vector<vector<int> >(12,vector<int>(12,INF)));
    rep(i,12){
      if(rm[i]==0)continue;
      rep(j,rm[i])rep(k,rm[i]){
        if(unit[i][j][k]==INF)continue;
        int mvj=cost[s][t][is[i][j]][js[i][j]];
        minch(dp[(1<<i)][i][k],mvj+unit[i][j][k]);
     
      }
    }
    rep(S,1<<12){
      totunit[S]=INF;
    }
    totunit[0]=0;
    rep(S,1<<12)rep(i,12){
      if(rm[i]==0)continue;
      rep(j,rm[i]){
        if(dp[S][i][j]==INF)continue;
        int mvs=cost[is[i][j]][js[i][j]][s][t];
        minch(totunit[S],dp[S][i][j]+mvs);
        rep(k,12){
          if((S>>k)&1)continue;
          rep(l,rm[k])rep(m,rm[k]){
            if(unit[k][l][m]==INF)continue;
            int mvl=cost[is[i][j]][js[i][j]][is[k][l]][js[k][l]];
            minch(dp[S|(1<<k)][k][m],dp[S][i][j]+mvl+unit[k][l][m]);
          }
        }
      }
    }
  }

  vector<vector<int> > dp(K+1,vector<int>(1<<12,INF));
  dp[0][((1<<12)-1)^mask]=0;
  rep(i,K){
    rep(S,1<<12){
      if(dp[i][S]==INF)continue;
      for(int T=S;T>=0;T--){
        T&=S;
        minch(dp[i+1][T],max(dp[i][S],totunit[S^T]));
      }
    }
  }
  cout<<dp[K][0]<<endl;

  return 0;
}

