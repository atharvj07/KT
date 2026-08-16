#include<iostream>
#include<map>
#include<cassert>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)
typedef long long ll;
typedef pair<int,int> pii;
const int N = 500;
char m[N][N+1];
int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};

bool cango(int r,int c,int y,int x,int ty,int tx){
  rep(i,4){
    int ddx=x+dx[i],ddy=y+dy[i];
    while(ddy != -1 && ddx != -1 && ddy != r && ddx != c){
      if (m[ddy][ddx] != '.')break;
      if (ddy == ty && ddx == tx)return true;
      ddx+=dx[i];
      ddy+=dy[i];
    }
  }
  return false;
}

bool erase(int r,int c,int y1,int x1,int y2,int x2){
  vector<int> tx,ty;
  if (y1 == y2){
    tx.push_back(x1 < x2?x1+1:x2+1);
    ty.push_back(y1);
  }else if (x1 == x2){
    tx.push_back(x1);
    ty.push_back(y1 < y2?y1+1:y2+1);
  }else {
    tx.push_back(x1);
    ty.push_back(y2);
    tx.push_back(x2);
    ty.push_back(y1);
  }
  bool isok=false;
  rep(i,(int)tx.size()){
    if (cango(r,c,y1,x1,ty[i],tx[i]) && cango(r,c,y2,x2,ty[i],tx[i])){isok=true;break;}
  }
  if (isok)m[y1][x1]=m[y2][x2]='.';
  return isok;
}

int main(){
  int r,c;
  while(cin>>r>>c){
    rep(i,r)cin>>m[i];
    vector<pii> in[26];
    rep(i,r){
      rep(j,c){
	if (!isalpha(m[i][j]))continue;
	in[m[i][j]-'A'].push_back(make_pair(i,j));
      }
    }
    int ans=0;
    while(true){
      bool iserased=false;
      rep(i,26){
	if (in[i].size() == 0)continue;
	if (abs(in[i][0].first-in[i][1].first)+abs(in[i][0].second-in[i][1].second) == 1)in[i].clear();
	if (erase(r,c,in[i][0].first,in[i][0].second,in[i][1].first,in[i][1].second))ans+=2,iserased=true,in[i].clear();
      }
      if (!iserased)break;
    }
    cout << ans << endl;
  }
  return 0;
}