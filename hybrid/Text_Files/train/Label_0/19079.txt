#include<bits/stdc++.h>
using namespace std;
#define int long long

typedef long long ll;
typedef pair<int,int> P;

template <typename T,typename E>
struct SegmentTree{
  typedef function<T(T,E)> G;
  typedef function<T(E,E)> H;
  int n;
  G g;
  H h;
  T d1;
  E d0;
  vector<T> dat;
  vector<E> laz;
  SegmentTree(int n_,G g,H h,T d1,E d0,vector<T> v=vector<T>()){
    this->g=g;
    this->h=h;
    this->d1=d1;
    this->d0=d0;
    init(n_);
    if(n_==(int)v.size()) build(n_,v);
  }
  void init(int n_){
    n=1;
    while(n<n_) n*=2;
    dat.clear();
    dat.resize(n,d1);
    laz.clear();
    laz.resize(2*n-1,d0);
  }
  void build(int n_, vector<T> v){
    for(int i=0;i<n_;i++) dat[i]=v[i];
  }
  void update(int a,int b,E x,int k,int l,int r){
    if(r<=a||b<=l) return;
    if(a<=l&&r<=b){
      laz[k]=h(laz[k],x);
      return;
    }
    update(a,b,x,k*2+1,l,(l+r)/2);
    update(a,b,x,k*2+2,(l+r)/2,r);
  }
  void update(int a,int b,E x){
    update(a,b,x,0,0,n);
  }
  T query(int k){
    T c=dat[k];
    k+=n-1;
    E x=laz[k];
    while(k>0){
      k=(k-1)/2;
      x=h(x,laz[k]);
    }
    return g(c,x);
  }
};

SegmentTree<ll,ll> rsq(100009,
         [](ll a,ll b){return min(a,b);},
         [](ll a,ll b){return min(a,b);},
         1e17,1e17);
 
struct HLD {
  int n,pos;
  vector<vector<int> > G;
  vector<int> vid, head, sub, hvy, par, dep, inv, type;

  HLD(){}
  HLD(int sz):n(sz),pos(0),G(n),vid(n,-1),head(n),sub(n,1),hvy(n,-1),par(n),dep(n),inv(n),type(n){}
  
  void add_edge(int u, int v) {
    G[u].push_back(v);
    G[v].push_back(u);
  }

  void build() {
    dfs(0);
    bfs(0, 0);
  }

  void build_2(vector<int> rs) {
    int c=0;
    for(int i=0;i<rs.size();i++){
        int r=rs[i];
      dfs(r);
      bfs(r, c++);
    }
  }
  
  void dfs(int rt) {
    stack<P> st;
    par[rt]=-1;
    dep[rt]=0;
    st.push(P(rt,0));
    while(!st.empty()){
        int v=st.top().first;
        int &i=st.top().second;
        if(i<(int)G[v].size()){
            int u=G[v][i++];
            if(u==par[v]) continue;
            par[u]=v;
            dep[u]=dep[v]+1;
            st.push(P(u,0));
        }else{
            st.pop();
            int res=0;
            for(int i=0;i<G[v].size();i++){
                int u=G[v][i];
                if(u==par[v]) continue;
                sub[v]+=sub[u];
                if(res<sub[u]) res=sub[u],hvy[v]=u;
            }
        }
    }
  }

  void bfs(int r,int c) {
    int &k=pos;
    queue<int> q;
    q.push(0);
    while(!q.empty()){
      int h=q.front();q.pop();
      for(int i=h;i!=-1;i=hvy[i]) {
        type[i]=c;
        vid[i]=k++;
        inv[vid[i]]=i;
        head[i]=h;
        for(int J=0;J<G[i].size();J++){
            int j=G[i][J];
            if(j!=par[i]&&j!=hvy[i]) q.push(j);
        }
      }
    }
  }
  
  // for_each(vertex)
  // [l,r] <- attention!!
  int for_each(int u, int v) {
    int ans=0;
    while(1){
      if(vid[u]>vid[v]) swap(u,v);
      //f(max(vid[head[v]],vid[u]),vid[v]);
      //ans = max(ans,rmq.query(l, r + 1));
      if(head[u]!=head[v]) v=par[head[v]];
      else {return ans;}
    }
  }
  
  // for_each(edge)
  // [l,r] <- attention!!
  ll for_each_edge(int u, int v) {
    ll ans=0;
    while(1){
      if(vid[u]>vid[v]) swap(u,v);
      if(head[u]!=head[v]){
        //f(vid[head[v]],vid[v]);
        ans += rsq.query(vid[head[v]]);
        v=par[head[v]];
      } else{
        //if(u!=v) f(vid[u]+1,vid[v]);
        //cout<<1<<endl;
        if(u!=v) ans += rsq.query(vid[u]+1);
        return ans;
      }
    }
  }

