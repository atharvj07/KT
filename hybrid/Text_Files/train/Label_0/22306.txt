#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<ll>;
using vvll = vector<vll>;
using P = pair<int, int>;
const double eps = 1e-8;
const ll MOD = 1000000007;
const int INF = INT_MAX / 2;
const ll LINF = LLONG_MAX / 2;
template<typename T1, typename T2>
bool chmax(T1 &a, const T2 &b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}
template<typename T1, typename T2>
bool chmin(T1 &a, const T2 &b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}
template<typename T1, typename T2>
ostream &operator<<(ostream &os, const pair<T1, T2> p) {
  os << p.first << ":" << p.second;
  return os;
}
template<class T>
ostream &operator<<(ostream &os, const vector<T> &v) {
  for(int i=0;i<((int)(v.size()));++i) {
    if (i) os << " ";
    os << v[i];
  }
  return os;
}
struct Point {
  double x, y, z;
  Point(double x, double y, double z): x(x), y(y), z(z) {}
};
double operator*(const Point &p1, const Point &p2) {
  return p1.x * p2.x + p1.y * p2.y + p1.z * p2.z;
}
Point operator+(const Point &p1, const Point &p2) {
  return Point(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z);
}
Point operator-(const Point &p1, const Point &p2) {
  return Point(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z);
}
Point operator*(const double &k, const Point &p) {
  return Point(k * p.x, k * p.y, k * p.z);
}
double dist2(const Point &p1, const Point &p2) {
  return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y) + (p1.z - p2.z) * (p1.z - p2.z);
}
bool solve() {
  int n, m, R;
  cin >> n >> m >> R;
  if (n == 0) return false;
  vector<Point> s;
  vector<double> r(n);
  for(int i=0;i<(n);++i) {
    double x, y, z, nr; cin >> x >> y >> z >> nr;
    s.emplace_back(Point(x, y, z));
    r[i] = nr;
  }
  vector<Point> t;
  vector<double> b(m);
  for(int i=0;i<(m);++i) {
    double x, y, z, nb; cin >> x >> y >> z >> nb;
    t.emplace_back(Point(x, y, z));
    b[i] = nb;
  }
  Point e(0, 0, 0);
  cin >> e.x >> e.y >> e.z;
  vector<bitset<2000>> need(m);
  for(int i=0;i<(m);++i) {
    for(int j=0;j<(n);++j) {
      Point d = t[i] - e;
      double k = ((s[j] * d) - (e * d)) / (d * d);
      Point x = e + k * d;
      bool ok = true;
      if(0 < k && k < 1 && dist2(e, s[j]) > r[j] * r[j] && dist2(t[i], s[j]) > r[j] * r[j]) ok &= dist2(x, s[j]) > r[j] * r[j];
      ok &= (dist2(e, s[j]) > r[j] * r[j]) == (dist2(t[i], s[j]) > r[j] * r[j]);
      need[i][j] = !ok;
    }
  }
  double ma = 0;
  for(int i=0;i<(1<<m);++i) {
    bitset<2000> now;
    for(int j=0;j<(m);++j) {
      if((i>>j)&1) now |= need[j];
    }
    if(now.count() > R) continue;
    double val = 0;
    for(int j=0;j<(m);++j) {
      if((i>>j)&1) {
        val += b[j] / dist2(t[j], e);
      }
    }
    chmax(ma, val);
  }
  cout << ma << endl;
  return true;
}
int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout << fixed << setprecision(10);
  while (solve()) {}
}

