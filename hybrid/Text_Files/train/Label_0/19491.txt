#include<bits/stdc++.h>
#define EQ(a,b) (abs((a)-(b)) < EPS)
using namespace std;
typedef double D;
typedef complex<D> P;
typedef pair<P,P> L;
typedef pair<int,int> pii;
typedef vector<pii> vp;

const D EPS = 1e-8;
const D PI = acos(-1);

void normalize(vector<int> &v){
  map<int,int> cnt;
  int k = 0;
  for(int i=0;i<(int)v.size();i++){
    if(cnt.count(v[i]) == 0){
      cnt[v[i]] = k++;
    }
  }
 
  for(int i=0;i<(int)v.size();i++){
    v[i] = cnt[v[i]];
  }
}

inline D dot(P a, P b){
  return real(conj(a)*b);
}

inline D cross(P a, P b){
  return imag(conj(a)*b);
}

inline int ccw(P a, P b, P c){
  b -= a; c-= a;
  if(cross(b,c)>EPS) return 1;
  if(cross(b,c)<-EPS) return -1;
  return 0;
}

inline P rotate(P v, D s){
  return P(real(v)*cos(s) - imag(v)*sin(s), real(v)*sin(s) + imag(v)*cos(s) );
}

inline P norm(P p){return p*P(0,1);}

map< pair<int, vector<int> >, int> memo;

int rec(int d, vector<int> use, vector<vp> &segs){
  pair< int, vector<int> > key(d,use);
  if(memo.count(key)) return memo[key];

  if(d == (int)segs.size()){
    /*
    for(int i=0;i<(int)use.size();i++){
      cout << use[i] << " ";
    }
    cout << endl;
    */

    set<int> c;
    for(int x : use) c.insert(x);

    if(c.size() == 1) return 0;
    else return 100;
  }

  int res = rec(d+1,use,segs);

  for(auto p : segs[d]){
    int a = use[p.first], b = use[p.second];
    for(int i=0;i<(int)use.size();i++){
      if(use[i] == a) use[i] = b;
    }
  }
  normalize(use);
  res = min(res, rec(d+1,use,segs) + 1);

  return memo[key] = res;
}

int main(){
  int n;
  cin >> n;

  vector<P> p(n);
  for(int i=0;i<n;i++){
    int x,y;
    cin >> x >> y;
    p[i] = P(x,y);
  }

  vector< vp > segs;
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      P mid = (p[i]+p[j])/2.0;
      P nv = norm(p[i] - p[j]);
      L seg = make_pair(mid, mid + nv);

      vp ans;
      for(int k=0;k<n;k++){
	for(int l=k+1;l<n;l++){
	  P mid_c = (p[k]+p[l])/2.0;
	  if( ccw(seg.first, seg.second, mid_c) == 0 ){
	    if( abs( dot(seg.second - seg.first, p[k] - p[l])) < EPS){
	      ans.push_back( make_pair(k,l) );
	    }
	  }
	}
      }
      /*
      cout << i << " " << j << ": " << endl;
      for(pii a : ans){
	cout << a.first << "," << a.second << " ";
      }
      cout << endl;
      */

      segs.push_back(ans);
    }
  }

  vector<int> use(n,0);
  for(int i=0;i<n;i++)use[i] = i;

  cout << rec(0,use,segs) << endl;
}