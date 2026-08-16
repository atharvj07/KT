#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>
namespace lc {
static const double EPS = 1e-9;
}
namespace lc {
struct Point {
	double x;
	double y;
	explicit Point(const double &x = 0.0, const double &y = 0.0) :
		x(x), y(y)
	{ }
	Point operator+(const Point &p) const { return Point(x + p.x, y + p.y); }
	Point &operator+=(const Point &p){ return *this = *this + p; }
	Point operator-(const Point &p) const { return Point(x - p.x, y - p.y); }
	Point operator*(double s) const { return Point(x * s, y * s); }
	bool operator==(const Point &p) const { return x == p.x && y == p.y; }
	bool operator<(const Point &p) const {
		return (x == p.x) ? (y < p.y) : (x < p.x);
	}
	double abs() const { return sqrt(x * x + y * y); }
	double norm() const { return x * x + y * y; }
};
inline Point operator*(double s, const Point &p){ return p * s; }
inline double cross(const Point &a, const Point &b){
	return a.x * b.y - a.y * b.x;
}
inline double dot(const Point &a, const Point &b){
	return a.x * b.x + a.y * b.y;
}
inline int ccw(const Point &a, const Point &b, const Point &c){
	Point d = b - a, e = c - a;
	if(cross(d, e) > 0.0){ return 1; }
	if(cross(d, e) < 0.0){ return -1; }
	if(dot(d, e) < 0.0){ return 2; }
	if(d.abs() < e.abs()){ return -2; }
	return 0;
}
}
namespace lc {
struct Line {
	Point a;
	Point b;
	explicit Line(const Point &a = Point(), const Point &b = Point()) :
		a(a), b(b)
	{ }
	Point projection(const Point &p) const {
		double t = dot(p - a, b - a) / (b - a).norm();
		return a + t * (b - a);
	}
};
}
namespace lc {
class Polygon {
private:
	std::vector<Point> m_points;
public:
	Polygon() : m_points() { }
	explicit Polygon(size_t s, const Point &p = Point())
		: m_points(s, p)
	{ }
	template <typename Iterator>
	explicit Polygon(Iterator begin, Iterator end)
		: m_points(begin, end)
	{ }
	explicit Polygon(std::initializer_list<Point> init)
		: m_points(init)
	{ }
	const Point &operator[](int i) const { return m_points[i]; }
	Point &operator[](int i){ return m_points[i]; }
	int size() const { return static_cast<int>(m_points.size()); }
	int contains(const Point &p) const {
		int result = -1;
		for(int i = 0; i < size(); ++i){
			Point a = m_points[i] - p;
			Point b = m_points[(i + 1) % size()] - p;
			if(a.y > b.y){ std::swap(a, b); }
			if(a.y <= 0.0 && b.y > 0.0 && cross(a, b) < 0.0){
				result = -result;
			}
			if(cross(a, b) == 0.0 && dot(a, b) <= 0.0){ return 0; }
		}
		return result;
	}
};
}
namespace lc {
inline Polygon convex_hull(const std::vector<Point> &points){
	const int n = points.size();
	std::vector<Point> ps(points);
	std::sort(ps.begin(), ps.end());
	std::vector<Point> ch(2 * n);
	int k = 0;
	for(int i = 0; i < n; ch[k++] = ps[i++]){
		while(k >= 2 && ccw(ch[k - 2], ch[k - 1], ps[i]) <= 0){ --k; }
	}
	for(int i = n - 2, t = k + 1; i >= 0; ch[k++] = ps[i--]){
		while(k >= t && ccw(ch[k - 2], ch[k - 1], ps[i]) <= 0){ --k; }
	}
	ch.resize(k - 1);
	return Polygon(ch.begin(), ch.end());
}
}
namespace lc {
class Visualizer {
private:
	double m_scale;
	double m_offset_x;
	double m_offset_y;
public:
	explicit Visualizer(
		double scale = 1.0, double offset_x = 0.0, double offset_y = 0.0)
		: m_scale(scale)
		, m_offset_x(offset_x)
		, m_offset_y(offset_y)
	{ }
};
}
using namespace std;
static const double EPS = lc::EPS;
static const lc::Point DIR_TABLE[4] = {
	lc::Point(1.0, 0.0),
	lc::Point(0.0, 1.0),
	lc::Point(-1.0, 0.0),
	lc::Point(0.0, -1.0)
};
int main(){
	ios_base::sync_with_stdio(false);
	cout << setiosflags(ios::fixed) << setprecision(10);
	lc::Visualizer vis(1.0, 0.0, 0.0);
	while(true){
		int m, n;
		cin >> m >> n;
		if(m == 0 && n == 0){ break; }
		vector<lc::Point> segments(m), polls(n * 4);
		for(int i = 0; i < m; ++i){ cin >> segments[i].x >> segments[i].y; }
		for(int i = 0; i < n; ++i){
			double x, y;
			cin >> x >> y;
			polls[i * 4 + 0] = lc::Point(x, y) + DIR_TABLE[0] * 10.0 * EPS;
			polls[i * 4 + 1] = lc::Point(x, y) + DIR_TABLE[1] * 10.0 * EPS;
			polls[i * 4 + 2] = lc::Point(x, y) + DIR_TABLE[2] * 10.0 * EPS;
			polls[i * 4 + 3] = lc::Point(x, y) + DIR_TABLE[3] * 10.0 * EPS;
		}
		while(true){
			bool modified = false;
			segments.erase(unique(
				segments.begin(), segments.end()), segments.end());
			vector<lc::Point> next;
			next.clear();
			for(size_t i = 0; i < segments.size(); ++i){
				next.push_back(segments[i]);
				if(i + 2 >= segments.size()){ continue; }
				if((segments[i + 2] - segments[i]).abs() < 2.0 * EPS){ continue; }
				lc::Polygon tri({
					segments[i], segments[i + 1], segments[i + 2]
				});
				for(size_t j = 0; j < polls.size(); ++j){
					const auto &p = polls[j];
					if(tri[1] == p){ tri[1] += DIR_TABLE[j % 4] * EPS; }
				}
				vector<lc::Point> pts({ segments[i], segments[i + 2] });
				for(size_t j = 0; j < polls.size(); ++j){
					const auto &p = polls[j];
					const int contains = tri.contains(p);
					if(contains > 0){
						pts.push_back(p);
					}else if(contains == 0){
						const auto &dir = DIR_TABLE[j % 4];
						const auto proj = lc::Line(
							segments[i], segments[i + 2]).projection(p);
						if(lc::dot(proj - p, dir) < 0.0){ pts.push_back(p); }
					}
				}
				const lc::Polygon conv = convex_hull(pts);
				int locs[3] = { -1, -1, -1 };
				for(int j = 0; j < conv.size(); ++j){
					for(int k = 0; k < 3; ++k){
						if(segments[i + k] == conv[j]){ locs[k] = j; }
					}
				}
				if(locs[1] < 0){
					const int t = conv.size();
					const int d = ((locs[0] + 1) % t == locs[2]) ? -1 : 1;
					for(int j = locs[0]; j != locs[2]; j = (j + d + t) % t){
						next.push_back(conv[j]);
					}
					modified = true;
					for(size_t j = i + 2; j < segments.size(); ++j){
						next.push_back(segments[j]);
					}
					break;
				}else{
					next.push_back(segments[i]);
				}
			}
			if(!modified){ break; }
			segments.swap(next);
		}
		double answer = 0.0;
		for(size_t i = 0; i + 1 < segments.size(); ++i){
			answer += (segments[i + 1] - segments[i]).abs();
		}
		cout << answer << endl;
	}
	return 0;
}