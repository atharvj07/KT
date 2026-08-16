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

template <typename T, typename F>
struct SegmentTree{
  // using F = function<T(T,T)>;
  int n;
  F f;
  T ti;
  vector<T> dat;
  SegmentTree(){};
  SegmentTree(F f,T ti):f(f),ti(ti){}
  void init(int n_){    
    n=1;
    while(n<n_) n<<=1;
    dat.assign(n<<1,ti);
  }
  void build(const vector<T> &v){
    int n_=v.size();
    init(n_);
    for(int i=0;i<n_;i++) dat[n+i]=v[i];
    for(int i=n-1;i;i--)
      dat[i]=f(dat[(i<<1)|0],dat[(i<<1)|1]);
  }
  void set_val(int k,T x){
    dat[k+=n]=x;
    while(k>>=1)
      dat[k]=f(dat[(k<<1)|0],dat[(k<<1)|1]);    
  }
  T query(int a,int b){
    T vl=ti,vr=ti;
    for(int l=a+n,r=b+n;l<r;l>>=1,r>>=1) {
      if(l&1) vl=f(vl,dat[l++]);
      if(r&1) vr=f(dat[--r],vr);
    }
    return f(vl,vr);
  }
};

//INSERT ABOVE HERE
const int MAX = 5050;
int dp[2][MAX][MAX];
signed main(){
  int n;
  cin>>n;
  vector<vector<int> > G(n);
  for(int i=1;i<n;i++){
    int x,y;
    cin>>x>>y;
    x--;y--;
    G[x].emplace_back(y);
    G[y].emplace_back(x);
  }
  if(n==2){
    cout<<0<<endl;
    return 0;
  }
  for(int i=0;i<MAX;i++)
    for(int j=0;j<MAX;j++)
      dp[0][i][j]=dp[1][i][j]=MAX;

  vector<int> hs(n),dep(n);
  using P = pair<int, int>;  
  vector<vector<P> > vp(n);
  
  vector<vector<vector<int> > > H(2,vector<vector<int> >(n));
  vector<vector< deque<int> > > ds(2,vector<deque<int> >(n));
  
  function<void(int, int, int)> dfs1=
    [&](int v,int p,int d)->void{      
      hs[v]=0;
      dep[v]=d;
      
      vp[v].clear();
      ds[0][v].clear();
      ds[1][v].clear();
      H[0][v].clear();
      H[1][v].clear();
      
      for(int u:G[v]){
        if(u==p) continue;
        dfs1(u,v,d+1);
        chmax(hs[v],hs[u]+1);      
        vp[v].emplace_back(hs[u]+1,u);  
      }
      sort(vp[v].rbegin(),vp[v].rend());
    };
  
  auto f=[&](int a,int b){return max(a,b);};
  SegmentTree<int, decltype(f)> seg(f,-1);
  seg.build(vector<int>(n,-1));
  
  vector<queue<int> > ss(2);
  function<void(int, int, int)> dfs2=
    [&](int r,int v,int p){
      ds[0][v].emplace_front(v);
      ds[1][v].emplace_front(v);
      if(vp[v].size()==0u) return;
      
      if(vp[v].size()==1u)
        vp[v].emplace_back(0,-1);
      
      int l=vp[v][0].second;
      for(int u:G[v]){
        if(u==p) continue;
        seg.set_val(dep[v],dep[v]+vp[v][u==l].first);        
        dfs2(r,u,v);        
      }
      
      for(int k=0;k<2;k++){
        auto unite=
          [&](int x,int y)->void{          
            if(ds[k][x].size()<ds[k][y].size()) swap(ds[k][x],ds[k][y]);
            for(int i=0;i<(int)ds[k][y].size();i++){
              if(ds[k][x][i]<ds[k][y][i])
                swap(ds[k][x][i],ds[k][y][i]);
              if(~ds[k][y][i])
                H[k][ds[k][x][i]].emplace_back(ds[k][y][i]);
            }
          };
        
        for(int u:G[v]){
          if(u==p) continue;
          ds[k][u].emplace_front(-1);
          if(u!=l) unite(v,u);
        }
        
        auto inch=
          [&](int x,int sd)->void{
            while(!ds[k][x].empty()){
              int y=ds[k][x].back();
              if(y<0){
                ds[k][x].pop_back();
                continue;
              }
              if(y==r) break;
              int dist=dep[y]-dep[v];
              
              // dist+(dist+k) -1 +1
              if(dist+(dist+k)==dep[y]){
                if(dist+sd+k>seg.query(dist+k-1,dep[v])){
                  dp[k][r][y]=v;
                  ss[k].emplace(y);
                  ds[k][x].pop_back();
                  continue;
                }
              }
              
              if(dist+(dist+k)>=dep[y]){
                ds[k][x].pop_back();
                continue;              
              }
              
              if(dist+sd+k>seg.query(dist+k,dep[v])){
                dp[k][r][y]=v;
                ss[k].emplace(y);
                ds[k][x].pop_back();
                continue;
              }
              return;   
            }
          };
        
        inch(v,vp[v][0].first);
        inch(l,vp[v][1].first);
        
        unite(v,l);
      }
    };
  

  for(int i=0;i<n;i++){
    dfs1(i,-1,0);
    dfs2(i,i,-1);

    for(int k=0;k<2;k++){
      while(!ss[k].empty()){
        int v=ss[k].front();ss[k].pop();
        for(int u:H[k][v]){
          dp[k][i][u]=dp[k][i][v];
          ss[k].emplace(u);
        }
      }
      
      for(int j=0;j<n;j++)
        if(dp[k][i][j]!=MAX)
          dp[k][i][j]=dep[j]-dep[dp[k][i][j]];
    }    
  }
  
  int ans=0;
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
      if(i!=j) ans+=dp[0][i][j]<=dp[1][j][i];
  
  cout<<ans<<endl;
  return 0;
}

