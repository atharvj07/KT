#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <deque>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <valarray>
#include <unordered_map>
#include <iterator>
#include <functional>
#include <cassert>
using namespace std;
typedef long long int ll;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

#define REP(i,x) for(int i=0;i<(int)(x);i++)
#define REPS(i,x) for(int i=1;i<=(int)(x);i++)
#define RREP(i,x) for(int i=((int)(x)-1);i>=0;i--)
#define RREPS(i,x) for(int i=((int)(x));i>0;i--)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();i++)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();i++)
#define ALL(container) (container).begin(), (container).end()
#define RALL(container) (container).rbegin(), (container).rend()
#define SZ(container) ((int)container.size())
#define mp(a,b) make_pair(a, b)
#define pb push_back
#define eb emplace_back
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }
template<class T> ostream& operator<<(ostream &os, const vector<T> &t) {
os<<"["; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"]"; return os;
}
template<class T> ostream& operator<<(ostream &os, const set<T> &t) {
os<<"{"; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"}"; return os;
}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}
template<class S, class T> pair<S,T> operator+(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first+t.first, s.second+t.second);}
template<class S, class T> pair<S,T> operator-(const pair<S,T> &s, const pair<S,T> &t){ return pair<S,T>(s.first-t.first, s.second-t.second);}
struct UnionFind {
  vector<int> d;
  UnionFind(int n=0) : d(n, -1){}
  bool unite(int x, int y) {
    if ((x = root(x)) != (y = root(y))){
      if (d[y] < d[x]) swap(x, y);
      d[x] += d[y]; d[y] = x;
    }
    return x != y;
  }
  bool find(int x, int y){return root(x) == root(y);}
  int root(int x){return d[x] < 0 ? x : d[x] = root(d[x]);}
  int size(int x=-1) {return x<0 ? d.size() : -d[root(x)];}
};

namespace geom{
#define X real()
#define Y imag()
#define at(i) ((*this)[i])
#define SELF (*this)
	enum {TRUE = 1, FALSE = 0, BORDER = -1};
	typedef int BOOL;
	typedef long double R;
	const R INF = 1e8;
	R EPS = 1e-6;
	const R PI = 3.1415926535897932384626;
	inline int sig(const R &x) { return (abs(x) < EPS ? 0 : x > 0 ? 1 : -1); }
	inline BOOL less(const R &x, const R &y) {return sig(x-y) ? x < y : BORDER;}
	typedef complex<R> P;
	inline R norm(const P &p){return p.X*p.X+p.Y*p.Y;}
	inline R inp(const P& a, const P& b){return (conj(a)*b).X;}
	inline R outp(const P& a, const P& b){return (conj(a)*b).Y;}
	inline P unit(const P& p){return p/abs(p);}
	inline P proj(const P &s, const P &t){return t*inp(s, t)/norm(t);}
	inline int ccw(const P &s, const P &t, const P &p, int adv=0){
		int res = sig(outp(t-s, p-s));
		if(res || !adv) return res;
		if(sig(inp(t-s, p-s)) < 0) return -2;	// p-s-t
		if(sig(inp(s-t, p-t)) < 0) return 2;	// s-t-p
		return 0;								// s-p-t
	}
	
	
	struct L : public vector<P>{	// line
		L(const P &p1, const P &p2){this->push_back(p1);this->push_back(p2);}
		L(){}
		P dir()const {return at(1) - at(0);}
		BOOL online(const P &p)const {return !sig(outp(p-at(0), dir()));}
	};
	struct S : public L{	// segment
		S(const P &p1, const P &p2):L(p1, p2){}
		S(){}
		BOOL online(const P &p)const {
			if(!sig(norm(p - at(0))) || !sig(norm(p - at(1)))) return BORDER;
			// ??§?¨????????????¨EPS???????????§??????????????????????????¨???
			return !sig(outp(p-at(0), dir())) && inp(p-at(0), dir()) > EPS && inp(p-at(1), -dir()) > -EPS;
			//return !sig(abs(at(0)-p) + abs(at(1) - p) - abs(at(0) - at(1)));
		}
	};
	struct C : public P{
		C(){}
		C(const P& p, const R r):P(p), r(r){}
		R r;
		BOOL inside(const P& p)const { return less(norm(p-SELF), r*r);}
	};
	P crosspoint(const L &l, const L &m);
	struct G : public vector<P>{
		G(size_type size=0):vector(size){}
		S edge(int i)const {return S(at(i), at(i+1 == size() ? 0 : i+1));}
		BOOL contains(const P &p)const {
			R sum = .0;
			REP(i, size()){
				if(S(at(i), at((i+1)%size())).online(p)) return BORDER;	// online
				sum += arg((at(i) - p) / (at((i+1)%size()) - p));
			}
			return !!sig(sum);
		}
		R area()const {
			R sum = 0;
			REP(i, size()) sum += outp(at(i), at((i+1)%size()));
			return abs(sum / 2.);
		}
		P gp()const {
			P r(.0, .0);
			REP(i, size()){
				const S &s = edge(i);
				r += (s[0]+s[1])*outp(s[0], s[1]);
			}
			return r / (6*area());
		}
		G convex_hull(bool online = false) {
			if(size() < 2) return *this;
			sort(ALL(*this));
			G r;
			r.resize((int)size()*2);
			int k=0;
			for(int i=0;i<size();r[k++]=at(i++))
				while(k>1 && ccw(r[k-2], r[k-1], at(i)) < 1-online) k--;
			int t = k;
			for(int i=(int)size()-1;i>=0;r[k++]=at(i--))
				while(k>t && ccw(r[k-2], r[k-1], at(i)) < 1-online) k--;
			r.resize(k-1);
			return r;
		}
	};

