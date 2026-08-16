#include <iostream>
#include <vector>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <functional>
#include <ctime>
#include <numeric>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define fst first
#define snd second
#define all(c) ((c).begin()), ((c).end())


const double EPS = 1e-8;
int sign(double x) {
  if (x < -EPS) return -1;
  if (x > +EPS) return +1;
  return 0;
}
struct point {
  typedef double T;
  T x, y; 
  point &operator+=(point p) { x += p.x; y += p.y; return *this; }
  point &operator-=(point p) { x -= p.x; y -= p.y; return *this; }
  point &operator*=(T a)     { x *= a;   y *= a;   return *this; }
  point &operator/=(T a)     { return *this *= (1.0/a); }
  point operator-() const    { return {-x, -y}; }
  bool operator<(point p) const { 
    int s = sign(x - p.x);
    return s ? s < 0 : sign(y - p.y) < 0;
  }
};
bool operator==(point p, point q) { return !(p < q) && !(q < p); }
point operator+(point p, point q) { return p += q; }
point operator-(point p, point q) { return p -= q; }
point operator*(point::T a, point p) { return p *= a; }
point operator*(point p, point::T a) { return p *= a; }
point operator/(point p, point::T a) { return p /= a; }
point::T dot(point p, point q) { return p.x*q.x+p.y*q.y; }
point::T cross(point p, point q) { return p.x*q.y-p.y*q.x; } // left turn > 0
point::T norm2(point p) { return dot(p,p); }
point orth(point p) { return {-p.y, p.x}; }
point::T norm(point p) { return sqrt(dot(p,p)); }
point::T arg(point p) { return atan2(p.y, p.x); }

struct line { point p, q; };
typedef vector<point> polygon;

polygon convex_cut(polygon ps, line l) {
  vector<point> qs;
  for (int i = 0; i < ps.size(); ++i) {
    int j = (i+1 == ps.size() ? 0 : i+1);
    if (sign(cross(l.p - ps[i], l.q - ps[i])) >= 0) qs.push_back(ps[i]); 
    if (sign(cross(l.p - ps[i], l.q - ps[i])) *
        sign(cross(l.p - ps[j], l.q - ps[j])) < 0) {
      auto a = cross(ps[j] - ps[i], l.q - l.p);
      auto b = cross(l.p - ps[i], l.q - l.p); 
      qs.push_back(ps[i] + b/a*(ps[j] - ps[i]));
    }
  }
  return qs;
}

