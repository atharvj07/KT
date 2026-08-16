#include <bits/stdc++.h>

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define reps(i, f, n) for(int i = (int)(f); i < (int)(n); i++)

typedef pair<double, int> P;

const double inf = 1e9;

#define EPS (1e-10)
#define equals(a, b) (fabs((a)-(b)) < EPS)
#define lt(a, b) ((a) - (b) < -EPS)

// ???/????????????
struct Point {
  double x, y;
  Point(double x = 0.0, double y = 0.0):x(x), y(y){}
  
  Point operator + (Point p) { return Point(x + p.x, y + p.y); }
  Point operator - (Point p) { return Point(x - p.x, y - p.y); }
  Point operator * (double a) { return Point(x * a, y * a); }
  Point operator / (double a) { return Point(x / a, y / a); }

  double abs() { return sqrt(norm()); }
  double norm() { return x*x + y*y; }

  bool operator < (const Point& p) const {
    return x != p.x ? x < p.x : y < p.y;
  }
  bool operator == (const Point& p) const {
    return fabs(x - p.x) < EPS && fabs(y - p.y) < EPS;
  }
};
typedef Point Vector;

// ???
struct Circle {
  Point c;
  double r;
  Circle(Point c = Point(), double r = 0.0):c(c), r(r){}
};

// ????§???¢
typedef vector<Point> Polygon;

// ??????/??´???
struct Segment {
  Point p1, p2;
  Segment(Point p1 = Point(), Point p2 = Point()):p1(p1), p2(p2){}  
};
typedef Segment Line;

// ????????????????????????
double norm(Vector v)
{
  return v.x*v.x + v.y*v.y;
}
// ?????????????????§??????
double abs(Vector v)
{
  return sqrt(norm(v));
}
// ?????????????????????
double dot(Vector a, Vector b)
{
  return a.x*b.x + a.y*b.y;
}
// ??????????????????????????§??????
double cross(Vector a, Vector b)
{
  return a.x*b.y - a.y*b.x;
}
// ??´?????????
bool isOrthogonal(Vector a, Vector b)
{
  return equals(dot(a, b), 0.0);
}
bool isOrthogonal(Point a1, Point a2, Point b1, Point b2)
{
  return isOrthogonal(a1 - a2, b1 - b2);
}
bool isOrthogonal(Segment s1, Segment s2)
{
  return equals(dot(s1.p2 - s1.p1, s2.p2 - s2.p1), 0.0);
}
// ????????????
bool isParallel(Vector a, Vector b)
{
  return equals(cross(a, b), 0.0);
}
bool isParallel(Point a1, Point a2, Point b1, Point b2)
{
  return isParallel(a1 - a2, b1 - b2);
}
bool isParallel(Segment s1, Segment s2)
{
  return equals(cross(s1.p2 - s1.p1, s2.p2 - s2.p1), 0.0);
}
// ?°???±
Point project(Segment s, Point p)
{
  Vector base = s.p2 - s.p1;
  double r = dot(p - s.p1, base) / norm(base);
  return s.p1 + base * r;
}
// ????°?
Point reflect(Segment s, Point p)
{
  return p + (project(s, p) - p) * 2.0;
}
static const int COUNTER_CLOCKWISE = 1;
static const int CLOCKWISE         = -1;
static const int ONLINE_BACK       = 2;
static const int ONLINE_FRONT      = -2;
static const int ON_SEGMENT        = 0;
// ???????¨???????
int ccw(Point p0, Point p1, Point p2)
{
  Vector a = p1 - p0;
  Vector b = p2 - p0;
  if(cross(a, b) > EPS) return COUNTER_CLOCKWISE;
  if(cross(a, b) < -EPS) return CLOCKWISE;
  if(dot(a, b) < -EPS) return ONLINE_BACK;
  if(a.norm() < b.norm()) return ONLINE_FRONT;
  return ON_SEGMENT;
}
// ????????????
bool intersect(Point p1, Point p2, Point p3, Point p4)
{
  return (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 &&
	  ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0);
}
bool intersect(Segment s1, Segment s2)
{
  return intersect(s1.p1, s1.p2, s2.p1, s2.p2);
}
// ?????????????????¢
double getDistance(Point a, Point b)
{
  return abs(a - b);
}
// ??´?????¨?????¨????????¢
double getDistanceLP(Line l, Point p)
{
  return abs(cross(l.p2 - l.p1, p - l.p1) / abs(l.p2 - l.p1));
}
// ????????¨?????¨????????¢
double getDistanceSP(Segment s, Point p)
{
  if(dot(s.p2 - s.p1, p - s.p1) < 0.0) return abs(p - s.p1);
  if(dot(s.p1 - s.p2, p - s.p2) < 0.0) return abs(p - s.p2);
  return getDistanceLP(s, p);
}
// ????????????????????¢
double getDistance(Segment s1, Segment s2)
{
  if(intersect(s1, s2)) return 0.0;
  return min(min(getDistanceSP(s1, s2.p1), getDistanceSP(s1, s2.p2)),
	     min(getDistanceSP(s2, s1.p1), getDistanceSP(s2, s1.p2)));
}
// ???????????????
Point getCrossPoint(Segment s1, Segment s2)
{
  Vector base = s2.p2 - s2.p1;
  double d1 = abs(cross(base, s1.p1 - s2.p1));
  double d2 = abs(cross(base, s1.p2 - s2.p1));
  double t = d1 / (d1 + d2);
  return s1.p1 + (s1.p2 - s1.p1) * t;
}
Point getCrossPointLL(Line l1, Line l2)
{
  Vector v1 = l1.p2 - l1.p1, v2 = l2.p2 - l2.p1;
  double d = cross(v2, v1);
  if(abs(d) < EPS) return l2.p1;
  return l1.p1 + v1 * cross(v2, l2.p2 - l1.p1) * (1.0 / d);
}