  /*void update_edge(int u,int w){
    rsq.add(vid[u],w);
  }*/

  void range_update_edge(int u,int v,int w){
    while(1){
      if(vid[u]>vid[v]) swap(u,v);
      if(head[u]!=head[v]){
        //f(vid[head[v]],vid[v]);
        rsq.update(vid[head[v]],vid[v]+1,w);
        v=par[head[v]];
      } else{
        //if(u!=v) f(vid[u]+1,vid[v]);
        rsq.update(vid[u]+1,vid[v]+1,w);
        break;
      }
    }
  }

  void range_update_vertex(int u,int v,int w){
    while(1){
      if(vid[u]>vid[v]) swap(u,v);
      //cout<<u<<' '<<v<<endl;
      if(head[u]!=head[v]){
        //f(vid[head[v]],vid[v]);
        rsq.update(vid[head[v]],vid[v]+1,w);
        v=par[head[v]];
      } else{
        //if(u!=v) f(vid[u]+1,vid[v]);
        rsq.update(vid[u],vid[v]+1,w);
        break;
      }
    }
  }

  int lca(int u,int v){
    while(1){
      if(vid[u]>vid[v]) swap(u,v);
      if(head[u]==head[v]) return u;
      v=par[head[v]];
    }
  }

  int distance(int u,int v){
    return dep[u]+dep[v]-2*dep[lca(u,v)];
  }
};
set<P>st;
struct Kruskal{
  struct UnionFind{
    int n;
    vector<int> r,p;
    UnionFind(){}
    UnionFind(int sz):n(sz),r(sz,1),p(sz,0){
      iota(p.begin(),p.end(),0);
      for(int i=0;i<n;i++){
        //cout<<p[i]<<endl;
      }
    }
    int find(int x){
      return (x==p[x]?x:p[x]=find(p[x]));
    }
    bool same(int x,int y){
      return find(x)==find(y);
    }
    void unite(int x,int y){
      x=find(x);y=find(y);
      if(x==y) return;
      if(r[x]<r[y]) swap(x,y);
      r[x]+=r[y];
      p[y]=x;
    }
  };
  
  struct edge{
    int from,to,cost,used;
    edge(){}
    edge(int from,int to,int cost):
      from(from),to(to),cost(cost),used(0){}
    bool operator<(const edge& e) const{
      return cost<e.cost;
    }
  };

  int n;
  vector<edge> edges;

  Kruskal(){}
  Kruskal(int sz):n(sz){}
  
  void add_edge(int u,int v,int c){
    edges.emplace_back(u,v,c);
  }

  void input(int m,int offset=0){
    int a,b,c;
    for(int i=0;i<m;i++){
      cin>>a>>b>>c;
      add_edge(a+offset,b+offset,c);
    }
  }
  
  int build(){
    sort(edges.begin(),edges.end());
    UnionFind uf(n+1);
    int res=0;
    //cout<<edges.size()<<endl;
    for(auto &e:edges){
      if(!uf.same(e.from,e.to)){
        //cout<<e.from<<' '<<e.to<<endl;
        st.insert(P(e.from,e.to));
        st.insert(P(e.to,e.from));
        res+=e.cost;
        uf.unite(e.from,e.to);
        e.used=1;
      }
    }
    return res;
  }
};



signed main(){
    Kruskal K(100009);
    int n,x,w,p,m;
    scanf("%ld%ld",&n,&m);
    int a[m],b[m],c[m];
    for(int i=0;i<m;i++){
      scanf("%ld%ld%ld",&a[i],&b[i],&c[i]);
      a[i]--;b[i]--;
      K.add_edge(a[i],b[i],c[i]);
    }

    int X=K.build();
    //return 0;
    HLD Tree(n);
    for(int i=0;i<m;i++){
     // cout<<a[i]<<' '<<b[i]<<endl;
      if(st.count(P(a[i],b[i]))){
       // cout<<a[i]<<b[i]<<endl;
        Tree.add_edge(a[i],b[i]);
      }
    }//return 0;
    Tree.build();
    for(int i=0;i<m;i++){
      if(!st.count(P(a[i],b[i]))){
        Tree.range_update_edge(a[i],b[i],c[i]);
      }
    }
    for(int i=0;i<m;i++){
      if(!st.count(P(a[i],b[i])))cout<<X<<endl;
      else{
        ll XX=X-c[i]+Tree.for_each_edge(a[i],b[i]);
        if(XX>=1e16)cout<<-1<<endl;
        else cout<<XX<<endl;
      }
    }
}
