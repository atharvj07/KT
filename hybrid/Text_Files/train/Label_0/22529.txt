#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <bitset>

using namespace std;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define MEMSET(v, h) memset((v), h, sizeof(v))

template <class T>
ostream &operator<<(ostream &os, const vector<T> &rhs) {
  os << "[ ";
  FORIT(it, rhs) {
    if (it != rhs.begin()) { os << ", "; }
    os << *it;
  }
  os << " ]";
  return os;
}

typedef int Weight;
struct Edge {
  int src;
  int dest;
  Weight weight;
  Edge(int src, int dest, Weight weight) : src(src), dest(dest), weight(weight) {;}
  bool operator<(const Edge &rhs) const {
    if (weight != rhs.weight) { return weight > rhs.weight; }
    if (src != rhs.src) { return src < rhs.src; }
    return dest < rhs.dest;
  }
};
typedef vector<Edge> Edges;
typedef vector<Edges> Graph;

#include <complex>

typedef complex<double> Point;
typedef vector<Point> Polygon;

static const double INF = 1e+10;

#define CURR(P, i) (P[i])
#define NEXT(P, i) (P[(i + 1) % P.size()])

struct Line : public vector<Point> {
  Line() {;}
  Line(Point a, Point b) { push_back(a); push_back(b); }
};

struct Circle {
  Point p;
  double r;
  Circle() {;}
  Circle(Point p, double r) : p(p), r(r) {;}
};

namespace std {
  bool operator<(const Point &lhs, const Point &rhs) {
    return lhs.real() == rhs.real() ? lhs.imag() < rhs.imag() : lhs.real() < rhs.real();
  }
}

inline double cross(const Point &a, const Point &b) {
  return imag(conj(a) * b);
}

inline double dot(const Point &a, const Point &b) {
  return real(conj(a) * b);
}

inline int ccw(Point a, Point b, Point c) {
  b -= a;
  c -= a;
  if (cross(b, c) > 0) { return 1; }
  if (cross(b, c) < 0) { return -1; }
  if (dot(b, c) < 0) { return 2; }
  if (norm(b) < norm(c)) { return -2; }
  return 0;
}

enum { OUT, ON, IN };
int Contains(const Polygon& P, const Point& p) {
  bool in = false;
  for (int i = 0; i < (int)P.size(); ++i) {
    Point a = CURR(P,i) - p, b = NEXT(P,i) - p;
    if (imag(a) > imag(b)) swap(a, b);
    if (imag(a) <= 0 && 0 < imag(b))
      if (cross(a, b) < 0) in = !in;
    if (cross(a, b) == 0 && dot(a, b) <= 0) return ON;
  }
  return in ? IN : OUT;
}


double Area(const Polygon &p) {
  double ret = 0;
  for (int i = 0; i < (int)p.size(); i++) {
    ret += cross(CURR(p, i), NEXT(p, i));
  }
  return ret / 2.0;
}

// Need Area
struct Angle {
  double rad;
  int src;
  int src_e;
  int dest;
  Angle() {;}
  Angle(double rad, int src, int src_e, int dest) : rad(rad), src(src), src_e(src_e), dest(dest) {;}
  bool operator<(const Angle &rhs) const {
    return rad < rhs.rad;
  }
};
vector<Polygon> PlainGraphToPolygon(const Graph &g, const vector<Point> &ps, bool remove_2edge = true, bool remove_clockwize = true) {
  const int n = g.size();
  assert((int)ps.size() == n);
  vector<vector<char> > visit(n);
  vector<vector<Angle> > angles(n);
  REP(from, n) {
    visit[from] = vector<char>(g[from].size(), false);
    int index = 0;
    FORIT(it, g[from]) {
      int to = it->dest;
      double rad = arg(ps[to] - ps[from]);
      angles[from].push_back(Angle(rad, from, index, to));
      angles[from].push_back(Angle(rad + 2 * PI, from, index, to));
      index++;
    }
    sort(angles[from].begin(), angles[from].end());
  }

  vector<Polygon> ret;
  REP(start_node, n) {
    REP(start_edge, g[start_node].size()) {
      if (visit[start_node][start_edge]) { continue; }
      Polygon poly;
      Edge e = g[start_node][start_edge];
      double rad = arg(ps[e.dest] - ps[e.src]);
      Angle angle(rad, start_node, start_edge, e.dest);
      while (true) {
        int from = angle.dest;
        angle.rad += PI + EPS;
        while (angle.rad > PI) { angle.rad -= 2 * PI; }
        angle = *upper_bound(angles[from].begin(), angles[from].end(), angle);
        if (visit[angle.src][angle.src_e]) { break; }
        visit[angle.src][angle.src_e] = 1;
        poly.push_back(ps[from]);
      }
      if (remove_2edge && poly.size() == 2) { continue; }
      if (remove_clockwize && Area(poly) > 0) { continue; }
      ret.push_back(poly);
    }
  }
  return ret;
}