	inline P proj(const P &s, const L &t){return t[0] + proj(s-t[0], t[1]-t[0]);}
	inline P reflect(const P &s, const L &t){return (R)2.*proj(s, t) - s;}
	inline S reflect(const S &s, const L &t){return S(reflect(s[0], t), reflect(s[1], t));}
	BOOL intersect(const S &s, const S &t){
		const int p = ccw(t[0], t[1], s[0], 1) * ccw(t[0], t[1], s[1], 1);
		const int q = ccw(s[0], s[1], t[0], 1) * ccw(s[0], s[1], t[1], 1);
		return (p>0||q>0) ? FALSE : (!p||!q) ? BORDER : TRUE;
	}
	BOOL intersect(const S &s, const L &l){
		if(l.online(s[0]) || l.online(s[1])) return BORDER;
		return (sig(outp(l.dir(), s[0]-l[0])) * sig(outp(l.dir(), s[1]-l[0])) <= 0);
	}
	R dist2(const L &l, const P &p){return norm(outp(l.dir(), p - l[0])) / norm(l.dir());}
	R dist2(const S &s, const P &p){
		if(inp(p-s[0],  s.dir()) < EPS) return norm(p - s[0]);
		if(inp(p-s[1], -s.dir()) < EPS) return norm(p - s[1]);
		return dist2((const L &)s, p);
	}
	R dist2(const S &s, const L &l){
		return intersect(s, l) ? .0 : min(dist2(l, s[0]), dist2(l, s[1]));
	}
	R dist2(const S &s, const S &t){
		return intersect(s, t) ? .0 : min(min(dist2(s, t[0]), dist2(t, s[0])), 
									   	  min(dist2(s, t[1]), dist2(t, s[1])));
	}
	template <class T> R dist2(const G &g, const T& t){ // todo: ?????¨????????¨?????????????????´???
		R res = INF;
		REP(i, g.size()) res = min(res, dist2(g.edge(i), t));
		return res;
	}
	template<class S, class T> R dist(const S& s, const T& t){return sqrt(dist2(s, t));}
	inline BOOL intersect(const C &a, const C &b){
		return less((a.r-b.r)*(a.r-b.r), norm(a-b)) + less(norm(a-b), (a.r+b.r)*(a.r+b.r)) - 1;
	}
	inline P crosspoint(const L &l, const L &m){
		R A = outp(l.dir(), m.dir()), B = outp(l.dir(), l[1] - m[0]);
		if(!sig(abs(A)) && !sig(abs(B))) return m[0]; // same line
		return m[0] + B / A * (m[1] - m[0]);
	}
	template<class T> vector<T> merge(vector<T> s) {
		REP(i, s.size()) if (s[i][1] < s[i][0]) swap(s[i][0], s[i][1]);
		sort(ALL(s));
		REP(i, s.size())REP(j, i)if(intersect(s[i], s[j]) && !sig(outp(s[i].dir(), s[j].dir()))) {
			s[j][1] = max(s[i][1], s[j][1]);
			s.erase(s.begin() + i--);
			break;
		}
		return s;
	}
	struct Arrangement{
		struct AEdge{
			int u, v, t;
			R cost;
			AEdge(int u=0, int v=0, int t=0, R cost=0)
				:u(u), v(v), t(t), cost(cost){}
		};
		typedef vector<vector<AEdge>> AGraph;
		vector<P> p;
		AGraph g;
		Arrangement(){}
		Arrangement(vector<S> seg){
			seg = merge(seg);
			int m = seg.size();
			REP(i, m){
				REP(j, i) if(sig(outp(seg[i].dir(), seg[j].dir())) && intersect(seg[i], seg[j]))
					p.push_back(crosspoint(seg[i], seg[j]));
			}
			sort(ALL(p)); UNIQUE(p);
			int n=p.size();
			g.resize(n);
			REP(i, m){
				S &s = seg[i];
				vector<pair<R, int>> ps;
				REP(j, n) if(s.online(p[j])) ps.emplace_back(norm(p[j] - s[0]), j);
				sort(ALL(ps));
				REP(j, (int)ps.size()-1){
					const int u=ps[j].second;
					const int v=ps[j+1].second;
					g[u].emplace_back(u, v, 0, 0);
					g[v].emplace_back(v, u, 0, 0);
				}
			}
		}
		
