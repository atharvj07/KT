#include<bits/stdc++.h>
using namespace std;
using Int = long long;

struct HLDecomposition {
  Int n,pos;
  vector<vector<Int> > G;
  vector<Int> vid, head, sub, hvy, par, dep, inv, type;
  
  HLDecomposition(){}
  HLDecomposition(Int sz):
    n(sz),pos(0),G(n),
    vid(n,-1),head(n),sub(n,1),hvy(n,-1),
    par(n),dep(n),inv(n),type(n){}
  
  void add_edge(Int u, Int v) {
    G[u].push_back(v);
    G[v].push_back(u);
  }

  void build(vector<Int> rs={0}) {
    Int c=0;
    for(Int r:rs){
      dfs(r);
      bfs(r, c++);
    }
  }
  
  void dfs(Int rt) {
    using T = pair<Int, Int>;
    stack<T> st;
    par[rt]=-1;
    dep[rt]=0;
    st.emplace(rt,0);
    while(!st.empty()){
      Int v=st.top().first;
      Int &i=st.top().second;
      if(i<(Int)G[v].size()){
	Int u=G[v][i++];
	if(u==par[v]) continue;
	par[u]=v;
	dep[u]=dep[v]+1;
	st.emplace(u,0);
      }else{
	st.pop();
	for(Int j=0;j<(Int)G[v].size();j++){
	  Int &u=G[v][j];
	  if(u==par[v]) swap(u,G[v].back());
	  if(u==par[v]) continue;
	  sub[v]+=sub[u];
	  if(sub[u]>sub[G[v].front()]) swap(u,G[v].front());
	}
      }
    }
  }

  void bfs(Int r,Int c) {
    using T = tuple<Int, Int, Int>;
    stack<T> st;
    st.emplace(r,r,0);
    while(!st.empty()){
      Int v,h;
      tie(v,h,ignore)=st.top();
      Int &i=get<2>(st.top());
      if(!i){
	type[v]=c;
	vid[v]=pos++;
	inv[vid[v]]=v;
	head[v]=h;
        hvy[v]=(G[v].empty()?-1:G[v][0]);
	if(hvy[v]==par[v]) hvy[v]=-1;
      }
      if(i<(Int)G[v].size()){
	Int u=G[v][i++];
	if(u==par[v]) continue;
	st.emplace(u,(hvy[v]==u?h:u),0);
      }else{
	st.pop();
      }
    }
  }
  
  // for_each(vertex)
  // [l,r] <- attention!!  
  template<typename F>
  void for_each(Int u, Int v, const F& f) {
    while(1){
      if(vid[u]>vid[v]) swap(u,v);
      f(max(vid[head[v]],vid[u]),vid[v]);
      if(head[u]!=head[v]) v=par[head[v]];
      else break;
    }
  }

  template<typename T,typename Q,typename F>
  T for_each(Int u,Int v,T ti,const Q &q,const F &f){
    T l=ti,r=ti;
    while(1){
      if(vid[u]>vid[v]){
	swap(u,v);
	swap(l,r);
      }
      l=f(l,q(max(vid[head[v]],vid[u]),vid[v]));
      if(head[u]!=head[v]) v=par[head[v]];
      else break;
    }
    return f(l,r);
  }
  
  // for_each(edge)
  // [l,r] <- attention!!
  template<typename F>
  void for_each_edge(Int u, Int v,const F& f) {
    while(1){
      if(vid[u]>vid[v]) swap(u,v);
      if(head[u]!=head[v]){
	f(vid[head[v]],vid[v]);
        v=par[head[v]];
      }else{
	if(u!=v) f(vid[u]+1,vid[v]);
	break;
      }
    }
  }

  Int lca(Int u,Int v){
    while(1){
      if(vid[u]>vid[v]) swap(u,v);
      if(head[u]==head[v]) return u;
      v=par[head[v]];
    }
  }

  Int distance(Int u,Int v){
    return dep[u]+dep[v]-2*dep[lca(u,v)];
  }
};


