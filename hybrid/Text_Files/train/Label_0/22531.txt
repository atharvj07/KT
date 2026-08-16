#include"bits/stdc++.h"
using namespace std;

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REPR(i,n) for(int i=(n)-1;i>=0;i--)
const bool DEBUG = false;
const double EPS = 1e-8;
typedef complex<double>point;
point operator*(const point &p, const double &d) {
	return point(real(p)*d, imag(p)*d);
}
namespace std {
	bool operator<(const point &a, const point &b) {
		return real(a) != real(b) ? real(a)<real(b) : imag(a)<imag(b);
	}
}
double dist(const point &a, const point &b) {
	return abs(a - b);
}
struct Line :public vector<point> {
	Line(const point &a, const point &b) {
		push_back(a); push_back(b);
	}
};
typedef vector<Line> Lines;
double cross(const point &a, const point &b) {
	return real(a)*imag(b) - imag(a)*real(b);
}
double dot(const point &a, const point &b) {
	return real(a)*real(b) + imag(a)*imag(b);
}
int ccw(point a, point b, point c) {
	b = b - a, c = c - a;
	if (cross(b, c)>EPS)return +1;
	if (cross(b, c)<-EPS)return -1;
	if (dot(b, c)<-EPS)return +2;
	if (norm(b)<norm(c))return -2;
	return 0;
}

bool intersectSP(const Line &s, const point &p) {
	return abs(s[0] - p) + abs(s[1] - p) - abs(s[1] - s[0])<EPS;
}
bool isSamePoint(const point &p1, const point &p2) {
	return p1==p2||abs(p1 - p2)<=EPS;
}
bool intersectSS(const Line &s, const Line &t) {
	return ccw(s[0], s[1], t[0])*ccw(s[0], s[1], t[1]) <= 0 &&
		ccw(t[0], t[1], s[0])*ccw(t[0], t[1], s[1]) <= 0;
}
bool connectSS(const Line &s, const Line &t) {
	REP(i, 2)REP(j, 2) {
		if (isSamePoint(s[i], t[j]))return true;
		//if (s[i] == t[j])return true;
	}
	return false;
}
point crosspoint(const Line &l, const Line &m) {
	double A = cross(l[1] - l[0], m[1] - m[0]);
	double B = cross(l[1] - l[0], l[1] - m[0]);
	if (abs(A)<EPS&&abs(B)<EPS)return m[0];
	if (abs(A)<EPS)assert(false);
	return m[0] + B / A * (m[1] - m[0]);
}
struct Circle {
	point c; double r;
	int id;
	Circle(const point &c_, double r_, int id_) :c(c_), r(r_), id(id_) {}
	bool contains(const point &p) {
		if (dist(c, p)<r + EPS)return true;
		else return false;
	}
};

struct Polygon :public vector<point> {
	//0->OUT,1->ON,2->IN
	int contains(const point &p) {
		bool in = false;
		int N = this->size();
		for (int i = 0; i<N; i++) {
			point a = this->at(i) - p;
			point b = this->at((i + 1) % N) - p;
			if (imag(a)>imag(b))std::swap(a, b);
			if (imag(a) <= 0 && 0<imag(b))if (cross(a, b)<0)in = !in;
			if (cross(a, b) == 0 && dot(a, b) <= 0)return 1;
		}
		return in ? 2 : 0;
	}
	void print() {
		if (DEBUG) {
			cerr << "number of points:" << this->size() << endl;
            for(int i=0;i<(int)this->size();i++){
				cerr << i + 1 << ":" << this->at(i) << endl;
			}
		}

	}
};
typedef vector<Circle> Circles;
set<int> get_enclosing_circle(const point &p, const Circles &Cs) {
	set<int> ret;
	for (auto c : Cs) {
		if (c.contains(p))ret.insert(c.id);
	}
	return ret;
}

struct Equiv {
	vector<int>links;
	Equiv(int n) :links(n) {
		REP(i, n)links[i] = i;
	}
	int find(int x) {
		int xx = links[x];
		if (xx == x)return x;
		return links[x] = find(xx);
	}
	void unify(int x, int y) {
		int xx = find(x), yy = find(y);
		if (xx <= yy)links[yy] = xx;
		else links[xx] = yy;
	}
};
typedef vector<Lines> vLines;
vLines connectedComponent(const Lines &ls) {
	vLines ret;
	Equiv equiv(ls.size());
	REP(i, (int)ls.size()) {
		REP(j, i) {
			if (connectSS(ls[i], ls[j])) {
				equiv.unify(i, j);
			}
		}
	}
	REP(i, (int)ls.size()) {
		if (equiv.find(i) == i) {
			Lines newLs;
			newLs.push_back(ls[i]);
			FOR(j, i + 1, (int)ls.size()) {
				if (equiv.find(j) == i)newLs.push_back(ls[j]);
			}
			ret.push_back(newLs);
		}
	}
	return ret;
}
typedef pair<double, point>doublePoint;
typedef vector<doublePoint>vDoublePoint;
typedef map<point, vDoublePoint>adjPoint;
typedef vector<point>Points;

