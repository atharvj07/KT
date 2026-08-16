#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

#define REP(i, a, b) for(int i = (a); i < int(b); ++i)
#define rep(i, n) REP(i, 0, n)
#define ALL(x) begin(x), end(x)

constexpr double EPS = 1e-5;
struct point {
	double x, y;
	explicit point(double x_ = 0, double y_ = 0):x(x_), y(y_) {}

	inline point operator+(const point &p) const {
		return point(x + p.x, y + p.y);
	}

	inline point operator-(const point &p) const {
		return point(x - p.x, y - p.y);
	}

	inline point operator*(double s) const {
		return point(x * s, y * s);
	}

	inline bool operator<(const point &p) const {
		return x + EPS < p.x || (abs(x - p.x) < EPS && y + EPS < p.y);
	}
};

inline double norm(const point &p) {
	return p.x * p.x + p.y * p.y;
}

inline double dot(const point &a, const point &b) {
	return a.x * b.x + a.y * b.y;
}

inline double cross(const point &a, const point &b) {
	return a.x * b.y - a.y * b.x;
}

inline int ccw(const point &a, point b, point c) {
	b = b - a;
	c = c - a;
	const double t = cross(b, c);
	if(t > EPS) return 1;
	if(t < -EPS) return -1;
	if(dot(b, c) < 0) return 2;
	if(norm(b) < norm(c)) return -2;
	return 0;
}

typedef vector<point> polygon;

struct segment {
	point a, b;
	segment(const point &a_, const point &b_):a(a_), b(b_) {}
};

inline bool intersect(const segment &s, const point &p) {
	return ccw(s.a, s.b, p) == 0;
}

inline bool intersect(const segment &s, const segment &t) {
	return ccw(s.a, s.b, t.a) * ccw(s.a, s.b, t.b) <= 0
		&& ccw(t.a, t.b, s.a) * ccw(t.a, t.b, s.b) <= 0;
}

inline point crosspoint(const segment &s, const segment &t) {
	const double tmp = cross(s.b - s.a, t.b - t.a);
	if(abs(tmp) < EPS) {
		if(intersect(s, t.a)) return t.a;
		if(intersect(s, t.b)) return t.b;
		if(intersect(t, s.a)) return t.a;
		return s.b;
	}
	return t.a + (t.b - t.a) * (cross(s.b - s.a, s.b - t.a) / tmp);
}

constexpr int MAX = 2000;
constexpr int INF = INT_MAX;

void update(vector<int> &exists, const segment &s, const vector<segment> &segments) {
}

int solve(const polygon &P) {
	const int n = P.size();
	vector<segment> segments;
	segments.reserve(n);

	point prev = P.back();
	for(const auto &curr : P) {
		segments.emplace_back(prev, curr);
		prev = curr;
	}

	int ans = 0;
	for(int y = -MAX; y <= MAX; ++y) {
		vector<int> exists(MAX + MAX + 2, 0);
		segment s1(point(-INF, y + EPS), point(INF, y + EPS));
		segment s2(point(-INF, y + 1 - EPS), point(INF, y + 1 - EPS));

		vector<pair<point, point>> cp;
		for(const auto &s : segments) {
			if(intersect(s, s1) && intersect(s, s2)) {
				const point p1 = crosspoint(s, s1);
				const point p2 = crosspoint(s, s2);
				cp.emplace_back(min(p1, p2), max(p1, p2));
			}
		}

		sort(ALL(cp));

		for(int i = 0; i < static_cast<int>(cp.size()); i += 2) {
			++exists[static_cast<int>(floor(cp[i].first.x)) + MAX];
			--exists[static_cast<int>(ceil(cp[i + 1].second.x)) + MAX];
		}

		partial_sum(ALL(exists), exists.begin());
		for(const auto &e : exists) {
			if(e) ++ans;
		}
	}

	return ans;
}

int main() {
	cin.tie(nullptr);
	ios::sync_with_stdio(false);

	for(int n; cin >> n && n;) {
		polygon P;
		P.reserve(n);

		rep(i, n) {
			int x, y;
			cin >> x >> y;
			P.emplace_back(x, y);
		}

		cout << solve(P) << endl;
	}
	return EXIT_SUCCESS;
}