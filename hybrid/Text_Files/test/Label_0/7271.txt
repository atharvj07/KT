#include <algorithm>
#include <climits>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;

constexpr double EPS = 1e-9;

struct point {
	double x, y;
	explicit point(double x_ = 0.0, double y_ = 0.0):x(x_), y(y_) {}
	point(const point &p):x(p.x), y(p.y) {}

	point operator+(const point &p) const {
		return point(x + p.x, y + p.y);
	}

	point operator-(const point &p) const {
		return point(x - p.x, y - p.y);
	}

	point operator*(double s) const {
		return point(x * s, y * s);
	}

	point operator*(const point &p) const {
		return point(x * p.x - y * p.y, x * p.y + y * p.x);
	}

	point operator/(double s) const {
		return point(x / s, y / s);
	}

	bool operator<(const point &p) const {
		return x + EPS < p.x || (abs(x - p.x) < EPS && y + EPS < p.y);
	}

	bool operator==(const point &p) const {
		return abs(x - p.x) < EPS && abs(y - p.y) < EPS;
	}
};

inline istream &operator>>(istream &is, point &p) {
	return is >> p.x >> p.y;
}

inline ostream &operator<<(ostream &os, const point &p) {
	return os << '(' << p.x << ", " << p.y << ')';
}

point rotate90(const point &p) {
	return point(-p.y, p.x);
}

double angle(const point &p) {
	return atan2(p.y, p.x);
}

double norm(const point &p) {
	return p.x * p.x + p.y * p.y;
}

double abs(const point &p) {
	return sqrt(norm(p));
}

double dot(const point &a, const point &b) {
	return a.x * b.x + a.y * b.y;
}

double cross(const point &a, const point &b) {
	return a.x * b.y - a.y * b.x;
}

struct line {
	point a, b;
	line(const point &a_, const point &b_):a(a_), b(b_){}
};

struct segment {
	point a, b;
	segment(const point &a_, const point &b_):a(a_), b(b_){}
};

struct circle {
	point c;
	double r;
	circle(const point &c_, const double &r_):c(c_), r(r_){}
};

bool intersect(const line &l, const segment &s) {
	return cross(l.b - l.a, s.a - l.a) * cross(l.b - l.a, s.b - l.a) < EPS;
}

bool intersect(const circle &c, const point &p) {
	return abs(c.c - p) + EPS < c.r;
}

bool intersect(const circle &c, const circle &d) {
	return abs(c.c - d.c) < c.r + d.r + EPS && abs(c.c - d.c) + EPS > abs(c.r - d.r);
}


double dist(const line &l, const point &p) {
	return abs(cross(l.b - l.a, p - l.a)) / abs(l.b - l.a);
}

double dist(const line &l, const segment &s) {
	return intersect(l, s) ? 0 : min(dist(l, s.a), dist(l, s.b));
}

double dist(const segment &s, const point &p) {
	if(dot(s.b - s.a, p - s.a) < 0) return abs(p - s.a);
	if(dot(s.a - s.b, p - s.b) < 0) return abs(p - s.b);
	return dist(line(s.a, s.b), p);
}

bool intersect(const circle &c, const segment &s) {
	return dist(s, c.c) + EPS < c.r;
}

vector<point> crosspoint(const circle &c, const circle &d) {
	vector<point> res;
	if(c.c == d.c || !intersect(c, d)) return res;

	const double tmp = abs(c.c - d.c);
	const double rc = (tmp * tmp + c.r * c.r - d.r * d.r) / (tmp + tmp);
	const double rs = sqrt(c.r * c.r - rc * rc);
	const point diff = (d.c - c.c) / tmp;
	res.emplace_back(c.c + diff * point(rc, rs));
	res.emplace_back(c.c + diff * point(rc, -rs));
	return res;
}

bool intersect(const circle &c1, const point &p1, const point &p2, const circle &c2) {
	if(intersect(c2, p1) || intersect(c2, p2)) return true;

	double theta = angle(p2 - c1.c) - angle(p1 - c1.c);
	if(theta < 0.0) theta += 2 * M_PI;;

	for(const auto &cp : crosspoint(c1, c2)) {
		double phi = angle(cp - c1.c) - angle(p1 - c1.c);

		if(phi < 0.0) phi += 2 * M_PI;
		if(phi < theta + EPS) return true;
	}

	return false;
}

vector<point> tangent(const circle &c, const point &p) {
	const double x = norm(p - c.c);
	double d = x - c.r * c.r;
	if(d < -EPS) return vector<point>();
	d = max(d, 0.0);
	const point q1 = (p - c.c) * (c.r * c.r / x);
	const point q2 = rotate90((p - c.c) * (-c.r * sqrt(d) / x));
	vector<point> res;
	res.emplace_back(c.c + q1 - q2);
	res.emplace_back(c.c + q1 + q2);
	return res;
}

