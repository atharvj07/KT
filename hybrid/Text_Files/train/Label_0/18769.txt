#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define pb push_back
#define sz size()
#define all(a) (a).begin(),(a).end()

using namespace std;
typedef long double D;

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector< vector<pii> > graph;

const D EPS = 1e-8;
const D Eps = 1e-5;
const D PI = acos(-1);
inline bool EQ(const D a, const D b){ return abs(a-b)<EPS; }

//for angle
inline D deg_add(D d, D a){
  D res = d + a;
  while(res >= 2*PI) res -= 2*PI;
  while(res < 0) res += 2*PI;
  return res;
}

inline bool in_angle(D d, D l, D r){
  if(l < r) return l+EPS<d and d+EPS<r;
  if(l < d+EPS) return l+EPS<d and d+EPS<r+2*PI;
  return l-2*PI+EPS<d and d+EPS<r;
}

//Point class
struct P{
  D x,y;
  P(D a=0, D b=0):x(a),y(b){}

  inline P operator-()const{ return P(-x,-y); }
  inline P operator+(const P a)const{ return P(x+a.x,y+a.y); }
  inline P operator-(const P a)const{ return P(x-a.x,y-a.y); }
  inline P operator*(const P a)const{ return P(x*a.x-y*a.y, x*a.y+y*a.x); }
  inline P operator*(const D a)const{ return P(x*a,y*a); }
  inline P operator/(const D a)const{ return P(x/a,y/a); }
  
  inline P operator+=(const P a){ return P(x+=a.x,y+=a.y); }
  inline P operator-=(const P a){ return P(x-=a.x,y-=a.y); }
  inline P operator*=(const D a){ return P(x*=a,y*=a); }
  inline P operator/=(const D a){ return P(x/=a,y/=a); }

  inline bool operator==(const P a)const{ return EQ(x,a.x) && EQ(y,a.y); }
  inline bool operator!=(const P a)const{ return !(*this==a); }
  inline bool operator<(const P a)const{ return EQ(x,a.x)?y<a.y:x<a.x; }
  inline bool operator<=(const P a)const{ return *this<a || *this==a; }
  inline bool operator>(const P a)const{ return !(*this<=a); }
  inline bool operator>=(const P a)const{ return !(*this<a); }
};

inline D dot(const P a, const P b){ return a.x*b.x + a.y*b.y; }
inline D cross(const P a, const P b){ return a.x*b.y - a.y*b.x; }

inline D norm(const P a){ return a.x*a.x + a.y*a.y; }
inline D abs(const P a){ return sqrt(norm(a)); }

inline P unit(const P a){ return a/abs(a); }
inline pair<P,P> normal(const P a){ return make_pair(a*P(0,1),a*P(0,-1)); }

inline D arg(const P a){
  D s = atan2(a.y,a.x);
  while(s < 0) s += 2*PI;
  while(s >= 2*PI) s -= 2*PI;
  return s;
}

//rotate a point counter-clockwise on the origin
inline P rotate(const P a, const D s){ return a * P(cos(s),sin(s)); }

//return seta A
inline D arg(P a,P b,P c){
  D s = acos(dot(b-a,c-a)/(abs(b-a)*abs(c-a)));
  while(s < 0) s += 2*PI;
  while(s >= 2*PI) s -= 2*PI;
  return s;
}
inline D arg(D a,D b,D c){
  D s = acos( (b*b+c*c-a*a)/(2*b*c) );
  while(s < 0) s += 2*PI;
  while(s >= 2*PI) s -= 2*PI;
  return s;
}

inline int ccw(const P a,P b,P c){
  b -= a;c -= a;
  if(cross(b,c)>EPS) return 1;      //counter clockwise
  if(cross(b,c)<-EPS) return -1;    //clockwise
  if(dot(b,c)<EPS) return 2;       //c--a--b on line
  if(abs(b)<abs(c)+EPS) return -2;  //a--b--c on line
  return 0;                         //on segment
}

//Line (or Segment) class
struct L{
  P s,t;
  L(const P a=P(0,0), const P b=P(0,1)):s(a),t(b){}
};

inline bool para(L a,L b){return abs(cross(a.s-a.t,b.s-b.t))<EPS;}

inline bool is_cp(L a,L b){
  if(ccw(a.s,a.t,b.s)*ccw(a.s,a.t,b.t)<=0)
    if(ccw(b.s,b.t,a.s)*ccw(b.s,b.t,a.t)<=0)return true;
  return false;
}

inline P line_cp(L a,L b){
  return a.s+(a.t-a.s)*cross(b.t-b.s,b.s-a.s)/cross(b.t-b.s,a.t-a.s);
}

typedef vector<P> Poly;

