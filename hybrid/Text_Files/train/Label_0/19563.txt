#include<bits/stdc++.h>
using namespace std;
using Int = long long;
template<typename T1,typename T2> inline void chmin(T1 &a,T2 b){if(a>b) a=b;}
template<typename T1,typename T2> inline void chmax(T1 &a,T2 b){if(a<b) a=b;}

struct FastIO{
  FastIO(){
    cin.tie(0);
    ios::sync_with_stdio(0);
  }
}fastio_beet;

using P = pair<int, int>;
vector< vector<int> > bfs(vector<string> &s,vector<P> &vp,char wall,int dir){
  int h=s.size(),w=s.front().size();
  vector< vector<int> > dp(h,vector<int>(w,-1));
  deque<P> q;

  for(int i=0;i<(int)vp.size();i++){
    int sy=vp[i].first,sx=vp[i].second;
    dp[sy][sx]=0;
    q.emplace_back(sy,sx);
  }

  int dy[]={1,-1,0,0,1,1,-1,-1};
  int dx[]={0,0,1,-1,1,-1,1,-1};
  auto in=[&](int y,int x){return 0<=y&&y<h&&0<=x&&x<w;};

  while(!q.empty()){
    int y,x;
    tie(y,x)=q.front();q.pop_front();
    for(int k=0;k<dir;k++){
      int ny=y+dy[k],nx=x+dx[k];
      if(!in(ny,nx)) continue;
      int nd=dp[y][x]+(s[ny][nx]==wall);
      if(~dp[ny][nx]&&dp[ny][nx]<=nd) continue;
      dp[ny][nx]=nd;
      if(s[ny][nx]=='#'){
        q.emplace_back(ny,nx);
      }else{
        q.emplace_front(ny,nx);
      }
    }
  }
  return dp;
}

vector< vector<int> > bfs(vector<string> &s,int sy,int sx,char wall,int dir){
  vector<P> vp;
  vp.emplace_back(sy,sx);
  return bfs(s,vp,wall,dir);
}


//INSERT ABOVE HERE

signed main(){
  int h,w;
  cin>>h>>w;
  vector<string> st(h);
  for(int i=0;i<h;i++) cin>>st[i];

  auto d1=bfs(st,0,0,'#',4);
  int ans=d1[h-1][w-1];

  // find B2
  vector< vector<int> > ex(h,vector<int>(w));
  {
    int flg=0;
    for(int i=0;i<h;i++){
      for(int j=0;j<w;j++) if(st[i][j]=='B') ex[i][j]|=flg;
      for(int j=0;j<w;j++) if(st[i][j]=='B') flg=1;
    }
  }
  {
    int flg=0;
    for(int j=0;j<w;j++){
      for(int i=0;i<h;i++) if(st[i][j]=='B') ex[i][j]|=flg;
      for(int i=0;i<h;i++) if(st[i][j]=='B') flg=1;
    }
  }

  // use B2
  for(int i=0;i<h;i++)
    for(int j=0;j<w;j++)
      if(ex[i][j]) chmin(ans,d1[i][j]);

  // find B1
  int by=-1,bx=-1;
  for(int i=0;i<h;i++)
    for(int j=0;j<w;j++)
      if(st[i][j]=='B'&&!ex[i][j]) by=i,bx=j;

  if(~by){
    // dist from B1
    auto d2=bfs(st,by,bx,'#',4);

    // dist to (i, j) with B1
    vector< vector<int> > d3(h,vector<int>(w));
    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++)
        d3[i][j]=d1[i][j]+d2[i][j]-(st[i][j]=='#');

    vector< queue<P> > qs((h+w)*2);
    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++)
        qs[d3[i][j]].emplace(i,j);

    int dy[]={1,-1,0,0,1,1,-1,-1};
    int dx[]={0,0,1,-1,1,-1,1,-1};
    auto in=[&](int y,int x){return 0<=y&&y<h&&0<=x&&x<w;};
    for(int d=0;d+1<(int)qs.size();d++){
      while(!qs[d].empty()){
        int y,x;
        tie(y,x)=qs[d].front();qs[d].pop();
        if(d3[y][x]!=d) continue;
        for(int k=0;k<4;k++){
          int ny=y+dy[k],nx=x+dx[k];
          if(!in(ny,nx)) continue;
          int nd=d3[y][x]+(st[ny][nx]=='#');
          if(d3[ny][nx]<=nd) continue;
          d3[ny][nx]=nd;
          qs[nd].emplace(ny,nx);
        }
      }
    }

    // dist from B2 and goal
    vector<P> vp;
    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++)
        if(ex[i][j]) vp.emplace_back(i,j);
    vp.emplace_back(h-1,w-1);
    auto d4=bfs(st,vp,'#',4);

    // use B1
    vector< vector<int> > d5(d3),d6(d3);
    for(int i=0;i<h;i++){
      for(int j=0;j<w;j++){
        if(i) chmin(d5[i][j],d5[i-1][j]);
        if(j) chmin(d6[i][j],d6[i][j-1]);
      }
    }

    // take B2 and use
    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++)
        chmin(ans,(d4[i][j]-(st[i][j]=='#'))+min(d5[i][j],d6[i][j]));
  }

  cout<<ans<<endl;
  return 0;
}

