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

struct state{
  int i,j;
  int dist;
  int predir,crtdir;
};

int n,q;
int sx,sy;
bool road[4][55][55];
bool vis[55][55][11][4][4];
int dirtable[0x100];
vector<state> restst;
int di[]={0,+1,0,-1};
int dj[]={+1,0,-1,0};

int main(){
  dirtable['E']=0; dirtable['N']=1; dirtable['W']=2; dirtable['S']=3;
  cin>>n>>sx>>sy>>q;
  rep(i,n){
    int x1,y1,x2,y2;
    cin>>x1>>y1>>x2>>y2;
    if(x1==x2){
      for(int i=min(y1,y2);i<max(y1,y2);i++)road[1][i][x1]=road[3][i+1][x1]=true;
    }else{
      for(int i=min(x1,x2);i<max(x1,x2);i++)road[0][y1][i]=road[2][y1][i+1]=true;
    }
  }

  rep(nxtdir,4){
    //if(crtdir==(nxtdir+2)%4)continue;
    if(road[nxtdir][sy][sx]){
      restst.push_back((state){sy,sx,0,0,(int)nxtdir});
    }
  }

  rep(i,q){
    int d;
    char c;
    cin>>d>>c;

    memset(vis,0,sizeof(vis));
    queue<state> que;
    for(state s : restst){
      vis[s.i][s.j][0][s.predir][s.crtdir]=true;
      que.push((state){s.i,s.j,0,s.predir,s.crtdir});
    }
    restst.clear();
    while(que.size()){
      state s=que.front(); que.pop();
      if(s.dist==d){
        if(s.crtdir==dirtable[c]||s.predir==dirtable[c]){
          restst.push_back(s);
        }
        continue;
      }
      int ni=s.i+di[s.crtdir],nj=s.j+dj[s.crtdir];
      rep(nxtdir,4){
        if(nxtdir==(s.crtdir+2)%4)continue;
        if(road[nxtdir][ni][nj]){
          if(!vis[ni][nj][s.dist+1][s.crtdir][nxtdir]){
            vis[ni][nj][s.dist+1][s.crtdir][nxtdir]=true;
            que.push((state){ni,nj,s.dist+1,s.crtdir,(int)nxtdir});
          }
        }
      }
    }
  }
  vector<P> res;
  for(state s : restst)res.push_back(P(s.j,s.i));
  sort(all(res));
  uni(res);
  rep(i,res.size()){
    cout<<res[i].fi<<" "<<res[i].se<<endl;
  }
  return 0;
}