//all vertex is already sorted.
inline D area(Poly p){
  if(p.size()<3)return 0;
  D res = cross(p[p.sz-1],p[0]);
  rep(i,p.sz-1)res += cross(p[i],p[i+1]);
  return res/2;
}

//convex, vertexes are in the counter-clockwise order.
inline bool in_poly(const Poly p,const P x){
  if(p.size() <= 2) return false;
  rep(i,p.size()){
    P a = p[i], b = p[(i+1)%p.size()];
    if(ccw(a,b,x) != 1) return false;
  }
  return true;
}

struct C{
  P c; D r;
  C(P _c, D _r):c(_c), r(_r) {}
};

inline vector<P> cir_cir_cp(C a, C b){
  vector<P> res;

  D dis = abs(a.c - b.c);
  if(dis > a.r + b.r + EPS) return res;

  P x = unit(b.c - a.c) * a.r;
  if( EQ(dis, a.r+b.r) ){
    res.pb(a.c + x);
  }else{
    D s = arg(b.r, abs(b.c-a.c), a.r);
    res.pb(a.c + rotate(x,s));
    res.pb(a.c + rotate(x,-s));
  }
  return res;
}

inline vector<P> cir_line_cp(C a, L l){
  vector<P> res;
  P n = normal(l.s-l.t).first;
  P p = line_cp(l, L(a.c,a.c+n));
  D dis = abs(p-a.c); 
  if( EQ(dis, a.r) ) res.pb(p);
  else if(dis < a.r){
    D len = sqrt(a.r*a.r - dis*dis);
    P cp_vec = unit(l.s-l.t)*len;
    res.pb(p + cp_vec);
    res.pb(p - cp_vec);
  }
  return res;
}

struct Fin{
  P c;
  D r, d1, d2;
  Fin(P _c, D _r, D _d1, D _d2):c(_c), r(_r), d1(_d1), d2(_d2) {}
};

inline bool in_fin(Fin f, P x){
  D s = arg(x-f.c);
  return abs(f.c-x)+EPS<f.r and in_angle(s,f.d1,f.d2);
}

inline vector<Fin> enumerateFins(L seg, int l, D d1, D d2){
  vector<Fin> fins;
  fins.pb( Fin(seg.s, l, d1, d2) );
  fins.pb( Fin(seg.s, l, deg_add(d1, PI), deg_add(d2, PI)) );
  fins.pb( Fin(seg.t, l, d1, d2) );
  fins.pb( Fin(seg.t, l, deg_add(d1, PI), deg_add(d2, PI)) );
  return fins;
}

inline vector<Poly> enumerateQuads(L seg, int l, D d1, D d2){
  vector<Poly> quads;
  P base(l,0);

  if( para( seg, L(rotate(base,d1),P(0,0)) ) ){
    P ns = seg.s + unit(seg.s-seg.t)*l, nt = seg.t + unit(seg.t-seg.s)*l;
    P n = unit(normal(seg.t-seg.s).first)*Eps;
    quads.pb( { ns+n, ns-n, nt-n, nt+n });
  }else{
    quads.pb( { rotate(base, d1) + seg.s, rotate(base, deg_add(d1,PI)) + seg.s, rotate(base, deg_add(d1,PI)) + seg.t, rotate(base, d1) + seg.t } );
    if(area(quads.back()) < 0) reverse( all(quads.back()) );
  }
  if( para( seg, L(rotate(base,d2),P(0,0)) ) ){
    P ns = seg.s + unit(seg.s-seg.t)*l, nt = seg.t + unit(seg.t-seg.s)*l;
    P n = unit(normal(seg.t-seg.s).first)*Eps;
    quads.pb( { ns+n, ns-n, nt-n, nt+n });
  }else{
    quads.pb( { rotate(base, d2) + seg.s, rotate(base, deg_add(d2,PI)) + seg.s, rotate(base, deg_add(d2,PI)) + seg.t, rotate(base, d2) + seg.t } );
    if(area(quads.back()) < 0) reverse( all(quads.back()) );
  }

  P n1, n2; tie(n1,n2) = normal(seg.t - seg.s);
  D s1 = arg(n1), s2 = arg(n2);
  if( in_angle(s1,d1,d2) or in_angle(s2,d1,d2) ){
    quads.pb( { unit(n1)*l + seg.s, unit(n2)*l + seg.s, unit(n2)*l + seg.t, unit(n1)*l + seg.t } );
    if(area(quads.back()) < 0) reverse( all(quads.back()) );
  }

  return quads;
}

inline bool inValidRegions(P p, const vector< vector<Fin> > &fins, const vector< vector<Poly> > &quads){
  int n = fins.size();
  rep(i,n) for(Fin f : fins[i]){
    if(in_fin(f, p)) return false;
  }
  rep(i,n) for(Poly q : quads[i]){
    if(in_poly(q, p)) return false;
  }
  return true;
}

