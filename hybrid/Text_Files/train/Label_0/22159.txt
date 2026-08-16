#include <algorithm>
#include <numeric>
#include <map>
#include <vector>
#include <cmath>
#include <iostream>
#include <queue>
#include <tuple>
#include <set>
#include <complex>
#include <iomanip>

using namespace std;

typedef long double D;
const D INF = 1e12, EPS = 1e-8;

typedef complex<D> P;

#define X real()
#define Y imag()

struct L : public vector<P> {
  P vec() const {return this->at(1)-this->at(0);}
  L(const P &a, const P &b) {push_back(a); push_back(b);}
  L(){push_back(P()); push_back(P());}
};

struct C {
  P o; D r;
  C(const P &o, D r) : o(o), r(r) {}
};

istream& operator >> (istream& is, complex<D> & p) {D x,y; is >> x >> y; p=P(x,y); return is;}

int sig(D a, D b=0) {return a<b-EPS?-1:a>b+EPS?1:0;}
template<typename T> bool eq(const T& a, const T& b){return sig(abs(a-b)) ==0;}
bool compX (const P& a, const P& b) {return !eq(a.X, b.X)?sig(a.X,b.X)<0:sig(a.Y,b.Y)<0;}

D cross(const P& a, const P& b) {return imag(conj(a)*b);}
D dot(const P& a, const P& b) {return real(conj(a)*b);}
int ccw(const P& a, P b, P c) {
  b -= a; c -= a;
  if (sig(cross(b,c)) > 0) return +1;
  if (sig(cross(b,c)) < 0) return -1;
  if (sig(dot(b,c)) < 0) return +2;
  if (sig(norm(b), norm(c)) < 0) return -2;
  return 0;
}

enum RELATION{INCOMPARABLE=0, SAME=1, CONTAIN=2, OVER=4};
pair<RELATION, int> cRel(const C& c1, const C& c2) {
  D d = abs(c1.o-c2.o);
  if (eq(c1.o,c2.o) && eq(c1.r,c2.r)) return make_pair(SAME, 1<<28);
  if (sig(d, c1.r-c2.r)<0) return make_pair(OVER,0);
  if (sig(d, c2.r-c1.r)<0) return make_pair(CONTAIN,0);
  if (sig(d, c1.r-c2.r)==0) return make_pair(OVER,0);
  if (sig(d, c2.r-c1.r)==0) return make_pair(CONTAIN,1);
  if (sig(d, c1.r+c2.r)==0) return make_pair(INCOMPARABLE,1);
  if (sig(d, c1.r+c2.r)<0) return make_pair(INCOMPARABLE,2);
  return make_pair(INCOMPARABLE, 0);
}

vector<P> intersectionCC(const C& c1, const C& c2) {
  pair<RELATION,int> rel = cRel(c1, c2);
  D d = abs(c2.o-c1.o);
  P diff=(c2.o-c1.o) / d;
  vector<P> res;
  if (rel.second == 1) {
	res.push_back(c1.o+diff*c1.r);
  } else if (rel.second==2) {
	double rc = (d*d + c1.r*c1.r - c2.r*c2.r) / (2*d);
	double rs = sqrt(c1.r*c1.r - rc*rc);
	res.push_back(c1.o+diff*P(rc,rs));
	res.push_back(c1.o+diff*P(rc,-rs));
  }
  return res;
}

P projection(const L &l, const P &p) {
  D t = dot(p-l[0], l.vec()) / norm(l.vec());
  return l[0] + t * l.vec();
}

D distanceLP(const L &l, const P &p) {return abs(p - projection(l, p));}

vector<P> intersectionLC(L l, C c) {
  D d = distanceLP(l, c.o);
  vector<P> res;
  if (sig(d-c.r) == 0) {
	res.push_back(projection(l, c.o));
  } else if (sig(d, c.r)< 0) {
	P m = projection(l, c.o), u = (l[1]-l[0])/abs(l[1]-l[0]);
	D t = sqrt(c.r*c.r - d*d);
	res.push_back(m + t*u); res.push_back(m-t*u);
  }
  return res;
}

vector<P> intersectionSC(L l, C c) {
  vector<P> ps = intersectionLC(l,c), res;
  for (int i = 0; i < (int)ps.size(); i++) {
	if (ccw(ps[i],l[0],l[1]) == +2 || ccw(ps[i],l[1], l[0]) == +2) {
	  res.push_back(ps[i]);
	}
  }
  return res;
}

D getH(D r, D h) {
  D res;
  if (r-h <= EPS) {
	res = r;
  } else {
	res = sqrt(r*r - (r-h)*(r-h));
  }
  return res;
}

vector<D> h(10);
vector<P> cent(10);
int n;
D w;
bool calc(D mid) {
  D m = getH(mid, w);
  if (EPS >= 50-m) {
	return false;
  } else {
	vector<C> circles;
	for (int i = 0; i < n; i++) {
	  circles.push_back(C(cent[i], getH(mid, h[i])));
	}
	for (int i = 0; i < n; i++) {
	  for (int j = 0; j < n; j++) {
		if (i == j) continue;
		vector<P> is = intersectionCC(circles[i], circles[j]);
		for (int k = 0; k < (int)is.size(); k++) {
		  if (m-is[k].X<=EPS &&is[k].X-(100-m)<=EPS && m-is[k].Y<=EPS &&is[k].Y-(100-m)<=EPS){
			bool flag = true;
			for (int l = 0; l < n; l++) {
			  if (circles[l].r - abs(is[k]-cent[l]) > EPS) {
				flag = false;
				break;
			  }
			}
			if (flag) return true;
		  }
		}
	  }
	}
	vector<L> ss;
	ss.push_back(L(P(m, m), P(m, 100-m)));
	ss.push_back(L(P(m, m), P(100-m, m)));
	ss.push_back(L(P(m, 100-m), P(100-m, 100-m)));
	ss.push_back(L(P(100-m, m), P(100-m, 100-m)));
	for (int i = 0; i < n; i++) {
	  for (int j = 0; j < 4; j++) {
		vector<P> is = intersectionSC(ss[j], circles[i]);
		for (int k = 0; k < (int)is.size(); k++) {
		  bool flag = true;
		  for (int l = 0; l < n; l++) {
			if (circles[l].r - abs(is[k]-cent[l]) > EPS) {
			  flag = false;
			  break;
			}
		  }
		  if (flag) return true;
		}
	  }
	}
	vector<P> is(4);
	is[0] = P(m, m); is[1] = P(m, 100-m); is[2] = P(100-m, m); is[3] = P(100-m, 100-m);
	for (int k = 0; k < 4; k++) {
	  bool flag = true;
	  for (int l = 0; l < n; l++) {
		if (circles[l].r - abs(is[k]-cent[l]) > EPS) {
		  flag = false;
		  break;
		}
	  }
	  if (flag) return true;
	}
  }
  return false;
}

int main() {
  cout << fixed << setprecision(10);
  while (true) {
	cin >> n >> w;
	if (n == 0 && w == 0) break;
	for (int i = 0; i < n; i++) {
	  D x, y;
	  cin >> x >> y >> h[i];
	  cent[i] = P(x, y);
	}

	D lb = 0.0, ub = 100000000.0;
	for (int z = 0; z < 100; z++) {
	  D mid = (lb + ub) / 2;
	  if (calc(mid)) {
		lb = mid;
	  } else {
		ub = mid;
	  }
	}
	cout << lb << endl;
  }
}