#include<bits/stdc++.h>
#define EPS (1e-10)
#define equals(a,b)(fabs((a)-(b))<EPS)
#define rep(i,n)for(int i=0;i<n;i++)
using namespace std;

struct Point {
	double x, y;
	Point(double x = 0, double y = 0) :x(x), y(y) {}
	Point operator*(double a) { return Point(a*x, a*y); }
	Point operator-(Point p) { return Point(x - p.x, y - p.y); }
	Point operator+(Point p) { return Point(x + p.x, y + p.y); }
	double norm() { return x*x + y*y; }
};
typedef Point Vector;
typedef vector<Point>Polygon;
struct Segment {
	Point p1, p2;
};
double cross(Point a, Point b) {
	return a.x*b.y - a.y*b.x;
}
double dot(Point a, Point b) {
	return a.x*b.x + a.y*b.y;
}
bool isPrallel(Segment s1, Segment s2) {
	return equals(cross(s1.p2 - s1.p1, s2.p2 - s2.p1), 0.0);
}
bool isOrthogonal(Segment s1, Segment s2) {
	return equals(dot(s1.p2 - s1.p1, s2.p2 - s2.p1), 0.0);
}
int contains(Polygon g, Point p) {
	int n = g.size();
	bool x = false;
	rep(i, n) {
		Point a = g[i] - p, b = g[(i + 1) % n] - p;
		if (abs(cross(a, b)) < EPS&&dot(a, b) < EPS)return 1;
		if (a.y > b.y)swap(a, b);
		if (a.y < EPS&&EPS<b.y&&cross(a, b)>EPS)x = !x;
	}
	return x ? 2 : 0;
}
int ccw(Point p0, Point p1, Point p2) {
	Point a = p1 - p0;
	Point b = p2 - p0;
	if (cross(a, b) > EPS)return 1;
	if (cross(a, b) < -EPS)return -1;
	if (dot(a, b) < -EPS)return 2;
	if (a.norm() < b.norm())return -2;
	return 0;
}
bool intersect(Point p1, Point p2, Point p3, Point p4) {
	return (ccw(p1, p2, p3)*ccw(p1, p2, p4) <= 0 &&
		ccw(p3, p4, p1)*ccw(p3, p4, p2) <= 0);
}
bool intersect(Segment s1, Segment s2) {
	return intersect(s1.p1, s1.p2, s2.p1, s2.p2);
}
Point project(Segment s, Point p) {
	Point base = s.p2 - s.p1;
	double r = dot(p - s.p1, base) / base.norm();
	return s.p1 + base*r;
}
Point reflect(Segment s, Point p) {
	return p + (project(s, p) - p)*2.0;
}
bool isconvex(Polygon g) {
	int back = 3;
	rep(i, g.size()) {
		int d = ccw(g[(i + g.size() - 1) % g.size()], g[i], g[(i + 1) % g.size()]);
		if (back != 3 && d != back)
			return false;
		else back = d;
	}
	return true;
}
double area(Polygon g) {
	double cnt = 0;
	rep(i, g.size())
		cnt += g[i].x*g[(i + 1) % g.size()].y - g[(i + 1) % g.size()].x*g[i].y;
	return abs(cnt) / 2;
}
int main() {
	int n; scanf("%d", &n);
	rep(i, n) {
		double xp1, yp1, xp2, yp2, xp3, yp3, xk, yk, xs, ys;
		cin >> xp1 >> yp1 >> xp2 >> yp2 >> xp3 >> yp3 >> xk >> yk >> xs >> ys;
		Point a(xp1, yp1), b(xp2, yp2), c(xp3, yp3), k(xk, yk), s(xs, ys);
		Vector AB = b - a, BP = k - b, BC = c - b, CP = k - c, CA = a - c, AP = k - a;
		bool flag = false;
		double c1 = cross(CA, AP), c2 = cross(BC, CP), c3 = cross(AB, BP);
		if ((c1 > 0 && c2 > 0 && c3 > 0) || (c1 < 0 && c2 < 0 && c3 < 0))flag = true;
		BP = s - b, CP = s - c, AP = s - a;
		c1 = cross(CA, AP), c2 = cross(BC, CP), c3 = cross(AB, BP);
		if ((c1 > 0 && c2 > 0 && c3 > 0) || (c1 < 0 && c2 < 0 && c3 < 0))flag ^= true;
		puts(flag ? "OK" : "NG");
	}
}