inline vector<P> enumeratePassPoints(const vector<L> &segs, int l, int r, int k){
  D d = k * PI/r;
  vector<P> candidates;
  vector<Poly> ext_objs;
  P base(l,0);

  for(L seg : segs){
    Poly p;
    if( para(seg, L(rotate(base, d), P(0,0))) ){
      P z = unit(seg.s-seg.t)*Eps;
      p.pb( rotate(base, d) + seg.s + rotate(z,PI/2) );
      p.pb( rotate(base, deg_add(d,PI)) + seg.s + rotate(z,-PI/2) );
      z *= -1;
      p.pb( rotate(base, d) + seg.t + rotate(z,PI/2) );
      p.pb( rotate(base, deg_add(d,PI)) + seg.t + rotate(z,-PI/2) );
    }else{
      p.pb( rotate(base, d) + seg.s);
      p.pb( rotate(base, deg_add(d,PI)) + seg.s );
      p.pb( rotate(base, deg_add(d,PI)) + seg.t );
      p.pb( rotate(base, d) + seg.t );

      P mid = (seg.s + seg.t)/2;
      rep(i,4) p[i] += unit(p[i]-mid)*Eps;
    }

    if(area(p) < 0) reverse( all(p) );
    ext_objs.pb(p);
    rep(i,4) candidates.pb(p[i]);
  }

  rep(i, ext_objs.size()) rep(j, i){
    Poly p1 = ext_objs[i], p2 = ext_objs[j];
    rep(ii,p1.size()) rep(jj,p2.size()) {
      L a(p1[ii], p1[(ii+1)%p1.size()]), b(p2[jj], p2[(jj+1)%p2.size()]);
      if(not para(a,b) and is_cp(a,b)) candidates.pb( line_cp(a,b) );
    }
  }

  sort(all(candidates));
  candidates.erase(unique(all(candidates)), candidates.end());
 
  vector<P> res;
  for(P p : candidates){
    bool f = true;
    for(Poly poly : ext_objs){
      if( in_poly(poly, p) ){
	f = false; break;
      }
    }
    if(f) res.pb(p);
  }

  return res;
}

inline vector<P> enumerateSpinPoints(const vector<L> &segs, int l, int r, int k){
  int n = segs.size();
  D d1 = k * PI/r, d2 = (k+1) * PI/r;
  vector< vector<Fin> >  fins(n);
  vector< vector<Poly> > quads(n);

  rep(i,n){
    fins[i] = enumerateFins(segs[i], l, d1, d2);
    quads[i] = enumerateQuads(segs[i], l, d1, d2);
  }

  vector<P> candidates;
  rep(i,n){
    candidates.pb(segs[i].s);
    candidates.pb(segs[i].t);
  }

  rep(i,n) rep(j,n){
    if(i<j){
      for(Fin f1 : fins[i]){
	for(Fin f2 : fins[j]){
	  vector<P> cps = cir_cir_cp(C(f1.c, f1.r+Eps), C(f2.c, f2.r+Eps));
	  for(P p : cps) candidates.pb(p);
	}
      }

      for(Poly p1 : quads[i]){
	for(Poly p2 : quads[j]){
	  rep(i1,p1.size()) rep(i2,p2.size()) {
	    L a(p1[i1], p1[(i1+1)%p1.size()]), b(p2[i2], p2[(i2+1)%p2.size()]);
	    P na = unit(normal(a.t-a.s).second)*Eps, nb = unit(normal(b.t-b.s).second)*Eps;
	    a.s += na; a.t += na; b.s += nb; b.t += nb;
	    if(not para(a,b) and is_cp(a,b)) candidates.pb( line_cp(a,b) );
	  }
	}
      }
    }

    for(Fin f1 : fins[i]){
      for(Poly p2 : quads[j]){
	rep(i2,p2.size()) {
	  L b(p2[i2], p2[(i2+1)%p2.size()]);
	  P nb = unit(normal(b.t-b.s).first)*Eps;
	  b.s += nb; b.t += nb;
	  vector<P> cps = cir_line_cp(C(f1.c, f1.r+Eps), b);
	  for(P p : cps) candidates.pb(p);
	}
      }
    }
  }

  sort(all(candidates));
  candidates.erase(unique(all(candidates)), candidates.end());

  vector<P> res;
  for(P p : candidates){
    if( inValidRegions(p, fins, quads) ) res.pb(p);
  }

  return res;
}

