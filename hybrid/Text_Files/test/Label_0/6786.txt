#include<bits/stdc++.h>
 
using namespace std;
 
const double EPS = 1e-8, PI = acos(-1);
 
inline bool eq(double a, double b)
{
  return abs(b - a) < EPS;
}
 
#define curr(P, i) P[i]
#define next(P, i) P[(i+1)%P.size()]
#define prev(P, i) P[(i+P.size()-1) % P.size()]
enum { OUT, ON, IN };
namespace Geometory
{
  struct Point
  {
    double x, y;
 
    Point()
    {
    };
 
    Point(double x, double y) : x(x), y(y)
    {
    };
 
    Point operator+(const Point& b) const
    {
      return Point(x + b.x, y + b.y);
    }
 
    Point operator-(const Point& b) const
    {
      return Point(x - b.x, y - b.y);
    }
 
    Point operator*(const double b) const
    {
      return Point(x * b, y * b);
    }
 
    Point operator*(const Point& b) const
    {
      return Point(x * b.x - y * b.y, x * b.y + y * b.x);
    }
 
    Point operator/(const double b) const
    {
      return Point(x / b, y / b);
    }
 
    bool operator<(const Point& b) const
    {
      return x != b.x ? x < b.x : y < b.y;
    }
 
    bool operator==(const Point& b) const
    {
      return eq(x, b.x) && eq(y, b.y);
    }
 
    double norm()
    {
      return x * x + y * y;
    }
 
    double arg()
    {
      return atan2(x, y);
    }
 
    double abs()
    {
      return sqrt(norm());
    }
 
    Point rotate(double theta)
    {
      return Point(cos(theta) * x - sin(theta) * y, sin(theta) * x + cos(theta) * y);
    }
 
    Point rotate90()
    {
      return Point(-y, x);
    }
 
    friend ostream& operator<<(ostream& os, Point& p)
    {
      return os << "(" << p.x << "," << p.y << ")";
    }
 
    friend istream& operator>>(istream& is, Point& a)
    {
      return is >> a.x >> a.y;
    }
  };
 
  struct Line
  {
    Point a, b;
 
    Line()
    {
    };
 
    Line(Point a, Point b) : a(a), b(b)
    {
    };
 
    friend ostream& operator<<(ostream& os, Line& p)
    {
      return os << "(" << p.a.x << "," << p.a.y << ") to (" << p.b.x << "," << p.b.y << ")";
    }
 
    friend istream& operator>>(istream& is, Line& a)
    {
      return is >> a.a.x >> a.a.y >> a.b.x >> a.b.y;
    }
  };
 
  struct Segment
  {
    Point a, b;
 
    Segment()
    {
    };
 
    Segment(Point a, Point b) : a(a), b(b)
    {
    };
 
    friend ostream& operator<<(ostream& os, Segment& p)
    {
      return os << "(" << p.a.x << "," << p.a.y << ") to (" << p.b.x << "," << p.b.y << ")";
    }
 
    friend istream& operator>>(istream& is, Segment& a)
    {
      return is >> a.a.x >> a.a.y >> a.b.x >> a.b.y;
    }
  };
 
  typedef vector< Point > Polygon;
  typedef vector< Segment > Segments;
  typedef vector< Line > Lines;
  typedef pair< Point, Point > PointPoint;
 
  double cross(const Point& a, const Point& b)
  {
    return a.x * b.y - a.y * b.x;
  }
 
  double dot(const Point& a, const Point& b)
  {
    return a.x * b.x + a.y * b.y;
  }
 
  int ccw(const Point& a, Point b, Point c)
  {
    b = b - a, c = c - a;
    if(cross(b, c) > EPS) return +1;  // a ??? b ???§ ????????¨??????????????????? c
    if(cross(b, c) < -EPS) return -1; // a ??? b ???§ ?????¨??????????????????? c
    if(dot(b, c) < 0) return +2;  // c -- a -- b???§??????´??????
    if(b.norm() < c.norm()) return -2; // a -- b -- c???§??????´??????
    return 0;  // a -- c -- b???§??????´??????
  }
 