//==================================================
void OutputSVGHeader(FILE *fp, double minx, double miny, double maxx, double maxy) {
  double w = (maxx - minx + 2);
  double h = (maxy - miny + 2);
  fprintf(fp, "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n");
  fprintf(fp, "<svg width=\"20cm\" height=\"20cm\" viewBox=\"%.3lf %3.lf %.3lf %.3lf\"\n", minx - 1, miny - 1 , w, h);
  fprintf(fp, "  xmlns=\"http://www.w3.org/2000/svg\"\n");
  fprintf(fp, "  xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n");
}
void OutputSVGFooter(FILE *fp) {
  fprintf(fp, "</svg>\n");
}
void OutputSVGPolygon(FILE *fp, const Polygon &poly, int color = -1) {
  const int n = poly.size();
  char color_name[100];
  if (color == -1) {
    snprintf(color_name, 99, "none");
  } else {
    int c1 = (color >> 0)  & 0xff;
    int c2 = (color >> 8)  & 0xff;
    int c3 = (color >> 16) & 0xff;
    snprintf(color_name, 99, "#%02x%02x%02x", c1, c2, c3);
  }
  fprintf(fp, "<polygon fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.300\" points=\"", color_name);
  REP(i, n) {
    fprintf(fp, "%.3lf,%.3lf ", poly[i].real(), poly[i].imag());
  }
  fprintf(fp, "\"/>\n");
}
void OutputSVGCircle(FILE *fp, const Circle &circle, int color = -1) {
  char color_name[100];
  if (color == -1) {
    snprintf(color_name, 99, "none");
  } else {
    int c1 = (color >> 0)  & 0xff;
    int c2 = (color >> 8)  & 0xff;
    int c3 = (color >> 16) & 0xff;
    snprintf(color_name, 99, "#%02x%02x%02x", c1, c2, c3);
  }
  fprintf(fp, "<circle cx=\"%lf\" cy=\"%lf\" r=\"%lf\" fill=\"%s\" stroke=\"#000000\" stroke-width=\"0.050\"/>\n", circle.p.real(), circle.p.imag(), circle.r, color_name);
}
//==================================================



int n, m;
Circle circles[200];
Point srcs[100];
Point dests[100];

void OutputSVG(const vector<Polygon> &polys) {
  FILE *fp = fopen("out.svg", "w");
  OutputSVGHeader(fp, -100, -100, 100, 100);
  REP(i, n) {
    Circle c = circles[i];
    c.p /= 100.0;
    c.r /= 100.0;
    OutputSVGCircle(fp, c, 0x00ff0000);
  }
  FORIT(it, polys) {
    Polygon poly = *it;
    FORIT(it2, poly) { *it2 /= 100.0; }
    OutputSVGPolygon(fp, poly);
  }
  REP(i, m) {
    Circle c1 = Circle(srcs[i] / 100.0, 1);
    Circle c2 = Circle(dests[i] / 100.0, 1);
    OutputSVGCircle(fp, c1, 0x0000ff00);
    OutputSVGCircle(fp, c2, 0x000000ff);
  }
  OutputSVGFooter(fp);
  fclose(fp);
}

int main() {
  while (scanf("%d %d", &n, &m) > 0 && n && m) {
    Graph g(n);
    vector<Point> ps(n);
    REP(i, n) {
      double x, y, r;
      scanf("%lf %lf %lf", &x, &y, &r);
      circles[i] = Circle(Point(x, y), r);
      ps[i] = Point(x, y);
    }
    REP(i, m) {
      double sx, sy, ex, ey;
      scanf("%lf %lf %lf %lf", &sx, &sy, &ex, &ey);
      srcs[i] = Point(sx, sy);
      dests[i] = Point(ex, ey);
    }

    REP(i, n) {
      FOR(j, i + 1, n) {
        const Circle &c1 = circles[i];
        const Circle &c2 = circles[j];
        double d = abs(c1.p - c2.p);
        if (max(c1.r, c2.r) - min(c1.r, c2.r) > d) { continue; }
        if (c1.r + c2.r < d) { continue; }
        g[i].push_back(Edge(i, j, 0));
        g[j].push_back(Edge(j, i, 0));
      }
    }
    vector<Polygon> polys = PlainGraphToPolygon(g, ps);
    // cout << polys << endl;
    vector<string> anss;
    REP(i, m) {
      bitset<100> in_circles[2];
      bitset<10000> in_polys[2];
      assert(polys.size() < 10000);
      Point points[2] = { srcs[i], dests[i] };
      REP(iter, 2) {
        REP(i, n) {
          int v = (abs(circles[i].p - points[iter]) < circles[i].r) ? 1 : 0;
          in_circles[iter].set(i, v);
        }
        REP(i, polys.size()) {
          int v = Contains(polys[i], points[iter]) == IN ? 1 : 0;
          in_polys[iter].set(i, v);
        }
      }
      // cout << in_circles[0] << " " << in_circles[1] << endl;
      // cout << in_polys[0] << " " << in_polys[1] << endl;
      // cout << endl;
      if ((in_circles[0].any() && in_circles[1].any() && in_circles[0] == in_circles[1]) ||
          (!in_circles[0].any() && !in_circles[1].any() && in_polys[0] == in_polys[1])) {
        anss.push_back("YES");
      } else {
        anss.push_back("NO");
      }
    }

    REP(i, m) {
      printf("%s%s", anss[i].c_str(), i != m - 1 ? " " : "\n");
    }
    // OutputSVG(polys);
  }
}