		int getIdx(P q){
			auto it = lower_bound(ALL(p), q);
			if(it == p.end() || *it != q) return -1;
			return it - p.begin();
		}
	};
	struct DualGraph{
		struct DEdge{
			int u, v, f, l;
			R a;
			DEdge(int u, int v, R a):u(u),v(v),f(0),l(0){
				while(PI < a) a -= 2*PI;
				while(a < -PI) a += 2*PI;
				this->a = a;
			}
			bool operator==(const DEdge &opp) const{
				return v==opp.v;
			}
			bool operator<(const DEdge &opp) const{
				return a>opp.a;
			}
			bool operator<(const R &opp) const{
				return a>opp;
			}
		};
		
		int n;
		vector<P> p;
		vector<vector<DEdge>> g;
		UnionFind uf;
		DualGraph(const vector<P> &p):p(p),g(p.size()),n(p.size()),uf(p.size()){}
		void add_edge(const int s, const int t){
			R a = arg(p[t]-p[s]);
			g[s].emplace_back(s, t, a);
			g[t].emplace_back(t, s, a > 0 ? a-PI : a+PI);
			uf.unite(s, t);
		}
		vector<G> poly;
		
		void add_polygon(int s, int t, R a){
			auto e = lower_bound(ALL(g[s]), a-1e-8);
			if(e == g[s].end()) e = g[s].begin();
			if(e->f) return;
			e->f = 1;
			e->l = t;
			poly[t].push_back(p[s]);
			add_polygon(e->v, t, e->a > 0 ? e->a-PI : e->a+PI);
		}
		
