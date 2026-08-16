#include <bits/stdc++.h>
using namespace std;
template <class T>
bool uin(T &a, T b) {
  return a > b ? (a = b, true) : false;
}
template <class T>
bool uax(T &a, T b) {
  return a < b ? (a = b, true) : false;
}
struct Point {
  long long x, y;
  int id;
  Point operator+(Point p) const { return {x + p.x, y + p.y, -1}; }
  Point operator-(Point p) const { return {x - p.x, y - p.y, -1}; }
  long long operator*(Point p) const { return x * p.x + y * p.y; }
  long long operator%(Point p) const { return x * p.y - y * p.x; }
  bool operator==(Point p) const { return x == p.x && y == p.y; }
  double operator~() const { return sqrt(*this * *this); }
  bool collin(Point p) const { return *this % p == 0 && *this * p > 0; }
};
struct SideOrVertex {
  Point a, b;
  SideOrVertex(Point a_, Point b_) : a(a_), b(b_) {
    if (make_pair(a.x, a.y) > make_pair(b.x, b.y)) swap(a, b);
  }
  SideOrVertex to_vertex(int z) const {
    if (!z) return {a, a};
    return {b, b};
  }
  bool is_vertex() const { return a == b; }
  int compare(SideOrVertex r) const {
    if (is_vertex() && r.is_vertex()) {
      return a.x == r.a.x ? (a.y < r.a.y ? -1 : 1) : 0;
    }
    if (!is_vertex() && !r.is_vertex()) {
      {
        int tmp = (to_vertex(0).compare(r));
        if (tmp) return tmp;
      };
      {
        int tmp = (to_vertex(1).compare(r));
        if (tmp) return tmp;
      };
      {
        int tmp = (-r.to_vertex(0).compare(*this));
        if (tmp) return tmp;
      };
      {
        int tmp = (-r.to_vertex(1).compare(*this));
        if (tmp) return tmp;
      };
      return 0;
    }
    if (!is_vertex()) return -r.compare(*this);
    if (a.x < r.a.x || a.x > r.b.x) return 0;
    long long v = (r.b - r.a) % (a - r.a);
    if (v == 0) return 0;
    if (v > 0) return 1;
    return -1;
  }
  bool operator<(const SideOrVertex &r) const { return compare(r) == -1; }
};
const int maxn = 110000;
Point p[maxn];
struct TEvent {
  long long x;
  int type;
  SideOrVertex sv;
  bool operator<(const TEvent &ev) const {
    if (x != ev.x) return x < ev.x;
    if (type != ev.type) return type < ev.type;
    return false;
  }
};
vector<pair<int, double> > e[maxn];
const double PI = atan2(0, -1);
double atan3(double y, double x) {
  double res = atan2(y, x);
  if (res < 0) res += 2 * PI;
  return res;
}
bool ccw(Point a, Point b, Point c) {
  if (a.collin(b)) return false;
  if (a.collin(c)) return false;
  if (b.collin(c)) return false;
  double sang = atan3(a % b, a * b) + atan3(b % c, b * c) + atan3(c % a, c * a);
  return sang > 3 * PI;
}
class Entry : public pair<double, int> {
 public:
  using pair<double, int>::pair;
  bool operator<(const Entry &r) const {
    if (fabs(first - r.first) > 1e-9) return first < r.first;
    return second < r.second;
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.precision(10);
  cout << fixed;
  int n;
  cin >> n;
  for (int i = 0; i < (int)(n); ++i) cin >> p[i].x >> p[i].y, p[i].id = i;
  p[n] = p[0];
  for (int i = 0; i < (int)(n); ++i) {
    int j = (i + 1) % n;
    e[i].push_back({j, ~(p[i] - p[j])});
    e[j].push_back({i, ~(p[i] - p[j])});
  }
  vector<TEvent> evs;
  for (int i = 0; i < (int)(n); ++i) {
    SideOrVertex s(p[i], p[i]);
    evs.push_back({p[i].x, 1, s});
  }
  for (int i = 0; i < (int)(n); ++i) {
    Point a = p[i], b = p[i + 1];
    if (a.x == b.x) continue;
    SideOrVertex s(a, b);
    evs.push_back({s.a.x, 2, s});
    evs.push_back({s.b.x, 0, s});
  }
  sort((evs).begin(), (evs).end());
  set<SideOrVertex> svs;
  int ptr = 0;
  while (ptr < evs.size()) {
    int x = evs[ptr].x;
    while (ptr < evs.size() && evs[ptr].x == x && evs[ptr].type == 0) {
      svs.erase(evs[ptr++].sv);
    }
    vector<SideOrVertex> xp;
    while (ptr < evs.size() && evs[ptr].x == x && evs[ptr].type == 1) {
      svs.insert(evs[ptr].sv);
      xp.push_back(evs[ptr].sv);
      ++ptr;
    }
    for (auto sv : xp) {
      int j = sv.a.id;
      int i = (j + n - 1) % n, k = (j + 1) % n;
      if (ccw(p[i] - p[j], Point({0, 1}), p[k] - p[j])) {
        auto it = svs.upper_bound(sv);
        if (it != svs.end()) {
          SideOrVertex rsv = *it;
          if (rsv.is_vertex()) {
            int rp = rsv.a.id;
            e[rp].push_back({j, ~(p[rp] - p[j])});
          } else {
            Point v = rsv.b - rsv.a;
            double y = rsv.a.y + 1.0 * v.y * (x - rsv.a.x) / v.x;
            e[rsv.a.id].push_back(
                {j, y - sv.a.y + hypot(rsv.a.x - x, rsv.a.y - y)});
            e[rsv.b.id].push_back(
                {j, y - sv.a.y + hypot(rsv.b.x - x, rsv.b.y - y)});
          }
        };
      }
      if (ccw(p[i] - p[j], Point({0, -1}), p[k] - p[j])) {
        auto it = svs.lower_bound(sv);
        if (it != svs.begin()) {
          --it;
          SideOrVertex rsv = *it;
          if (rsv.is_vertex()) {
            int rp = rsv.a.id;
            e[j].push_back({rp, ~(p[rp] - p[j])});
          } else {
            Point v = rsv.b - rsv.a;
            double y = rsv.a.y + 1.0 * v.y * (x - rsv.a.x) / v.x;
            e[j].push_back(
                {rsv.a.id, sv.a.y - y + hypot(rsv.a.x - x, rsv.a.y - y)});
            e[j].push_back(
                {rsv.b.id, sv.a.y - y + hypot(rsv.b.x - x, rsv.b.y - y)});
          }
        };
      }
    }
    for (auto sv : xp) svs.erase(sv);
    while (ptr < evs.size() && evs[ptr].x == x && evs[ptr].type == 2) {
      svs.insert(evs[ptr++].sv);
    }
  }
  int s, t;
  cin >> s >> t;
  --s;
  --t;
  vector<double> dist(n, 1e9);
  dist[s] = 0.0;
  set<Entry> q = {{0.0, s}};
  while (!q.empty()) {
    auto it = q.begin();
    int v = it->second;
    q.erase(it);
    for (auto [u, len] : e[v]) {
      double ndist = dist[v] + len;
      if (ndist + 1e-9 < dist[u]) {
        q.erase({dist[u], u});
        dist[u] = ndist;
        q.insert({dist[u], u});
      }
    }
  }
  cout << dist[t] << '\n';
  return 0;
}
