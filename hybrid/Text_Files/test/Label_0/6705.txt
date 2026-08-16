#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<deque>
#include<algorithm>
#include<numeric>
#include<utility>
#include<complex>
#include<functional>
 
using namespace std;

/* constant */

const double PI = acos(-1);
const double PIH = PI / 2;

/* typedef */

template <typename T>
struct Pt {
  T x, y;

  Pt() {}
  Pt(T _x, T _y) : x(_x), y(_y) {}
  Pt(const Pt& pt) : x(pt.x), y(pt.y) {}

  Pt operator+(const Pt pt) const { return Pt(x + pt.x, y + pt.y); }
  Pt operator-() const { return Pt(-x, -y); }
  Pt operator-(const Pt pt) const { return Pt(x - pt.x, y - pt.y); }
  Pt operator*(T t) const { return Pt(x * t, y * t); }
  Pt operator/(T t) const { return Pt(x / t, y / t); }
  T dot(Pt v) { return x * v.x + y * v.y; }
  T cross(Pt v) { return x * v.y - y * v.x; }
  Pt mid(const Pt pt) { return Pt((x + pt.x) / 2, (y + pt.y) / 2); }
  T d2() { return x * x + y * y; }
  double d() { return sqrt(d2()); }

  Pt rot(double th) {
    double c = cos(th), s = sin(th);
    return Pt(c * x - s * y, s * x + c * y);
  }
  
  void print(string format) {
    printf(("(" + format + ", " + format + ")\n").c_str(), x, y);
  }
};

template <typename T>
struct Pt3D {
  T x, y, z;

  Pt3D() {}
  Pt3D(T _x, T _y, T _z) { x = _x; y = _y; z = _z; }

  bool operator==(const Pt3D<T>& pt) {
    return x == pt.x && y == pt.y && z == pt.z;
  }

  bool operator<(const Pt3D<T>& pt) const {
    return x < pt.x || (x == pt.x && (y < pt.y || (y == pt.y && z < pt.z)));
  }
  
  Pt3D<T> operator+(const Pt3D<T>& pt) {
    return Pt3D<T>(x + pt.x, y + pt.y, z + pt.z);
  }

  Pt3D<T> operator-(const Pt3D<T>& pt) {
    return Pt3D<T>(x - pt.x, y - pt.y, z - pt.z);
  }
  
  Pt3D<T> operator-() { return Pt3D<T>(-x, -y, -z); }
  Pt3D<T> operator*(const T& t) { return Pt3D<T>(x * t, y * t, z * t); }
  Pt3D<T> operator/(const T& t) { return Pt3D<T>(x / t, y / t, z / t); }

  T dot(const Pt3D<T>& v) { return x * v.x + y * v.y + z * v.z; }

  Pt3D<T> cross(const Pt3D<T>& v) {
    return Pt3D<T>(y * v.z - z * v.y, z * v.x - x * v.z, x * v.y - y * v.x);
  }

  T d2() { return x * x + y * y + z * z; }
  double d() { return sqrt(d2()); }
  Pt3D<T> normalize() { return *this / d(); }

  void print(string format) {
    printf(("(" + format + ", " + format + ", " + format + ")\n").c_str(),
	   x, y, z);
  }
};

typedef Pt<double> pt;
typedef Pt3D<double> pt3d;

/* global variables */

pt3d t, b, p;
double r;

/* subroutines */

pt3d rot_x(const pt3d pt, double th) {
  double c = cos(th), s = sin(th);
  return pt3d(pt.x, c * pt.y - s * pt.z, s * pt.y + c * pt.z);
}

pt3d rot_y(const pt3d pt, double th) {
  double c = cos(th), s = sin(th);
  return pt3d(s * pt.z + c * pt.x, pt.y, c * pt.z - s * pt.x);
}

pt3d rot_z(const pt3d pt, double th) {
  double c = cos(th), s = sin(th);
  return pt3d(c * pt.x - s * pt.y, s * pt.x + c * pt.y, pt.z);
}

bool cross_lines(const pt& a0, const pt& a1, const pt& b0, const pt& b1,
                 pt& ret) {
  pt da = a1 - a0;
  pt db = b1 - b0;

  double op01 = da.cross(db);
  if (op01 == 0.0) return false; /* need to handle parallel?? */

  pt v = b0 - a0;
  double op0 = v.cross(da);
  double op1 = v.cross(db);

  double t0 = op1 / op01;
  double t1 = op0 / op01;

  ret = db * t1 + b0;
  return true;
}

/* main */

int main() {
  cin >> t.x >> t.y >> t.z;
  cin >> b.x >> b.y >> b.z >> r;
  cin >> p.x >> p.y >> p.z;

  t = t - b;
  p = p - b;

  double th0 = atan2(t.y, t.x);
  t = rot_z(t, -th0);
  p = rot_z(p, -th0);
  //t.print("%.6lf");
  
  double th1 = atan2(t.x, t.z);
  t = rot_y(t, -th1);
  p = rot_y(p, -th1);
  //t.print("%.6lf");
  
  double th2 = atan2(p.y, p.x);
  p = rot_z(p, PIH - th2);
  //p.print("%.6lf");
  
  double v = PI * r * r * t.z / 3;
  //printf("%.6lf\n", v);

  pt pp(p.y, p.z), aa(r, 0.0), bb(-r, 0.0), tt(0.0, t.z);
  pt aad, bbd;
  
  cross_lines(aa, pp, bb, tt, aad);
  cross_lines(bb, pp, aa, tt, bbd);
  //aad.print("%.6lf");
  //bbd.print("%.6lf");

  pt mo = aad.mid(bbd);
  //mo.print("%.6lf");

  pt dabd = aad - bbd;
  double ry = dabd.d() / 2;

  double mr = r * (t.z - mo.y) / t.z;
  double rx = sqrt(mr * mr - mo.x * mo.x);
  //printf("rx=%.6lf, ry=%.6lf\n", rx, ry);

  pt oo(0.0, 0.0), dtt;
  cross_lines(aad, bbd, oo, tt, dtt);
  //dtt.print("%.6lf");

  double th3 = atan2(abs(dabd.y), abs(dabd.x));
  double h = (tt.y - dtt.y) * cos(th3);
  //printf("tt.y=%.6lf, dtt.y=%.6lf, cos=%.6lf, h=%.6lf\n",
  //tt.y, dtt.y, cos(th3), h);

  double v0 = PI * rx * ry * h / 3;
  printf("%.6lf %.6lf\n", v0, v - v0);
  
  return 0;
}