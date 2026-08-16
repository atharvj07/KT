#include <bits/stdc++.h>
using namespace std;
template <typename T>
void maxtt(T& t1, T t2) {
  t1 = max(t1, t2);
}
template <typename T>
void mintt(T& t1, T t2) {
  t1 = min(t1, t2);
}
bool debug = 0;
int n, m, k;
int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};
string direc = "RDLU";
long long ln, lk, lm;
void etp(bool f = 0) {
  puts(f ? "YES" : "NO");
  exit(0);
}
void addmod(int& x, int y, int mod = 1000000007) {
  assert(y >= 0);
  x += y;
  if (x >= mod) x -= mod;
  assert(x >= 0 && x < mod);
}
void et(int x = -1) {
  printf("%d\n", x);
  exit(0);
}
long long fastPow(long long x, long long y, int mod = 1000000007) {
  long long ans = 1;
  while (y > 0) {
    if (y & 1) ans = (x * ans) % mod;
    x = x * x % mod;
    y >>= 1;
  }
  return ans;
}
long long gcd1(long long x, long long y) { return y ? gcd1(y, x % y) : x; }
struct Point {
  long long x, y;
  Point() {}
  Point(long long x, long long y) : x(x), y(y) {}
  long long abs() const { return x * x + y * y; }
  long double arg() const { return atan2(y, x); }
  Point operator*(double o) const { return Point(x * o, y * o); }
  Point operator+(const Point& o) const { return Point(x + o.x, y + o.y); }
  Point operator-(const Point& o) const { return Point(x - o.x, y - o.y); }
  Point operator/(double o) const { return Point(x / o, y / o); }
  bool operator<(const Point& o) const {
    return x < o.x - 1e-9 || (x < o.x + 1e-9 && y < o.y - 1e-9);
  }
  friend bool operator==(const Point& r1, const Point& r2) {
    return r1.x == r2.x && r1.y == r2.y;
  }
  Point scale(double o) const { return *this * (o / abs()); }
  Point rotY() const { return Point(-y, x); }
  Point rotX() const { return Point(y, -x); }
  long long cross(Point b) const { return x * b.y - b.x * y; }
  long long dot(Point b) const { return x * b.x + y * b.y; }
  long double disToSeg(Point& a, Point& b) {
    return fabs(((*this) - a).cross(b - a) / (b - a).abs());
  }
  pair<long long, long long> getVec() {
    if (x == 0) return {0, y > 0 ? 1 : -1};
    if (y == 0) return {x < 0 ? -1 : 1, 0};
    long long gg = gcd1(::abs(x), ::abs(y));
    long long px = x / gg, py = y / gg;
    return {px, py};
  }
  void readin() { scanf("%lld%lld", &x, &y); }
};
Point a[100035], b[100035];
int d1, d2, ans;
void fmain(int tid) {
  scanf("%d%d%d", &n, &d1, &d2);
  d1 *= d1;
  d2 *= d2;
  bool ok = 1;
  for (int(i) = 1; (i) <= (int)(n); (i)++) {
    a[i].readin();
    b[i].readin();
  }
  if ((a[1] - b[1]).abs() <= d1) {
    ok = 0;
    ans++;
  }
  for (int(i) = 1; (i) <= (int)(n - 1); (i)++) {
    long long kx = a[i + 1].x - a[i].x - (b[i + 1].x - b[i].x);
    long long ky = a[i + 1].y - a[i].y - (b[i + 1].y - b[i].y);
    if (kx == 0 && ky == 0) {
    } else {
      long long up = (a[i].x - b[i].x) * kx + (a[i].y - b[i].y) * ky;
      long long dn = kx * kx + ky * ky;
      long long s1 = (a[i] - b[i]).abs();
      long long s2 = (a[i + 1] - b[i + 1]).abs();
      if (up > 0 || -up > dn) {
        if (s1 <= s2) {
          if (!ok && s2 > d2) ok = 1;
        } else {
          if (ok && s2 <= d1) {
            ok = 0;
            ans++;
          }
        }
      } else {
        long double zx =
            (long double)up / dn * (a[i].x - a[i + 1].x) + a[i].x -
            ((long double)up / dn * (b[i].x - b[i + 1].x) + b[i].x);
        long double zy =
            (long double)up / dn * (a[i].y - a[i + 1].y) + a[i].y -
            ((long double)up / dn * (b[i].y - b[i + 1].y) + b[i].y);
        long double Z = zx * zx + zy * zy;
        if (ok && (Z < d1 || abs(Z - d1) < 1e-9)) {
          ok = 0;
          ans++;
        }
        if (!ok && s2 > d2) ok = 1;
      }
    }
  }
  printf("%d\n", ans);
}
int main() {
  int t = 1;
  for (int(i) = 1; (i) <= (int)(t); (i)++) {
    fmain(i);
  }
  return 0;
}