vector<line> tangent(const circle &a, const circle &b) {
	vector<line> res;
	if(abs(a.r - b.r) < EPS) {
		point dir = b.c - a.c;
		dir = rotate90(dir * (a.r / abs(dir)));
		res.emplace_back(a.c + dir, b.c + dir);
		res.emplace_back(a.c - dir, b.c - dir);
	}
	else {
		point p = a.c * (-b.r) + b.c * a.r;
		p = p * (1.0 / (a.r - b.r));
		vector<point> ps = tangent(a, p), qs = tangent(b, p);
		for(unsigned i = 0; i < min(ps.size(), qs.size()); ++i) {
			res.emplace_back(ps[i], qs[i]);
		}
	}

	point p = a.c * b.r + b.c * a.r;
	p = p * (1.0 / (a.r + b.r));
	vector<point> ps = tangent(a, p), qs = tangent(b, p);
	for(unsigned i = 0; i < min(ps.size(), qs.size()); ++i) {
		res.emplace_back(ps[i], qs[i]);
	}

	return res;
}

inline int get_index(const point &p, const vector<point> &points) {
	return lower_bound(begin(points), end(points), p) - begin(points);
}

struct edge {
	int to;
	double cost;
	edge(int to_, double cost_):to(to_), cost(cost_) {}
};

typedef vector<vector<edge>> graph;

double dijkstra(int s, int g, const graph &G) {
	typedef pair<double, int> P;

	const int n = G.size();

	vector<double> dis(n, INT_MAX);
	priority_queue<P, vector<P>, greater<P>> que;

	dis[s] = 0;
	que.push({0, s});

	while(!que.empty()) {
		const double d = que.top().first;
		const int v = que.top().second;
		que.pop();

		if(dis[v] + EPS < d) continue;
		if(v == g) return d;

		for(const auto &e : G[v]) {
			const double next_dis = d + e.cost;

			if(dis[e.to] > next_dis + EPS) {
				dis[e.to] = next_dis;
				que.push({next_dis, e.to});
			}
		}
	}

	return -1;
}

void add_edge(int v, int u, double d, graph &G) {
	G[v].emplace_back(u, d);
	G[u].emplace_back(v, d);
}

int main() {
	cin.tie(nullptr);
	ios::sync_with_stdio(false);
	cout.setf(ios::fixed);
	cout.precision(10);

	constexpr int radius = 100;

	int n;
	point s(0, 0), g;

	cin >> n >> g;

	vector<circle> poles;
	poles.reserve(n);

	for(int i = 0; i < n; ++i) {
		point c;
		cin >> c;
		poles.emplace_back(move(c), radius);
	}

	vector<point> points{s, g};
	vector<vector<point>> on_circle(n);

	points.reserve(n * n);

	for(int i = 0; i < n; ++i) {
		const circle &c1 = poles[i];

		for(const auto &p : tangent(c1, s)) {
			points.emplace_back(p);
			on_circle[i].emplace_back(p);
		}

		for(const auto &p : tangent(c1, g)) {
			points.emplace_back(p);
			on_circle[i].emplace_back(p);
		}

		for(int j = i + 1; j < n; ++j) {
			const circle &c2 = poles[j];
			for(const auto &l : tangent(c1, c2)) {
				points.emplace_back(l.a);
				points.emplace_back(l.b);

				if((abs(c1.c - l.a) - c1.r) < EPS) {
					on_circle[i].emplace_back(l.a);
				}
				else {
					on_circle[j].emplace_back(l.a);
				}

				if((abs(c1.c - l.b) - c1.r) < EPS) {
					on_circle[i].emplace_back(l.b);
				}
				else {
					on_circle[j].emplace_back(l.b);
				}
			}
		}
	}

	sort(begin(points), end(points));
	points.erase(unique(begin(points), end(points)), end(points));

	const int V = points.size();
	graph G(V);

	for(int i = 0; i < V; ++i) {
		for(int j = i + 1; j < V; ++j) {
			const segment seg(points[i], points[j]);

			bool ok = true;
			for(const auto &c : poles) {
				if(intersect(c, seg)) {
					ok = false;
					break;
				}
			}

			if(ok) add_edge(i, j, abs(points[i] - points[j]), G);
		}
	}

	for(int i = 0; i < n; ++i) {
		for(const auto &p1 : on_circle[i]) {
			const int v = get_index(p1, points);

			for(const auto &p2 : on_circle[i]) {
				if(p1 == p2) continue;

				bool ok = true;

				for(int j = 0; j < n; ++j) {
					if(i == j) continue;
					if(intersect(poles[i], p1, p2, poles[j])) {
						ok = false;
						break;
					}
				}

				if(ok) {
					double theta = angle(p2 - poles[i].c) - angle(p1 - poles[i].c);
					if(theta < 0.0) theta += 2 * M_PI;
					add_edge(v, get_index(p2, points), radius * theta, G);
				}
			}
		}
	}

	const auto ans = dijkstra(get_index(s, points), get_index(g, points), G);
	if(ans < 0) {
		cout << "0.0" << endl;
	}
	else {
		cout << ans << endl;
	}

	return EXIT_SUCCESS;
}