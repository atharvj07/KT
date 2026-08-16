#include <bits/stdc++.h>
using namespace std;

using VI = vector<int>;
using VVI = vector<VI>;
using PII = pair<int, int>;
using LL = long long;
using VL = vector<LL>;
using VVL = vector<VL>;
using PLL = pair<LL, LL>;
using VS = vector<string>;

#define ALL(a)  begin((a)),end((a))
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define SZ(a) int((a).size())
#define SORT(c) sort(ALL((c)))
#define RSORT(c) sort(RALL((c)))

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define FF first
#define SS second
template<class S, class T>
istream& operator>>(istream& is, pair<S,T>& p){
  return is >> p.FF >> p.SS;
}
template<class S, class T>
ostream& operator<<(ostream& os, pair<S,T>& p){
  return os << p.FF << " " << p.SS;
}
template<class T>
void maxi(T& x, T y){
  if(x < y) x = y;
}
template<class T>
void mini(T& x, T y){
  if(x > y) x = y;
}

const double EPS = 1e-10;
const double PI  = acos(-1.0);
const LL MOD = 1e9+7;

class Point{
public:
  double x, y;

  Point(double x = 0.0, double y = 0.0) : x(x), y(y){}

  Point operator + (const Point& p) const{ return Point(x + p.x, y + p.y); }
  Point& operator += (const Point& p){ x += p.x; y += p.y; return *this;}
  Point operator - (const Point& p) const{ return Point(x - p.x, y - p.y); }
  Point& operator -= (const Point& p){ x -= p.x; y -= p.y; return *this;}
  Point operator * (double a) const{ return Point(a*x, a*y); }
  Point& operator *= (double a){ x *= a; y *= a; return *this;}
  Point operator / (double a) const{ return Point(x / a, y / a); }
  Point& operator /= (double a){ x /= a; y /= a; return *this;}

  double abs(){ return sqrt(norm()); }
  double norm(){ return x*x + y*y; }
};

class Circle{
public:
	Point c;
	double r;
};
typedef Point Vector;

double dot(Vector a, Vector b){
	return a.x*b.x + a.y*b.y;
}
double cross(Vector a, Vector b){
	return a.x*b.y - a.y*b.x;
}
Point rotate(Point p,double angle){
  return Point(p.x*cos(angle) - p.y*sin(angle),
			   p.x*sin(angle) + p.y*cos(angle));
}

pair<Point, Point> getCrossPoints(const Circle& c1, const Circle& c2){
  double d = (c2.c - c1.c).abs();
  double a = (c1.r*c1.r + d*d - c2.r*c2.r) / (2*d);
  Vector e = (c2.c - c1.c) / d;
  Vector h = rotate(e, PI/2) * sqrt(max(c1.r*c1.r - a*a, 0.));
  if(d + min(c1.r, c2.r) <= max(c1.r, c2.r))
	return MP(c1.c + e*c1.r, c1.c + e*c1.r);

  return MP(c1.c + e*a + h, c1.c + e*a - h);
}

// ??????????????§?????¢???????????????
// ?????????????????°???O(N^2)
void partCircles(const vector<Circle>& cs, set<LL>& res){
  int N = SZ(cs);
  vector<Point> ps;
  REP(i,N) REP(j,N){
	if(i == j) continue;
	auto cc = getCrossPoints(cs[i], cs[j]);
	Point crossPoints[2] = {cc.FF, cc.SS};
	REP(k,2){
	  Vector delta = crossPoints[1-k] - crossPoints[k];
	  if(delta.abs() == 0)
		delta = crossPoints[k] - cs[i].c;
	  delta /= delta.abs();
	  REP(d,4){
		ps.PB(crossPoints[k] + delta*EPS);
		delta = rotate(delta, PI/2);
	  }
	}
  }

  for(auto&& p: ps){
	LL bit = 0;
	REP(i,N)
	  if((cs[i].c - p).abs() < cs[i].r)
		bit |= 1LL<<i;
	res.insert(bit);
  }
}

// ?????¢?????´?????§??????????????¨????????????????????????????????????
// ????????????O(N^2)
void partPoints(vector<Point> ps, set<PLL>& res){
  int N = SZ(ps);
  REP(i,N){
	Vector e(0,1);
	REP(d,4){
	  ps.PB(ps[i]+e*EPS);
	  e = rotate(e, PI/2);
	}
  }
  
  REP(i,SZ(ps)) REP(j,SZ(ps)){
	if(i == j) continue;
	Point p1 = ps[i];
	Point p2 = ps[j];
	Vector e = p2 - p1;
	e /= e.abs();
	e = rotate(e, PI/2);
	LL b1 = 0, b2 = 0;
	REP(k,N)
	  if(dot(e, ps[k]-p1) >= 0)
		b1 |= 1LL<<k;
	  else
		b2 |= 1LL<<k;
	if(b1 > b2) swap(b1, b2);
	res.insert(MP(b1,b2));
  }
}

int N, M;
double calcBest(LL bps, LL bcs, VI& as, vector<double>& vs, vector<Circle>& cs){
  Point q(0, 0);
  double inv = 0.;
  REP(i,M){
	if((bcs>>i&1) == 0 || (bps>>as[i]&1) == 0) continue;
	double tmp = 1. / (vs[i] * vs[i]);
	q.x += cs[i].c.x * tmp;
	q.y += cs[i].c.y * tmp;
	inv += tmp;
  }
  if(inv <= 0) return 0;
  q.x /= inv;
  q.y /= inv;

  double res = 0.;
  REP(i,M){
	if((bcs>>i&1) == 0 || (bps>>as[i]&1) == 0) continue;
	res += ((cs[i].c - q).norm() - (cs[i].r * cs[i].r)) / (vs[i] * vs[i]);
  }
  return res;
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  while(cin>>N>>M,N){
	vector<Point> ps(N);
	REP(i,N) cin >> ps[i].x >> ps[i].y;
	VI as(M), bs(M);
	vector<double> vs(M);
	vector<Circle> cs(M);
	REP(i,M){
	  cin >> as[i] >> bs[i] >> vs[i];
	  --as[i];
	  --bs[i];
	  cs[i].c = ps[as[i]];
	  cs[i].r = (ps[bs[i]] - ps[as[i]]).abs();
	}
	if(M <= 2){
	  cout << fixed << setprecision(9) << 0. << endl;
	  continue;
	}

	set<LL> planes;
	set<PLL> points;
	partCircles(cs, planes);
	partPoints(ps, points);

	double best = 0.;
	for(auto&& bpos: points){
	  double d1 = 0, d2 = 0;
	  for(auto&& bpls: planes){
		mini(d1, calcBest(bpos.FF, bpls, as, vs, cs));
		mini(d2, calcBest(bpos.SS, bpls, as, vs, cs));
	  }
	  mini(best, d1+d2);
	}

	double ans = 0;
	REP(i,M) ans += pow(cs[i].r / vs[i], 2);
	cout << fixed << setprecision(9) << sqrt((ans+best)/M) << endl;
  }

  return 0;
}