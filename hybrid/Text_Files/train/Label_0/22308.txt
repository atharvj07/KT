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
#include <iterator>
using namespace std;
typedef long long int ll;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;

#define rep(i,x) for(int i=1;i<=(int)(x);i++)
#define REP(i,x) for(int i=0;i<(int)(x);i++)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();i++)
#define RREP(i,x) for(int i=(x);i>=0;i--)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();i++)
#define ALL(container) container.begin(), container.end()
#define SZ(container) ((int)container.size())
#define mp(a, b) make_pair(a, b)

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }
/*
template<class T> ostream& operator<<(ostream &os, const vector<T> &t) {
os<<"["; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"]"; return os;
}
*/
template<class T> ostream& operator<<(ostream &os, const set<T> &t) {
os<<"{"; FOR(it,t) {if(it!=t.begin()) os<<","; os<<*it;} os<<"}"; return os;
}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}



const int INF = 1<<28;
const double EPS = 1e-8;
const int MOD = 1000000007;

struct P{
	double x, y, z;
	P(){}
	P(double a, double b, double c):x(a),y(b),z(c){}
	
	P operator+(P &opp){
		return P(x+opp.x, y+opp.y, z+opp.z);
	}
	P operator-(P &opp){
		return P(x-opp.x, y-opp.y, z-opp.z);
	}
	P operator/(P &opp){
		return P(abs(opp.x)<EPS?0:x/opp.x, abs(opp.y)<EPS?0:y/opp.y, abs(opp.z)<EPS?0:z/opp.z);
	}
	P operator*(double opp){
		return P(x*opp, y*opp, z*opp);
	}
};

struct C{
	P p;
	double r;
	C(){}
	C(P q, double s):p(q),r(s){}
};


double inp(P v1, P v2){
	return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z;
}
double norm(P v){
	return v.x*v.x + v.y*v.y + v.z*v.z;
}

double sp_distance(P t, P p1, P p2){
	P v1 = t - p1;
	P v2 = p2 - p1;
	P v3 = v2*(inp(v1, v2)/norm(v2));
	P v4 = v3 / v2;
	if(v4.x < -EPS || 1+EPS < v4.x) return sqrt(min(norm(t-p1), norm(t-p2)));
	if(v4.y < -EPS || 1+EPS < v4.y) return sqrt(min(norm(t-p1), norm(t-p2)));
	if(v4.z < -EPS || 1+EPS < v4.z) return sqrt(min(norm(t-p1), norm(t-p2)));
	return sqrt(norm(v1 - v3));
}

int n, m, r;
int main(){
	while(cin >> n >> m >> r, n){
		vector<C> cir;
		vector<pair<P, double> > l;
		P e;
		REP(i, n){
			double x,y,z,r;
			cin >> x >> y >> z >> r;
			cir.push_back(C(P(x,y,z),r));
		}
		REP(i, m){
			double x,y,z,b;
			cin >> x >> y >> z >> b;
			l.push_back(mp(P(x,y,z),b));
		}
		cin >> e.x >> e.y >> e.z;
		REP(i, m){
			l[i].second /= norm(l[i].first - e);
//			printf("%d is %f brights\n", i, l[i].second);
		}
		vector<int> lb(n);
		REP(i, n)REP(j, m){
//			printf("dist(<%.0f,%.0f,%.0f>, <%.0f,%.0f,%.0f>, <%.0f,%.0f,%.0f>) = %f\n", cir[i].p.x, cir[i].p.y, cir[i].p.z, l[j].first.x, l[j].first.y, l[j].first.z, e.z, e.y, e.z, sp_distance(cir[i].p, l[j].first, e));
			if(sp_distance(cir[i].p, l[j].first, e) <= cir[i].r+EPS && !(norm(cir[i].p - l[j].first) <= cir[i].r*cir[i].r+EPS && norm(cir[i].p - e) <= cir[i].r*cir[i].r+EPS)){
				lb[i] |= 1<<j;
//				printf("%d and %d is intersect\n", i, j);
			}
		}
		double ans = 0;
		REP(i, 1<<m){
			int b = 0;
			REP(j, n) if(lb[j] & i) b++;
			if(b > r) continue;
			double sum = 0;
			REP(j, m) if((i>>j)&1) sum += l[j].second;
			ans = max(ans, sum);
		}
		printf("%.10f\n", ans);
	}
	return 0;
}