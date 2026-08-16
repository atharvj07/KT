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
#include <assert.h>
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

namespace geom{
#define X real()
#define Y imag()
#define at(i) ((*this)[i])
#define SELF (*this)
	enum {TRUE = 1, FALSE = 0, BORDER = -1};
	typedef int BOOL;
	typedef long double R;
	const R INF = 1e8;
	R EPS = 1e-10;
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
			// 座標の二乗とEPSの差が大きすぎないように注意
			return !sig(outp(p-at(0), dir())) && inp(p-at(0), dir()) > EPS && inp(p-at(1), -dir()) > -EPS;
			//return !sig(abs(at(0)-p) + abs(at(1) - p) - abs(at(0) - at(1)));
		}
	};
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
	};
	BOOL intersect(const S &s, const L &l){
		if(l.online(s[0]) || l.online(s[1])) return BORDER;
		return (sig(outp(l.dir(), s[0]-l[0])) * sig(outp(l.dir(), s[1]-l[0])) <= 0);
	}
	inline P crosspoint(const L &l, const L &m){
		R A = outp(l.dir(), m.dir()), B = outp(l.dir(), l[1] - m[0]);
		if(!sig(abs(A)) && !sig(abs(B))) return m[0]; // same line
		if(abs(A) < EPS) assert(false); // !!!PRECONDITION NOT SATISFIED!!!
		return m[0] + B / A * (m[1] - m[0]);
	}

#undef SELF
#undef at
}

using namespace geom;

int f = 0;
namespace std{
	bool operator<(const P &a, const P &b){return sig(a.X-b.X) ? a.X < b.X : a.Y+EPS < b.Y;}
	bool operator==(const P &a, const P &b){return abs(a-b) < EPS;}
	istream& operator>>(istream &is, P &p){R x,y;is>>x>>y;p=P(x, y);return is;}
	istream& operator>>(istream &is, L &l){l.resize(2);return is >> l[0] >> l[1];}
	const R B = 200;
	const R Z = 30;
	ostream& operator<<(ostream &os, const P &p){return os << "circle("<<B+Z*(p.X)<<", "<<1000-B-Z*(p.Y)<<", 2)";}
	ostream& operator<<(ostream &os, const L &s){return os << "line("<<B+Z*(s[0].X)<<", "<<1000-B-Z*(s[0].Y)<<", "<<B+Z*(s[1].X)<<", "<<1000-B-Z*(s[1].Y)<<")";}
	ostream& operator<<(ostream &os, const G &g){REP(i, g.size()) os << g.edge(i) << endl;return os;}

}

int n;

int main(int argc, char *argv[]){
	ios::sync_with_stdio(false);
int T = 1;
	while(cin >> n, n){
		G g(n);
		vector<R> y;
		REP(i, n){
			cin >> g[i];
			y.push_back(g[i].Y+2*EPS);
			y.push_back(g[i].Y-2*EPS);
		}
		sort(ALL(y)); UNIQUE(y);
		auto cut = [&](R f, R t){
			R sum = 0;
			REP(i, g.size()){
				S s = g.edge(i);
				if(s[0].Y > s[1].Y) swap(s[0], s[1]);
				if(s[1].Y <= f || t <= s[0].Y) continue;
				if(s[0].Y < f && f < s[1].Y) s[0] = (s[1]*(f-s[0].Y)+s[0]*(s[1].Y-f))/(s[1].Y-s[0].Y);
				if(s[0].Y < t && t < s[1].Y) s[1] = (s[1]*(t-s[0].Y)+s[0]*(s[1].Y-t))/(s[1].Y-s[0].Y);
				
				sum += abs(s.dir());
			}
			return sum;
		};
		auto len = [&](R y){
			vector<P> res;
			L l(P(0, y), P(1, y));
			REP(i, g.size()){
				if(sig(g.edge(i).dir().Y) && intersect(g.edge(i), l)) 
					res.push_back(crosspoint(g.edge(i), l));
			}
			sort(ALL(res)); UNIQUE(res);
			R sum = .0;
			REP(i, (int)res.size()-1)
				if(g.contains((res[i]+res[i+1])*(R).5)) sum += abs(res[i+1]-res[i]);
			return sum;
		};
		R ans = .0;
		REP(i, (int)y.size()-1){
			ans += (len(y[i]) + len(y[i+1])) * cut(y[i], y[i+1]);
		}
		printf("%.10f\n", (double)ans);
	}
	return 0;
}