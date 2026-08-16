#include <bits/stdc++.h>
using namespace std;
template <class T>
inline T sqr(T x) {
  return x * x;
}
const double EPS = 1e-6;
const int INF = 0x3fffffff;
const long long LINF = INF * 1ll * INF;
const double PI = acos(-1.0);
using namespace std;
int sign(double x) { return x < -EPS ? -1 : x > EPS; }
struct Point {
  double x, y;
  Point(double x, double y) : x(x), y(y) {}
  Point() {}
  bool operator==(const Point& p) const {
    return sign(x - p.x) == 0 && sign(y - p.y) == 0;
  }
  Point operator-(const Point& p) const { return Point(x - p.x, y - p.y); }
  Point operator*(const double t) const { return Point(t * x, t * y); }
  Point operator+(const Point& p) const { return Point(x + p.x, y + p.y); }
  bool operator<(const Point& p) const {
    return sign(x - p.x) == 0 ? sign(y - p.y) < 0 : sign(x - p.x) < 0;
  }
};
struct Line {
  Point a, b;
  Line() {}
  Line(Point a, Point b) : a(a), b(b) {}
};
inline double Length(Point a, Point b) {
  double x = a.x - b.x, y = a.y - b.y;
  return sqrt(x * x + y * y);
}
inline double Cross(Point a, Point b) { return a.x * b.y - a.y * b.x; }
inline double Dot(Point a, Point b) { return a.x * b.x + a.y * b.y; }
Point Rotate(Point A, double rad) {
  return Point(A.x * cos(rad) - A.y * sin(rad),
               A.x * sin(rad) + A.y * cos(rad));
}
inline Point LineInterSection(Line l1, Line l2) {
  Point u = l1.a - l2.a;
  Point v1 = l1.b - l1.a, v2 = l2.b - l2.a;
  if (sign(Cross(v1, v2)) == 0) {
    if (sign(Cross(u, v1)))
      return Point(-INF, -INF);
    else
      return Point(-INF, -INF);
  }
  double t = Cross(v2, u) / Cross(v1, v2);
  return l1.a + v1 * t;
}
struct Light {
  double x, y, ang;
} light[22];
double dp[1 << 20];
int main(void) {
  int n;
  double l, r;
  cin >> n >> l >> r;
  for (int i = 0; i < n; i++) {
    cin >> light[i].x >> light[i].y >> light[i].ang;
    light[i].ang *= PI;
    light[i].ang /= 180;
  }
  for (int i = 0; i < (1 << n); i++) dp[i] = -INF;
  dp[0] = l;
  for (int i = 0; i < (1 << n); i++) {
    if (sign(dp[i] + INF) == 0) continue;
    for (int j = 0; j < n; j++) {
      if (i & (1 << j)) continue;
      dp[i | (1 << j)] = max(dp[i | (1 << j)], dp[i]);
      Point p(light[j].x, light[j].y);
      Point v1 = Point(dp[i], 0) - p;
      v1 = Rotate(v1, light[j].ang);
      double ret;
      if (sign(Cross(Point(1, 0), v1)) >= 0) {
        ret = r;
      } else {
        Point inter =
            LineInterSection(Line(v1 + p, p), Line(Point(1, 0), Point(-1, 0)));
        ret = min(r, inter.x);
      }
      dp[i | (1 << j)] = max(dp[i | (1 << j)], ret);
    }
  }
  if (sign(dp[(1 << n) - 1] + INF) == 0) dp[(1 << n) - 1] = l;
  printf("%.10lf\n", dp[(1 << n) - 1] - dp[0]);
}