struct delaunay {
  struct edge {
    int src, dst;
  };
  int n;
  vector<point> ps;
  vector<vector<edge>> adj; // optional
  vector<int> inner;
  int incircle(int a, int b, int c, int p) {
    point u = ps[a]-ps[p], v = ps[b]-ps[p], w = ps[c]-ps[p];
    return sign(norm2(u)*cross(v,w)
               +norm2(v)*cross(w,u)
               +norm2(w)*cross(u,v)) > 0;
  }
  bool orient(int a, int b, int p) { 
    point u = ps[a]-ps[b], v = ps[p]-ps[b];
    int s = sign(cross(u, v));
    return s ? s > 0 : sign(dot(u, v)) > 0;
  }
  delaunay(vector<point> ps) : n(ps.size()), ps(ps), adj(n), inner(n) {
    if (n <= 1) return;
    vector<unordered_map<int,int>> ccw(n); // ccw[u][v] is the third pt for (u,v)
    auto make_triangle = [&](int a, int b, int c) {
      ccw[a][b] = c; ccw[b][c] = a; ccw[c][a] = b;
    };
    vector<int> is(n); iota(all(is), 0);
    sort(all(is), [&](int i, int j) { return ps[i] < ps[j]; });

    // delaunay flips
    int nflip = 0;
    function<void(int,int)> rec = [&](int a, int b) { 
      if (!ccw[a].count(b) || !ccw[b].count(a)) return;
      int c = ccw[a][b], d = ccw[b][a];
      if (incircle(a, b, c, d) > 0) {
        ++nflip;
        ccw[a].erase(b); ccw[b].erase(a);
        make_triangle(d, c, a);
        make_triangle(c, d, b);
        rec(a, d); rec(d, b); rec(b, c); rec(c, a);
      }
    };
    // lexicographic triangulation 
    vector<int> next(n,-1), prev(n,-1); 
    next[is[0]] = prev[is[0]] = is[1];
    next[is[1]] = prev[is[1]] = is[0];
    for (int i = 2; i < n; ++i) {
      int h = is[i], u = is[i-1], v = u;
      while ( orient(u, next[u], h)) u = next[u];
      while (!orient(v, prev[v], h)) v = prev[v];
      for (int w = v; w != u; w = next[w]) 
        if (sign(cross(ps[next[w]]-ps[h], ps[w]-ps[h])) > 0) 
          make_triangle(w, h, next[w]);
      next[h] = u; prev[u] = h;
      prev[h] = v; next[v] = h;
    }
    for (int u: is) { 
      auto nbh = ccw[u]; // hardcopy
      for (auto z: nbh) rec(z.fst, z.snd); // flip
    }
    // complete graph structure
    for (int u: is) {
      int v = ccw[u].begin()->fst, s = v;
      while (ccw[s].count(u)) {
        s = ccw[s][u];
        if (s == v) break;
      }
      if (v != s) { inner[u] = false; v = s; }
      do {
        adj[u].push_back({u, v});
        if (!ccw[u].count(v)) break;
        v = ccw[u][v];
      } while (v != s);
    }
  }
};
struct voronoi {
  struct edge {
    int src, dst;
    point::T len;
  };
  int n, m;
  vector<point> ps, qs; // qs is the voronoi vertices
  map<point,int> id;
  vector<vector<int>> cell;
  vector<vector<edge>> adj;

  void add_edge(int u, int v) {
    auto len = norm(qs[u] - qs[v]);
    adj[u].push_back({u, v, len});
    adj[v].push_back({v, u, len});
  }
  int node(point p) { 
    if (!id.count(p)) { id[p] = m++; qs.push_back(p); adj.push_back({}); }
    return id[p];
  }
  voronoi(delaunay DT, vector<point> domain) : 
    n(DT.n), m(0), ps(DT.ps), cell(n) {
    for (int u = 0; u < n; ++u) {
      vector<point> region = domain;
      for (auto e: DT.adj[u]) {
        point s = (ps[e.src]+ps[e.dst])/2, d = orth(ps[e.dst]-ps[e.src]);
        region = convex_cut(region, {s, s+d});
      }
      for (int i = 0; i < region.size(); ++i) {
        add_edge(node(region[i]), node(region[(i+1)%region.size()]));
        cell[u].push_back(node(region[i]));
      }
    }
  }
  voronoi(vector<point> ps, vector<point> domain) :
    voronoi(delaunay(ps), domain) { }
};
int main() {
  for (int n, m; scanf("%d %d", &n, &m); ) {
    if (n == 0) break;
    vector<point> ps(n);
    for (int i = 0; i < n; ++i) 
      scanf("%lf %lf", &ps[i].x, &ps[i].y);
    delaunay DT(ps);

    vector<double> score(n);
    double ans = 0.0;
    for (int j = 0; j < m; ++j) {
      point c, d;
      double s; 
      scanf("%lf %lf %lf %lf %lf", &c.x, &c.y, &d.x, &d.y, &s);
      vector<point> domain = {
        c + point({-d.x, -d.y}),
        c + point({+d.x, -d.y}),
        c + point({+d.x, +d.y}),
        c + point({-d.x, +d.y}),
      };
      voronoi V(DT, domain);

      vector<point> &qs = V.qs;
      for (int i = 0; i < n; ++i) {
        point::T area = 0;
        int K = V.cell[i].size();
        for (int k = 0; k < K; ++k) {
          int v = V.cell[i][k], w = V.cell[i][(k+1)%K];
          area += cross(qs[v], qs[w]);
        }
        //cerr << "area of " << i << "th region: " << area << endl;
        score[i] += s * area / 2 / (4 * d.x * d.y);
        ans = max(ans, score[i]);
      }
    }
    printf("%.12lf\n", ans);
  }
}