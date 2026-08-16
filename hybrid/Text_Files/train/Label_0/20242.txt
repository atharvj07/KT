#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
typedef pair<ll,ll> pll;
typedef pair<int,int> pii;
typedef long double D;
//typedef complex<D> P;
#define F first
#define S second
const ll MOD=1000000007;
//const ll MOD=998244353;

template<typename T,typename U>istream & operator >> (istream &i,pair<T,U> &A){i>>A.F>>A.S; return i;}
template<typename T>istream & operator >> (istream &i,vector<T> &A){for(auto &I:A){i>>I;} return i;}
template<typename T,typename U>ostream & operator << (ostream &o,const pair<T,U> &A){o<<A.F<<" "<<A.S; return o;}
template<typename T>ostream & operator << (ostream &o,const vector<T> &A){int i=A.size(); for(auto &I:A){o<<I<<(--i?" ":"");} return o;}

ll N;
vector<vector<int>> edge;
vector<vector<int>> mx;
int MX=0;
int NS=0;

void dfs1(int u,int p){
  mx[u]={0,0,0};
  for(auto &v:edge[u]){
    if(v==p){continue;}
    dfs1(v,u);
    mx[u].push_back(mx[v][0]+1);
  }
  sort(mx[u].begin(),mx[u].end(),greater<int>());
  mx[u].resize(3);
}

void dfs2(int u,int p,int np){
  mx[u].push_back(np);
  sort(mx[u].begin(),mx[u].end(),greater<int>());
  mx[u].resize(3);
  pii mx1={np+1,p},mx2={1,u};
  if(mx1<mx2){swap(mx1,mx2);}
  for(auto &v:edge[u]){
    if(v==p){continue;}
    mx2=max(mx2,{mx[v][0]+2,v});
    if(mx1<mx2){swap(mx1,mx2);}
  }
  for(auto &v:edge[u]){
    if(v==p){continue;}
    if(v==mx1.S){dfs2(v,u,mx2.F);}
    else{dfs2(v,u,mx1.F);}
  }
  if(mx[u][2]==0){return;}
  //cout<<u+1<<" "<<mx[u]<<endl;
  MX=max(MX,2*mx[u][2]);
  if(mx[u][0]!=mx[u][2]){NS=max(NS,mx[u][0]+mx[u][2]);}
  else if(mx[u][2]>1){NS=max(NS,mx[u][0]+mx[u][2]-1);}
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cin>>N;
  edge.resize(N);
  mx.resize(N);
  for(int i=1;i<N;i++){
    int a,b;
    cin>>a>>b;
    a--; b--;
    edge[a].push_back(b);
    edge[b].push_back(a);
  }
  dfs1(0,-1);
  dfs2(0,-1,0);
  for(int i=1;i<=N;i++){
    if(i<=2){cout<<1;}
    else if(i%2==0){
      if(i<=NS){cout<<0;}
      else{cout<<1;}
    }
    else{
      if(i<=max(MX,NS)){cout<<0;}
      else{cout<<1;}
    }
  }
  cout<<endl;
  //cout<<MX<<" "<<NS<<endl;

  return 0;
}