// ???????????????????????¢??¬?????????????????????????????????
bool mergeIfAble(Segment &s1, Segment s2)
{
  if(abs(cross(s1.p2 - s1.p1, s2.p2 - s2.p1)) > EPS) return false;
  if(ccw(s1.p1, s2.p1, s1.p2) == COUNTER_CLOCKWISE ||
     ccw(s1.p1, s2.p1, s1.p2) == CLOCKWISE) return false;
  if(ccw(s1.p1, s1.p2, s2.p1) == ONLINE_FRONT ||
     ccw(s2.p1, s2.p2, s1.p1) == ONLINE_FRONT) return false;
  s1 = Segment(min(s1.p1, s2.p1), max(s1.p2, s2.p2));
  return true;
}
void mergeSegments(vector<Segment>& segs)
{
  for(int i = 0; i < segs.size(); i++) {
    if(segs[i].p2 < segs[i].p1) swap(segs[i].p1, segs[i].p2);
  }
  for(int i = 0; i < segs.size(); i++) {
    for(int j = i+1; j < segs.size(); j++) {
      if(mergeIfAble(segs[i], segs[j])) {
	segs[j--] = segs.back(), segs.pop_back();
      }
    }
  }
}

// ????????¢??¬???????????????
struct edge
{
  int to;
  double cost;
  edge(){}
  edge(int to, double cost):to(to), cost(cost){}

  bool operator < (const edge& e) const {
    return lt(cost, e.cost);
  }
};
typedef vector< vector<edge> > Graph;

Graph segmentArrangement(vector<Segment>& segs, vector<Point>& ps)
{
  for(int i = 0; i < segs.size(); i++) {
    ps.push_back(segs[i].p1);
    ps.push_back(segs[i].p2);
    for(int j = i+1; j < segs.size(); j++) {
      if(intersect(segs[i], segs[j])) ps.push_back(getCrossPoint(segs[i], segs[j]));
    }
  }
  sort(ps.begin(), ps.end());
  ps.erase(unique(ps.begin(), ps.end()), ps.end());
  Graph graph(ps.size());
  for(int i = 0; i < segs.size(); i++) {
    vector< pair<double, int> > ls;
    for(int j = 0; j < ps.size(); j++) {
      if(intersect(segs[i], ps[j])) {
	ls.emplace_back(getDistanceSP(segs[i], ps[j]), j);
      }
    }
    sort(ls.begin(), ls.end());
    for(int j = 0; j+1 < ls.size(); j++) {
      int u = ls[j].second, v = ls[j+1].second;
      graph[u].emplace_back(v, getDistance(ps[u], ps[v]));
      graph[v].emplace_back(u, getDistance(ps[u], ps[v]));
    }
  }
  return graph;
}

double dijkstra(vector<Point> p, Point a, Point b)
{
  priority_queue<P, vector<P>, greater<P> > que;
  vector<double> mincost(p.size(), inf);  
  que.push(P(0.0, 0));
  mincost[0] = 0.0;
  while(!que.empty()) {
    double c; int now;
    tie(c, now) = que.top(); que.pop();
    if(now == 1) return c + getDistance(a, b);
    if(mincost[now] < c) continue;
    for(int i = 0; i < p.size(); i++) {
      if(intersect(p[now], p[i], a, b)) continue;
      if(getDistance(p[now], p[i]) + c < mincost[i]) {
	mincost[i] = getDistance(p[now], p[i]) + c;
	que.push(P(mincost[i], i));
      }
    }
  }
  return inf;
}

signed main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(12);

  int Na, Nb;
  cin >> Na >> Nb;
  vector<Point> pa(Na), pb(Nb);
  rep(i, Na) cin >> pa[i].x >> pa[i].y;
  rep(i, Nb) cin >> pb[i].x >> pb[i].y;

  double a_st = dijkstra(pb, pa[0], pa[1]);
  double b_st = dijkstra(pa, pb[0], pb[1]);

  if(a_st != inf || b_st != inf) cout << min(a_st, b_st) << endl;
  else cout << -1 << endl;
  
  return 0;
}