#include<bits/stdc++.h>
using namespace std;
using Int = long long;

template <typename T,typename E>
struct SegmentTree{
  using F = function<T(T,T)>;
  using G = function<T(T,E)>;
  using H = function<E(E,E)>;
  int n,height;
  F f;
  G g;
  H h;
  T ti;
  E ei;
  vector<T> dat;
  vector<E> laz;
  SegmentTree(int n_,F f,G g,H h,T ti,E ei):
    f(f),g(g),h(h),ti(ti),ei(ei){init(n_);}
  void init(int n_){
    n=1;height=0;
    while(n<n_) n<<=1,height++;
    dat.assign(2*n,ti);
    laz.assign(2*n,ei);
  }
  void build(int n_, vector<T> v){
    for(int i=0;i<n_;i++) dat[n+i]=v[i];
    for(int i=n-1;i;i--)
      dat[i]=f(dat[(i<<1)|0],dat[(i<<1)|1]);
  }
  inline T reflect(int k){
    return g(dat[k],laz[k]);
  }
  inline void eval(int k){
    if(laz[k]==ei) return;
    laz[(k<<1)|0]=h(laz[(k<<1)|0],laz[k]);
    laz[(k<<1)|1]=h(laz[(k<<1)|1],laz[k]);
    dat[k]=reflect(k);
    laz[k]=ei;
  }
  inline void thrust(int k){
    for(int i=height;i;i--) eval(k>>i);    
  }
  inline void recalc(int k){    
    while(k>>=1)
      dat[k]=f(reflect((k<<1)|0),reflect((k<<1)|1));
  }
  void update(int a,int b,E x){
    thrust(a+=n);
    thrust(b+=n-1);
    for(int l=a,r=b+1;l<r;l>>=1,r>>=1){
      if(l&1) laz[l]=h(laz[l],x),l++;
      if(r&1) --r,laz[r]=h(laz[r],x);
    }
    recalc(a);
    recalc(b);
  }
  void set_val(int a,T x){
    thrust(a+=n);
    dat[a]=x;laz[a]=ei;
    recalc(a);
  }
  T query(int a,int b){
    thrust(a+=n);
    thrust(b+=n-1);
    T vl=ti,vr=ti;
    for(int l=a,r=b+1;l<r;l>>=1,r>>=1) {
      if(l&1) vl=f(vl,reflect(l++));
      if(r&1) vr=f(reflect(--r),vr);
    }
    return f(vl,vr);
  }
};

//INSERT ABOVE HERE
char buf[314514];
signed main(){
  int n,q;
  scanf("%d %d",&n,&q);
  scanf("%s",buf);
  string s(buf);
  
  set<int> pos;
  for(int i=0;i<n;i++)
    if(s[i]==')') pos.emplace(i);

  auto f=[](int a,int b){return min(a,b);};
  auto g=[](int a,int b){return a+b;};
  const int INF = 1e7;
  SegmentTree<int, int> seg(n,f,g,g,INF,0);

  int h=0;
  vector<int> v(n);
  for(int i=0;i<n;i++){
    if(s[i]=='(') h++;
    if(s[i]==')') h--;
    v[i]=h;
  }
  seg.build(n,v);
  
  for(int i=0;i<q;i++){
    int p;
    scanf("%d",&p);
    p--;
    if(s[p]=='('){
      s[p]=')';      
      pos.emplace(p);
      seg.update(p,n,-2);
      int a=*pos.begin();
      s[a]='(';
      pos.erase(a);
      seg.update(a,n,2);
      printf("%d\n",a+1);
    }else{
      s[p]='(';
      pos.erase(p);
      seg.update(p,n,2);
      int l=0,r=p;
      while(l+1<r){
	int m=(l+r)>>1;
	if(seg.query(m,n)>=2) r=m;
	else l=m;       
      }      
      s[r]=')';
      pos.emplace(r);
      seg.update(r,n,-2);
      printf("%d\n",r+1);
    }    
  }
  return 0;
}

