#include<bits/stdc++.h>
 
#define EQ(a,b) (abs((a)-(b)) < EPS)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define fs first
#define sc second
#define pb push_back
#define sz size()
#define all(a) (a).begin(),(a).end()
 
using namespace std;
typedef double D;
typedef complex<D> P;
typedef pair<P,P> L;
typedef vector<P> Poly;
 
const D EPS = 1e-8;
const D PI = acos(-1);
 
inline D dot(P x, P y){return real(conj(x)*y);}
 
inline D cross(P x, P y){return imag(conj(x)*y);}
 
//for line(segment)
inline int ccw(P a,P b,P c){
  b -= a;c -= a;
  if (cross(b,c)>EPS) return 1;   //counter clockwise
  if (cross(b,c)<-EPS) return -1; //clockwise
  if (dot(b, c)<-EPS) return 2;   //c--a--b on line
  if (abs(b)+EPS<abs(c)) return -2;   //a--b--c on line
  return 0;                       //on segment
}
 
inline bool para(L a,L b){return abs(cross(a.fs-a.sc,b.fs-b.sc))<EPS;}
 
inline P line_cp(L a,L b){
  return a.fs+(a.sc-a.fs)*cross(b.sc-b.fs,b.fs-a.fs)/cross(b.sc-b.fs,a.sc-a.fs);
}
 
inline bool is_cp(L a,L b){
  if(ccw(a.fs,a.sc,b.fs)*ccw(a.fs,a.sc,b.sc)<=0)
    if(ccw(b.fs,b.sc,a.fs)*ccw(b.fs,b.sc,a.sc)<=0)return true;
  return false;
}
 
int main(){
  int n,m;
  cin >> n >> m;
 
  vector<Poly> vp(n);
  rep(i,n){
    int l; cin >> l;
    rep(j,l){
      int x,y; cin >> x >> y;
      vp[i].push_back( P(x,y) );
    }
  }
 
  vector<P> h(m);
  vector<L> vl;
  rep(i,m){
    int x,y; cin >> x >> y;
    h[i] = P(x,y);
 
    rep(j,n){
      for(auto x : vp[j]) vl.push_back( L(h[i], x) );
    }
  }
 
  vector<P> can;
  rep(i,m) can.push_back( h[i] );
  rep(i,vl.size()){
    rep(j,i){
      if( para(vl[i], vl[j]) ) continue;
      can.push_back( line_cp(vl[i], vl[j]) );
    }
  }
 
  int ans = 0;
  for(auto x : can){
    int tmp = 0;
    rep(i,m){
      if( EQ(h[i], x) ) tmp++;
      else{
	bool ok = true;
	L see = L(h[i],x);
	rep(j,n){
	  rep(k,vp[j].size()){
	    L edge = L(vp[j][k], vp[j][(k+1)%vp[j].size()]);
	    if( is_cp(see, edge) ){
	      P cp = line_cp(see, edge);
	      if( !EQ(cp, edge.first) && !EQ(cp, edge.second) && !EQ(cp, x) && !EQ(cp, h[i]) ) ok = false;
	    }
	    if(!ok) break;
	  }
	  if(!ok) break;
	}
	if(ok) tmp++;
      }
    }
    ans = max(ans, tmp);
  }
  cout << ans << endl;
}