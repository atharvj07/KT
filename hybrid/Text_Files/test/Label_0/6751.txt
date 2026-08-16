#include<iostream>
#include<vector>
#include<complex>
#include<algorithm>
using namespace std;

typedef double R;
typedef complex<R> P;
typedef vector<P> G;
#define REP(i, n) for(int i=0;i<(int)n;i++)
#define RREP(i, n) for(int i=(int)(n)-1;i>=0;i--)
#define X real()
#define Y imag()
const R EPS = 1e-8;
const R INF = 1e8;

inline int sig(const R &x){return abs(x)<EPS ? 0 : x > 0 ? 1 : -1;}
inline R  inp(const P &a, const P &b){return (conj(a)*b).X;}
inline R outp(const P &a, const P &b){return (conj(a)*b).Y;}
inline int ccw(const P &s, const P &t, const P &p){return sig(outp(t-s, p-s));}

inline P crosspoint(const P &p1, const P &p2, const P &q1, const P &q2){
	R A = outp(p2-p1, q2-q1), B = outp(p2-p1, p2-q1);
	if(!sig(A) && !sig(B)) return q1;
	return q1 + B/A * (q2 - q1);
}

R area(const G &g){
	R sum = 0;
	REP(i, g.size()) sum += outp(g[i], g[(i+1)%g.size()]);
	return abs(sum/2);
}

G cut(const G &g, const P &p1, const P &p2){
	G res;
	REP(i, g.size()){
		if(ccw(p1, p2, g[i]) >= 0) res.push_back(g[i]);
		if(ccw(p1, p2, g[i]) * ccw(p1, p2, g[(i+1)%g.size()]) < 0)
			res.push_back(crosspoint(g[i], g[(i+1)%g.size()], p1, p2));
	}
	return res;
}

R calc(const G &g, R a){
	R l = 0, r = INF;
	REP(itr, 100){
		R mid = (l+r)/2;
		if(area(cut(g, P(1, mid), P(0, mid))) < a) l = mid;
		else r = mid;
	}
	return r;
}
int n;
R d, V;
int main(){
	while(cin >> n >> d >> V, n){
		G g;
		REP(i, n){
			R x, y;
			cin >> x >> y;
			g.emplace_back(x, y);
		}
		R ans = 0;
		REP(i, n){
			RREP(i, n) g[i] -= g[0];
			P v = g[1]/abs(g[1]);
			RREP(i, n) g[i] /= v;
			ans = max(ans, calc(g, V/d));
			g.push_back(g[0]); g.erase(g.begin());
		}
		printf("%.11f\n", ans);
	}
	return 0;
}