  Point Projection(const Line& l, const Point& p)
  {
    double t = dot(p - l.a, l.a - l.b) / (l.a - l.b).norm();
    return l.a + (l.a - l.b) * t;
  }
 
  Point Projection(const Segment& l, const Point& p)
  {
    double t = dot(p - l.a, l.a - l.b) / (l.a - l.b).norm();
    return l.a + (l.a - l.b) * t;
  }
 
  Point Reflection(const Line& l, const Point& p)
  {
    return p + (Projection(l, p) - p) * 2.0;
  }
 
  double Distance(const Line& l, const Point& p)
  { //OK
    return (p - Projection(l, p)).abs();
  }
 
  bool Intersect(const Line& l, const Line& m)
  {
    return abs(cross(l.b - l.a, m.b - m.a)) > EPS || abs(cross(l.b - l.a, m.b - l.a)) < EPS;
  }
 
  bool Intersect(const Line& l, const Segment& s)
  {
    return cross(l.b - l.a, s.a - l.a) * cross(l.b - l.a, s.b - l.a) < EPS;
  }
 
  bool Intersect(const Line& l, const Point& p)
  {
    return abs(ccw(l.a, l.b, p)) != -1;
  }
 
  bool Intersect(const Segment& s, const Segment& t)
  {
    return ccw(s.a, s.b, t.a) * ccw(s.a, s.b, t.b) <= 0 && ccw(t.a, t.b, s.a) * ccw(t.a, t.b, s.b) <= 0;
  }
 
  bool Intersect(const Segment& s, const Point& p)
  {
    return ccw(s.a, s.b, p) == 0;
  }
 
  Point Crosspoint(const Segment& l, const Segment& m)
  { //OK
    double A = cross(l.b - l.a, m.b - m.a);
    double B = cross(l.b - l.a, l.b - m.a);
    if(abs(A) < EPS && abs(B) < EPS) return m.a; // same line
    return m.a + (m.b - m.a) * B / A;
  }
 
  Point Crosspoint(const Line& l, const Line& m)
  { //OK
    double A = cross(l.b - l.a, m.b - m.a);
    double B = cross(l.b - l.a, l.b - m.a);
    if(abs(A) < EPS && abs(B) < EPS) return m.a;
    return m.a + (m.b - m.a) * B / A;
  }
};
 
int main()
{
  int N, M;
 
  cin >> N >> M;
 
  vector< Geometory::Polygon > polygons(N);
  for(int i = 0; i < N; i++) {
    int L;
    cin >> L;
    polygons[i].resize(L);
    for(int j = 0; j < L; j++) {
      cin >> polygons[i][j];
    }
  }
 
  vector< Geometory::Point > points(M);
  for(int i = 0; i < M; i++) {
    cin >> points[i];
  }
 
  vector< Geometory::Line > lines;
  for(int i = 0; i < M; ++i) {
    for(int j = 0; j < N; ++j) {
      for(int l = 0; l < polygons[j].size(); ++l) {
        lines.emplace_back(Geometory::Line(points[i], polygons[j][l]));
      }
    }
  }
 
  int ret = 1;
  for(int i = 0; i < lines.size(); ++i) {
    for(int j = 0; j < i; ++j) {
      if(Geometory::Intersect(lines[i], lines[j])) {
        auto pp = Geometory::Crosspoint(lines[i], lines[j]);
        int cost = 0;
        for(int m = 0; m < M; m++) {
          auto seg = Geometory::Segment(pp, points[m]);
          bool iscross = false;
          for(int n = 0; n < N; n++) {
            for(int o = 0; o < polygons[n].size(); o++) {
              if(Geometory::Intersect(Geometory::Segment(curr(polygons[n], o), next(polygons[n], o)), seg)) {
                auto qq = Geometory::Crosspoint(Geometory::Segment(curr(polygons[n], o), next(polygons[n], o)), seg);
                if(curr(polygons[n], o) == qq) continue;
                if(next(polygons[n], o) == qq) continue;
                if(seg.a == qq || seg.b == qq) continue;
                iscross = true;
              }
            }
          }
          cost += iscross ^ 1;
        }
        ret = max(ret, cost);
      }
    }
  }
 
  cout << ret << endl;
}