inline bool isVisible(P s, P t, const vector<Poly> &ext_objs){    
  L l1(s,t);
  for(const Poly& p : ext_objs){
    rep(i, p.size()){
      L l2(p[i], p[(i+1)%p.size()]);
      if(not para(l1,l2) and is_cp(l1, l2)) return false;
    }
  }
  return true;
}

inline graph makeGraph(P S, P G, const vector<L> &objs, const vector< vector<P> > &pass_points, const vector< vector<P> > &spin_points, int l){
  int r = pass_points.size();
  vector<int> id_pass(r+1,0), id_spin(r+1,0);
  rep(k,r){
    id_pass[k+1] = id_pass[k] + pass_points[k].size();
    id_spin[k+1] = id_spin[k] + spin_points[k].size();
  }
  
  int N = id_pass[r] + id_spin[r] + 2;
  graph g(N);

  rep(k,r){
    vector<Poly> ext_objs;
    P base(l,0);
    D d = k * PI/r;
    for(L seg : objs){
      ext_objs.pb( { rotate(base, d) + seg.s, rotate(base, deg_add(d,PI)) + seg.s, rotate(base, deg_add(d,PI)) + seg.t, rotate(base, d) + seg.t } );
      if(area(ext_objs.back()) < 0) reverse( all(ext_objs.back()) );
    }
    
    if(k==0){
      int vid = N-2;
      rep(i, pass_points[k].size()){
	int uid = id_pass[k] + i;
	if( isVisible(S, pass_points[k][i], ext_objs) ) g[vid].pb( pii(uid,0) );
      }
      rep(i, spin_points[k].size()){
	int uid = id_pass[r] + id_spin[k] + i;
	if( isVisible(S, spin_points[k][i], ext_objs) ) g[vid].pb( pii(uid,1) );
      }
      int uid = N-1;
      if( isVisible(S, G, ext_objs) ) g[vid].pb( pii(uid,0) );
    }

    rep(i, pass_points[k].size()){
      int vid = id_pass[k] + i;
      rep(j, i){
	int uid = id_pass[k] + j;
	if( isVisible(pass_points[k][i], pass_points[k][j], ext_objs) ){
	  g[vid].pb( pii(uid,0) );
	  g[uid].pb( pii(vid,0) );
	}
      }
    }

    rep(i, pass_points[k].size()){
      int vid = id_pass[k] + i;
      rep(j, spin_points[k].size()){
	int uid = id_pass[r] + id_spin[k] + j;
	if( isVisible(pass_points[k][i], spin_points[k][j], ext_objs) ) g[vid].pb( pii(uid,1) );
      }
    }

    int prv_k = (k+r-1) % r;
    rep(i, pass_points[k].size()){
      int vid = id_pass[k] + i;
      rep(j, spin_points[prv_k].size()){
	int uid = id_pass[r] + id_spin[prv_k] + j;
	if( isVisible(pass_points[k][i], spin_points[prv_k][j], ext_objs) ) g[uid].pb( pii(vid,0) );
      }
    }

    rep(i, pass_points[k].size()){
      int vid = id_pass[k] + i;
      int uid = N-1;
      if( isVisible(pass_points[k][i], G, ext_objs) ){
	  g[vid].pb( pii(uid,0) );
	  g[uid].pb( pii(vid,0) );
      }
    }
  }
  return g;
}

inline int BFS01(int s, int t, const graph &g){
  int n = g.size();
  vector<int> d(n, -1);
  d[s] = 0;
  deque<int> q; q.push_back(s);

  while(not q.empty()){
    int v = q.front(); q.pop_front();
    for(pii e : g[v]){
      int u = e.first, c = e.second;
      if(d[u]>=0) continue;
      if(u==t) return d[v] + c;

      d[u] = d[v]+ c;
      if(c == 0) q.push_front(u);
      else q.push_back(u);
    }
  }

  return -1;
}

int main(){
  cin.tie(0); ios::sync_with_stdio(0);
  int l, r;
  cin >> l >> r;
  P S, G;
  cin >> S.x >> S.y >> G.x >> G.y;
  cerr << fixed << setprecision(10);

  int n;
  cin >> n;
  vector<L> objs(n);
  rep(i,n){
    cin >> objs[i].s.x >> objs[i].s.y >> objs[i].t.x >> objs[i].t.y;
  }

  vector< vector<P> > pass_points(r);
  rep(k,r) pass_points[k] = enumeratePassPoints(objs, l, r, k);

  vector< vector<P> > spin_points(r);
  rep(k,r) spin_points[k] = enumerateSpinPoints(objs, l, r, k);

  graph vis_graph = makeGraph(S, G, objs, pass_points, spin_points, l);

  int t = vis_graph.size() - 1, s = t-1;
  cout << BFS01(s, t, vis_graph) << endl;
}