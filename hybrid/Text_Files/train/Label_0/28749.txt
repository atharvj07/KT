#include<bits/stdc++.h>
using namespace std;
using Int = long long;
template<typename T1,typename T2> inline void chmin(T1 &a,T2 b){if(a>b) a=b;}
template<typename T1,typename T2> inline void chmax(T1 &a,T2 b){if(a<b) a=b;}


template<typename T>
struct Kruskal{
  
  struct edge{
    Int from,to;
    T cost;
    Int used;
    edge(){}
    edge(Int from,Int to,T cost):
      from(from),to(to),cost(cost),used(0){}
    bool operator<(const edge& e) const{
      return cost<e.cost;
    }
  };

  Int n;
  vector<Int> p,r;
  vector<edge> edges;

  Kruskal(){}
  Kruskal(Int n):n(n){}

  void init(Int n){
    r.assign(n,1);
    p.resize(n);
    iota(p.begin(),p.end(),0);
  }
  
  Int find(Int x){
    return (x==p[x]?x:p[x]=find(p[x]));
  }

  bool same(Int x,Int y){
    return find(x)==find(y);
  }

  void unite(Int x,Int y){
    x=find(x);y=find(y);
    if(x==y) return;
    if(r[x]<r[y]) swap(x,y);
    r[x]+=r[y];
    p[y]=x;
  }

  void add_edge(Int u,Int v,T c){
    edges.emplace_back(u,v,c);
  }
  
  T build(){
    sort(edges.begin(),edges.end());
    init(n);
    T res=0;
    for(auto &e:edges){
      if(!same(e.from,e.to)){
        res+=e.cost;
        unite(e.from,e.to);
        e.used=1;
      }
    }
    return res;
  }
};

//INSERT ABOVE HERE
signed main(){
  Int n,d;
  cin>>n>>d;
  vector<Int> a(n);
  for(Int i=0;i<n;i++) cin>>a[i];
  Kruskal<Int> ks(n);
  using P = pair<Int, Int>;
  using PP = pair<P, P>;
  auto add_edge=
    [&](Int x,Int y){
      Int c=abs(x-y)*d+a[x]+a[y];
      ks.add_edge(x,y,c);
    };
  
  function<PP(Int, Int)> dfs=
    [&](Int l,Int r)->PP{
      if(l+1==r) return PP(P(a[l]-l*d,l),P(a[l]+l*d,l));
      Int m=(l+r)>>1;      
      PP x=dfs(l,m),y=dfs(m,r);
      
      for(Int i=l;i<m;i++)
        add_edge(i,y.second.second);
      for(Int i=m;i<r;i++)
        add_edge(x.first.second,i);

      return PP(min(x.first,y.first),min(x.second,y.second));
    };  
  dfs(0,n);

  cout<<ks.build()<<endl;
  return 0;
}