		void toSpanningTree(){
			vector<pair<R, pii>> e;
			REP(i, n)REP(j, i)if(!uf.find(i, j))
				e.emplace_back(abs(p[i]-p[j]), pii(i, j));
			sort(ALL(e));
			REP(ii, e.size()){
				const int i = e[ii].second.first;
				const int j = e[ii].second.second;
				if(uf.find(i, j)) continue;
				const S s(p[i], p[j]);
				if([&](){
					REP(k, n)if(i!=k&&j!=k){
						FOR(it, g[k])
						if(intersect(s, S(p[k], p[it->v])) == TRUE) return 0;
					}
					return 1;
				}()) add_edge(i, j);
			}
		}
		
		void dual(){
//			toSpanningTree();
			
			REP(i, n){
				sort(ALL(g[i]));
				UNIQUE(g[i]);
			}
			int s = min_element(ALL(p)) - p.begin();
			poly.emplace_back();
			add_polygon(s, poly.size()-1, -PI*(R).5);
			REP(i, n)REP(j, g[i].size())if(!g[i][j].f){
				poly.emplace_back();
				add_polygon(i, poly.size()-1, g[i][j].a+2.*EPS);
			}
		}
	};

#undef SELF
#undef at
}

using namespace geom;

namespace std{
	bool operator<(const P &a, const P &b){return sig(a.X-b.X) ? a.X < b.X : a.Y+EPS < b.Y;}
	bool operator==(const P &a, const P &b){return norm(a-b) < EPS;}
	istream& operator>>(istream &is, P &p){R x,y;is>>x>>y;p=P(x, y);return is;}

}
int T, n, m;
R W = 12000;

int check(const P &p, const vector<P> &tar){
	vector<R> args;
	REPS(i, (int)tar.size()-1){
		R a = arg((tar[i] - p) / (tar[0] - p));
		if(a < -EPS) a += 2*PI;
		args.pb(a);
	}
	REPS(i, (int)args.size()-1) if(args[i-1] > args[i]) return 0;
	return 1;
}

int main(int argc, char *argv[]){
	ios::sync_with_stdio(false);
	for(int t=1;cin >> n, n;t++){
		vector<P> g(n);
		REP(i, n) cin >> g[i];
		vi idx(n);
		REP(i, n) cin >> idx[i];
		vector<P> g2(n);
		REP(i, n) g2[i] = g[idx[i]-1];
		g = g2;
		vector<S> s;
		vector<L> ls;
		REP(i, n)REP(j, i) ls.eb(g[i], g[j]);
		W = 1000;
		REP(i, ls.size()){
			int f = 0;
			REP(j, ls.size())if(i!=j && outp(ls[i].dir(), ls[j].dir())){
				P p = crosspoint(ls[i], ls[j]);
				W = max({W, abs(p.X), abs(p.Y)}) + 1;
			}
		}
		REP(i, n)REP(j, i){
			P dir = unit(g[j] - g[i]);
			s.eb(g[i] - dir*W*(R)5, g[i] + dir*W*(R)5);
		}
		s.eb(P(-W, -W), P(W, -W));
		s.eb(P(-W, -W), P(-W, W));
		s.eb(P(W, W), P(W, -W));
		s.eb(P(W, W), P(-W, W));
		Arrangement ar(s);
		DualGraph dg(ar.p);
		for(auto &it : ar.g) for(auto &e : it)if(e.u < e.v){
			dg.add_edge(e.u, e.v);
		}
		dg.dual();
		R ans = 0;
		int inff = 0;

		REPS(i, dg.poly.size()-1){
			R area = dg.poly[i].area();
			if(area < EPS) continue;
			if(!check(dg.poly[i].gp(), g)) continue;
			ans += area;
			R minn = 0, maxx = 0;
			for(auto &p : dg.poly[i]){
				chmin(minn, min(p.X, p.Y));
				chmax(maxx, max(p.X, p.Y));
			}
			if(maxx > W-EPS || minn < -W+EPS){
				inff = 1;
				break;
			}
		}
		printf("Case %d: ", t);
		if(ans < EPS) printf("No area\n");
		else if(inff) printf("Infinity\n");
		else printf("%.20f\n", (double)ans);
	}
	return 0;
}