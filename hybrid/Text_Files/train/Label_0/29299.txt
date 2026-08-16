#include <bits/stdc++.h>
using namespace std;
class Solver {
  int n;
  vector<vector<int> > es;
  vector<vector<double> > esw;

 public:
  Solver(int n) : n(n), es(n), esw(n) {}
  int addv(int cnt) {
    int ret = n;
    n += cnt;
    es.resize(n);
    esw.resize(n);
    return ret;
  }
  void adde(int a, int b, double w, bool oneSide = false) {
    es[a].push_back(b);
    esw[a].push_back(w);
    if (!oneSide) {
      es[b].push_back(a);
      esw[b].push_back(w);
    }
  }
  double solve(int st, int en) {
    vector<double> d(n, 1e100);
    priority_queue<pair<double, int> > q;
    d[st] = 0;
    q.push(make_pair(-d[st], st));
    while (!q.empty()) {
      double cd = -q.top().first;
      int v = q.top().second;
      q.pop();
      if (fabs(cd - d[v]) > 1e-9) continue;
      for (int i = 0; i < ((int)(es[v]).size()); i++) {
        int b = es[v][i];
        if (d[b] > cd + esw[v][i] + 1e-9) {
          d[b] = cd + esw[v][i];
          q.push(make_pair(-d[b], b));
        }
      }
    }
    return d[en];
  }
};
int sgn(double x) { return x < -1e-9 ? -1 : x > 1e-9; }
struct pt {
  double x, y;
  pt() : x(0), y(0) {}
  pt(double x, double y) : x(x), y(y) {}
  pt operator-(const pt &p2) const { return pt(x - p2.x, y - p2.y); }
  pt operator+(const pt &p2) const { return pt(x + p2.x, y + p2.y); }
  int operator*(const pt &p2) const { return sgn(x * p2.y - y * p2.x); }
  bool operator<(const pt &p2) const {
    if (fabs(x - p2.x) > 1e-9) return x < p2.x;
    return y < p2.y - 1e-9;
  }
  double dist() const { return sqrt(x * x + y * y); }
};
struct segm {
  pt a, b;
  int id;
  int dir;
  segm(pt a, pt b, int id)
      : a(min(a, b)),
        b(max(a, b)),
        id(id),
        dir((b.x < a.x - 1e-9) ? -1 : (a.x < b.x - 1e-9)) {}
  double gety(double x) const {
    if (fabs(b.x - a.x) < 1e-9) {
      assert(fabs(b.y - a.y) < 1e-9);
      return a.y;
    }
    return a.y + (b.y - a.y) * (x - a.x) / (b.x - a.x);
  }
  pt operator&(const double x) const { return pt(x, gety(x)); }
  bool operator<(const segm &s2) const {
    assert(!(b.x < s2.a.x - 1e-9));
    assert(!(s2.b.x < a.x - 1e-9));
    double vals[] = {a.x, b.x, s2.a.x, s2.b.x};
    sort(vals, vals + 4);
    double y1 = gety(vals[1]), y2 = s2.gety(vals[1]);
    if (fabs(y1 - y2) > 1e-9) return y1 < y2;
    return id < s2.id;
  }
};
struct Ev {
  double x;
  int id;
  int ty, dirs;
  Ev(double x, int id, int ty, int dirs = 0)
      : x(x), id(id), ty(ty), dirs(dirs) {}
  bool operator<(const Ev &e2) const {
    if (fabs(x - e2.x) > 1e-9) return x < e2.x;
    if (ty != e2.ty) return ty > e2.ty;
    return id < e2.id;
  }
};
int main() {
  int n;
  while (scanf("%d", &n) >= 1) {
    vector<pt> pts(n);
    for (int i = 0; i < n; i++) scanf("%lf%lf", &pts[i].x, &pts[i].y);
    pts.push_back(pts[0]);
    int stv, env;
    scanf("%d%d", &stv, &env), stv--, env--;
    vector<Ev> evs;
    for (int i = 0; i < n; i++) {
      {
        int pr = (i == 0) ? n - 1 : i - 1;
        int d1 = segm(pts[pr], pts[i], -1).dir;
        int d2 = segm(pts[i], pts[i + 1], -1).dir;
        int dirs = 0;
        if (d1 == d2) {
          if (d1 == 1)
            dirs |= 1;
          else if (d1 == -1)
            dirs |= 2;
        } else {
          int s = (pts[pr] - pts[i]) * (pts[i + 1] - pts[i]);
          if (s == 1) dirs |= 3;
        }
        if (dirs) evs.push_back(Ev(pts[i].x, i, 0, dirs));
      }
      pt a = pts[i], b = pts[i + 1];
      if (a.x > b.x) swap(a, b);
      if (fabs(a.x - b.x) > 1e-9) {
        evs.push_back(Ev(a.x, i, 1));
        evs.push_back(Ev(b.x, i, -1));
      }
    }
    sort(evs.begin(), evs.end());
    vector<vector<pair<pt, int> > > addpt(n);
    set<segm> segUp, segDn;
    for (int i = 0; i < ((int)(evs).size());) {
      int en = i;
      while (en < ((int)(evs).size()) && fabs(evs[en].x - evs[i].x) < 1e-9)
        en++;
      for (; i < en; i++) {
        int id = evs[i].id;
        if (evs[i].ty) {
          segm s(pts[id], pts[id + 1], id);
          set<segm> &ss = s.dir == 1 ? segUp : segDn;
          if (evs[i].ty == 1)
            ss.insert(s);
          else {
            assert(ss.count(s));
            ss.erase(s);
          }
        } else {
          segm s(pts[id], pts[id], -1);
          set<segm>::iterator it;
          if (evs[i].dirs & 1) {
            s.id = 1e9;
            it = segDn.upper_bound(s);
            if (it != segDn.end()) {
              pt tmp = *it & pts[id].x;
              addpt[it->id].push_back(make_pair(tmp, id));
            }
          }
          if (evs[i].dirs & 2) {
            s.id = -1;
            it = segUp.lower_bound(s);
            if (it != segUp.begin()) {
              it--;
              pt tmp = *it & pts[id].x;
              addpt[it->id].push_back(make_pair(tmp, id));
            }
          }
        }
      }
    }
    Solver s(n);
    for (int i = 0; i < n; i++) {
      sort(addpt[i].begin(), addpt[i].end());
      if (pts[i + 1] < pts[i]) reverse(addpt[i].begin(), addpt[i].end());
      int ne = (i + 1 == n) ? 0 : (i + 1);
      vector<pair<pt, int> > &cp = addpt[i];
      if (cp.empty()) {
        s.adde(i, ne, (pts[ne] - pts[i]).dist());
      } else {
        int st = s.addv(((int)(cp).size()));
        s.adde(i, st, (cp[0].first - pts[i]).dist());
        s.adde(st + ((int)(cp).size()) - 1, ne,
               (cp.back().first - pts[ne]).dist());
        for (int i2 = 0; i2 + 1 < ((int)(cp).size()); i2++) {
          s.adde(st + i2, st + i2 + 1,
                 (cp[i2 + 1].first - cp[i2].first).dist());
        }
        for (int i2 = 0; i2 < ((int)(cp).size()); i2++) {
          pt p1 = cp[i2].first;
          int aid = st + i2;
          pt p2 = pts[cp[i2].second];
          int bid = cp[i2].second;
          if (p1.y < p2.y) {
            swap(p1, p2);
            swap(aid, bid);
          }
          s.adde(aid, bid, (p1 - p2).dist(), true);
        }
      }
    }
    double ans = s.solve(stv, env);
    printf("%.18e\n", ans);
  }
  return 0;
}
