#include<bits/stdc++.h>
using namespace std;

#define int long long

vector<int> a,b;
  int n;
  int m;
map<pair<pair<pair<int,int>,pair<int,int>>,int>,int> table;

int get_score(int i,int j,int s,int t,int turn){
  if(table.count({{{i,j},{s,t}},turn})){
    return table[{{{i,j},{s,t}},turn}];
  }
  bool astop=false;
  bool bstop=false;
  int res=0;
  for(int card=0;card<(i-s)+(j-t);card++){
    
    if(card%2==turn){
      int bindex=j-card/2-1;
      assert(t<=bindex);
      if(b[bindex]==-1){
	astop=true;
      }
      else if(!bstop){
	res-=b[bindex];
      }
    }
    else{
      int aindex=i-card/2-1;
      assert(s<=aindex);
      if(a[aindex]==-1){
	bstop=true;
      }
      else if(!astop){
	res+=a[aindex];
      }
     
    }
  }
  
  return table[{{{i,j},{s,t}},turn}]=res;
}

int dfs(int i,int j,int s,int t,int turn,int time,map<pair<pair<pair<int,int>,pair<int,int>>,pair<int,int>>,int> &dp){
    if(time==2) return 0;
  if(i==n && j==m && s==n && t==m) return 0;
  if(dp.count({{{i,j},{s,t}},{turn,time}})){
    return dp[{{{i,j},{s,t}},{turn,time}}];
  }
  int res;
  if(i!=s || j!=t) res=get_score(i,j,s,t,turn)+dfs(i,j,i,j,!turn,0,dp);
    else res=dfs(i,j,i,j,!turn,time+1,dp);
  if((turn==0 && i==n) || (turn==1 && j==m)) return dp[{{{i,j},{s,t}},{turn,time}}]=res;
  if(turn==0){
res=max(res,dfs(i+1,j,s,t,!turn,0,dp));

  }
  else{
   res=min(res,dfs(i,j+1,s,t,!turn,0,dp));
  }
  return dp[{{{i,j},{s,t}},{turn,time}}]=res;
}
signed main(){

  cin>>n>>m;
  a.resize(n);b.resize(m);
  for(int i=0;i<n;i++) cin>>a[i];
  for(int i=0;i<m;i++) cin>>b[i];
  map<pair<pair<pair<int,int>,pair<int,int>>,pair<int,int>>,int> dp;

  int res=dfs(0,0,0,0,0,0,dp);
  cout<<res<<endl;
  return 0;
}