point findNext(const vDoublePoint &vdp, const point &p) {
	//隣接点のリスト(偏角ソート済み)から移動前の点を探してその次
	int n = vdp.size();
	REP(i, n) {
		if (p == vdp[i].second) {
			return vdp[(i + 1) % n].second;
		}
	}
	return vdp[0].second;
}
bool used[101][101];
void make_polys(point minPoint, vector<Polygon>&polys,adjPoint &aPoint,map<point, int>&p2id,
map<int, point>&id2p,int id) {
	Polygon ret;
	REP(i, id)REP(j, id)used[i][j] = false;
	ret.push_back(minPoint);
	point curP = aPoint[minPoint][0].second;
	used[p2id[minPoint]][p2id[curP]] = true;
	point lastP = minPoint;
	while (curP != minPoint) {
		ret.push_back(curP);
		point nextP = findNext(aPoint[curP], lastP);
		used[p2id[curP]][p2id[nextP]] = true;
		lastP = curP;
		curP = nextP;
	}

	
	polys.push_back(ret);

    bool all_used=false;
	while (!all_used) {
        all_used=true;
		bool found = false;
		point st, nx;
        st={1e9,1e9};
		REP(i, id) {
            if(found)break;
			for (auto nxt : aPoint[id2p[i]]) {
				if (!used[i][p2id[nxt.second]]) {
                    all_used=false;
					found = true;
                    if(id2p[i]<st){
                        st=id2p[i];
                        nx=nxt.second;
                    }
				}
			}
		}
        if(all_used)break;
		Polygon res;
		res.push_back(st);
		res.push_back(nx);
		used[p2id[st]][p2id[nx]] = true;
		point cur = nx;
		point las = st;
		while (cur != st) {
			vDoublePoint v = aPoint[cur];
			int n = v.size();
			int s_idx = -1;
			bool found = false;
			REP(i, n) {
				if (isSamePoint(v[i].second,las)) {
					s_idx = i; break;
				}
			}
            if(s_idx<0){
                cerr<<cur<<endl;
                cerr<<las<<endl;
            }
            assert(s_idx>=0);
			for (int i = s_idx + 1; i < s_idx + n + 1; i++) {
				int idx = i % n;
				if (v[idx].second == cur)continue;
				int cur_id = p2id[cur];
				int nxt_id = p2id[v[idx].second];
				if (!used[cur_id][nxt_id]) {
					found = true;
					las = cur;
					cur = v[idx].second;
					used[cur_id][nxt_id] = true;
					res.push_back(cur);
					break;
				}
			}
			//if(!found)break;
			if (cur == st)break;
			if (!found)goto END2;
		}
		polys.push_back(res);
	END2:;
	}

}
vector<Polygon> trace(const Lines &ls) {
	//隣接点(偏角付き)のリストを作成
	map<point, vDoublePoint> aPoint;
	//頂点に番号を付けて辺の使用を記録
	map<point, int>p2id;
	map<int, point>id2p;
	int id = 0;

	REP(i, (int)ls.size()) {
		if (!p2id.count(ls[i][0])) {
			p2id[ls[i][0]] = id;
			id2p[id] = ls[i][0];
			id++;
		}
		if (!p2id.count(ls[i][1])) {
			p2id[ls[i][1]] = id;
			id2p[id] = ls[i][1];
			id++;
		}
		aPoint[ls[i][0]].push_back(doublePoint(arg(ls[i][1] - ls[i][0]), ls[i][1]));
		aPoint[ls[i][1]].push_back(doublePoint(arg(ls[i][0] - ls[i][1]), ls[i][0]));
	}
	vector<point>minPoints;
    REP(i,id)REP(j,id)used[i][j]=false;
	//x座標最小の点の計算と隣接点リストのソート
	point minPoint(INT_MAX, INT_MAX);
	adjPoint::iterator it;
	for (it = aPoint.begin(); it != aPoint.end(); ++it) {
		point p = it->first;
		minPoints.push_back(p);
		minPoint = min(minPoint, p);
		vDoublePoint &vdp = it->second;
		sort(vdp.begin(), vdp.end());
	}
	vector<Polygon>polys;
	make_polys(minPoint, polys, aPoint, p2id, id2p, id);
	return polys;
}
bool intersectCC(const Circle &a, const Circle &b) {
	double d = dist(a.c, b.c);
	return abs(a.r - b.r)<d + EPS && d - EPS<a.r + b.r;
}
bool unuse[101];
bool canConnect(point p, point q, const Circles &circles) {
	set<int> p_enclose = get_enclosing_circle(p, circles);
	set<int> q_enclose = get_enclosing_circle(q, circles);
	if (p_enclose.size()>2) {
		cout << p << endl;
		for (auto id : p_enclose) {
			cout << circles[id].c << " " << circles[id].r << endl;
		}
	}
	assert(p_enclose.size() <= 2);
	assert(q_enclose.size() <= 2);
	if (p_enclose != q_enclose) {
		return false;
	}
    REP(i,100)unuse[i]=false;
	for (auto id : p_enclose) {
		unuse[id] = true;
	}
	int n = circles.size();
	vector<Line>segments;
	REP(i, n) {
		if (unuse[i])continue;
		FOR(j, i, n) {
			if (i == j)continue;
			if (unuse[j])continue;
			if (intersectCC(circles[i], circles[j])) {
				segments.push_back(Line(circles[i].c, circles[j].c));
			}
		}
	}
	vLines cc = connectedComponent(segments);
	for (auto ls : cc) {
		if (ls.size() <= 2)continue;
		vector<Polygon>polys = trace(ls);
		for (auto poly : polys) {
			if (poly.contains(p) != poly.contains(q))return false;
		}
	}

	return true;
}

void solve() {
	int N, M; cin >> N >> M;
	//cerr << N << " " << M << endl;
	if (N == 0)exit(0);
	Circles circles;
	REP(i, N) {
		unuse[i] = false;
		double x, y, r; cin >> x >> y >> r;
		point c(x, y);
		circles.push_back({ c,r ,i });
	}
	while (M--) {
		double x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
		point p(x1, y1), q(x2, y2);
		if (canConnect(p, q, circles))cout << "YES";
		else cout << "NO";
		if (M)cout << " ";
		else cout << endl;
	}
}
signed main() {
	while (true)solve();
}