template <typename T,typename E>
struct SegmentTree{
  using F = function<T(T,T)>;
  using G = function<T(T,E)>;
  using H = function<E(E,E)>;
  Int n,height;
  F f;
  G g;
  H h;
  T ti;
  E ei;
  vector<T> dat;
  vector<E> laz;
  SegmentTree(Int n_,F f,G g,H h,T ti,E ei):
    f(f),g(g),h(h),ti(ti),ei(ei){init(n_);}
  void init(Int n_){
    n=1;height=0;
    while(n<n_) n<<=1,height++;
    dat.assign(2*n,ti);
    laz.assign(2*n,ei);
  }
  void build(Int n_, vector<T> v){
    for(Int i=0;i<n_;i++) dat[n+i]=v[i];
    for(Int i=n-1;i;i--)
      dat[i]=f(dat[(i<<1)|0],dat[(i<<1)|1]);
  }
  T reflect(Int k){
    return g(dat[k],laz[k]);
  }
  inline void eval(Int k){
    if(laz[k]==ei) return;
    laz[(k<<1)|0]=h(laz[(k<<1)|0],laz[k]);
    laz[(k<<1)|1]=h(laz[(k<<1)|1],laz[k]);
    dat[k]=reflect(k);
    laz[k]=ei;
  }
  void update(Int a,Int b,E x){
    a+=n;b+=n-1;
    for(Int i=height;i;i--) eval(a>>i);
    for(Int i=height;i;i--) eval(b>>i);
    for(Int l=a,r=b+1;l<r;l>>=1,r>>=1){
      if(l&1) laz[l]=h(laz[l],x),l++;
      if(r&1) --r,laz[r]=h(laz[r],x);
    }
    while(a>>=1)
      dat[a]=f(reflect((a<<1)|0),reflect((a<<1)|1));
    while(b>>=1)
      dat[b]=f(reflect((b<<1)|0),reflect((b<<1)|1));
  }
  T query(Int a,Int b){
    a+=n;b+=n-1;
    for(Int i=height;i;i--) eval(a>>i);
    for(Int i=height;i;i--) eval(b>>i);
    T vl=ti,vr=ti;
    for(Int l=a,r=b+1;l<r;l>>=1,r>>=1) {
      if(l&1) vl=f(vl,reflect(l++));
      if(r&1) vr=f(reflect(--r),vr);
    }
    return f(vl,vr);
  }
};

//INSERT ABOVE HERE

const Int MOD = 1e9+7;

signed main(){
  Int n,q;
  scanf("%lld %lld",&n,&q);
  
  HLDecomposition hld(n);
  for(Int i=1;i<n;i++){
    Int a,b;
    scanf("%lld %lld",&a,&b);
    hld.add_edge(a,b);
  }
  hld.build();
  
  auto add=[](Int a,Int b){return (a+b)%MOD;};
  auto mul=[](Int a,Int b){return (a*b)%MOD;};

  struct T{
    Int l,r,s;
    T(){}
    T(Int l,Int r,Int s):l(l),r(r),s(s){};
  };
  struct P{
    Int a,b;
    P(){}
    P(Int a,Int b):a(a),b(b){};
    bool operator==(const P &x)const{return a==x.a&&b==x.b;}
    bool operator!=(const P &x)const{return a!=x.a||b!=x.b;}
  };
  
  auto f=[&](T a,T b){return T(a.l,b.r,add(a.s,b.s));};
  auto g=[&](T a,P b){
	   Int k=a.r-a.l;
	   b.b=add(b.b,a.l*b.a)*k;
	   a.s=add(a.s,add(mul(k*(k-1)/2%MOD,b.a),b.b));
	   return a;
	 };
  auto h=[&](P a,P b){return P(add(a.a,b.a),add(a.b,b.b));};

  SegmentTree<T, P> seg(n,f,g,h,T(-1,-1,0),P(0,0));
  vector<T> vt(n);
  for(Int i=0;i<n;i++) vt[hld.vid[i]]=T(hld.dep[i],hld.dep[i]+1,0);
  seg.build(n,vt);
  
  for(Int i=0;i<q;i++){
    Int c,s,t;
    scanf("%lld %lld %lld",&c,&s,&t);
    Int l=hld.lca(s,t);
    
    if(c==1){
      Int b,a;
      scanf("%lld %lld",&b,&a);
      Int up=(b+MOD-hld.dep[s]*(MOD-a)%MOD)%MOD;
      Int dw=(b+hld.distance(s,t)*a%MOD+MOD-hld.dep[t]*a%MOD)%MOD;      
      hld.for_each(l,s,[&](Int l,Int r){seg.update(l,r+1,P(MOD-a,up));});
      hld.for_each_edge(l,t,[&](Int l,Int r){seg.update(l,r+1,P(a,dw));});      
    }else{      
      auto ask=[&](Int l,Int r){return seg.query(l,r+1);};
      T ans=hld.for_each(s,t,T(0,0,0),ask,f);
      printf("%lld\n",(ans.s+MOD)%MOD);
    }
  }
  return 0;
}

