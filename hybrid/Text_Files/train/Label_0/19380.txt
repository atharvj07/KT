#include <bits/stdc++.h>
using namespace std;
const int N = 10003;
const long double eps = 1e-9;
int n, x[N], y[N], z[N];
template <typename T>
inline void read(T &x) {
  int ch = getchar();
  x = 0;
  bool f = false;
  for (; ch < '0' || ch > '9'; ch = getchar()) f |= ch == '-';
  for (; ch >= '0' && ch <= '9'; ch = getchar()) x = x * 10 + ch - '0';
  if (f) x = -x;
}
struct Quad {
  long double s, x, y, z;
  Quad(const long double &s = 0, const long double &x = 0,
       const long double &y = 0, const long double &z = 0)
      : s(s), x(x), y(y), z(z) {}
  Quad operator+(const Quad &o) const {
    return Quad(s + o.s, x + o.x, y + o.y, z + o.z);
  }
  Quad operator-(const Quad &o) const {
    return Quad(s - o.s, x - o.x, y - o.y, z - o.z);
  }
  Quad operator*(const Quad &o) const {
    return Quad(s * o.s - x * o.x - y * o.y - z * o.z,
                s * o.x + x * o.s + y * o.z - z * o.y,
                s * o.y + y * o.s + z * o.x - x * o.z,
                s * o.z + z * o.s + x * o.y - y * o.x);
  }
  Quad operator*(const long double &o) const {
    return Quad(s * o, x * o, y * o, z * o);
  }
  Quad operator/(const long double &o) const {
    return Quad(s / o, x / o, y / o, z / o);
  }
  Quad conj() const { return Quad(s, -x, -y, -z); }
  long double val() const { return s * s + x * x + y * y + z * z; }
  Quad inv() const { return conj() / val(); }
} q[N], g;
Quad round(const Quad &q) {
  Quad q1(roundl(q.s), roundl(q.x), roundl(q.y), roundl(q.z)),
      q2(roundl(q.s - 0.5) + 0.5, roundl(q.x - 0.5) + 0.5,
         roundl(q.y - 0.5) + 0.5, roundl(q.z - 0.5) + 0.5);
  return ((q1 - q).val() < (q2 - q).val()) ? q1 : q2;
}
Quad modu(const Quad &a, const Quad &b) { return a - b * round(b.inv() * a); }
Quad gcd(Quad a, Quad b) {
  while (b.val() > eps) {
    Quad r = modu(a, b);
    a = b;
    b = r;
  }
  return a;
}
int main() {
  read(n);
  for (register int i = 1; i <= n; ++i) {
    read(x[i]);
    read(y[i]);
    read(z[i]);
    q[i] = Quad(0, x[i], y[i], z[i]);
    g = gcd(q[i], g);
  }
  long long gval = round(g.val());
  vector<long long> div;
  for (long long i = 1; i * i <= gval; ++i)
    if (!(gval % i)) {
      div.push_back(i);
      if (i * i != gval) div.push_back(gval / i);
    }
  sort(div.rbegin(), div.rend());
  for (long long d : div) {
    Quad Q = gcd(g, Quad(d)), Qc = Q.conj();
    if (round(Q.val()) != d) continue;
    Quad Qp = Q / d, Qpc = Qc / d;
    bool f = true;
    for (register int i = 1; i <= n && f; ++i) {
      Quad tmp = Qpc * q[i] * Qp;
      if (fabs(round(tmp.x) - tmp.x) > eps ||
          fabs(round(tmp.y) - tmp.y) > eps || fabs(round(tmp.z) - tmp.z) > eps)
        f = false;
    }
    if (f) {
      Quad u[3] = {Q * Quad(0, 1) * Qc, Q * Quad(0, 0, 1) * Qc,
                   Q * Quad(0, 0, 0, 1) * Qc};
      printf("%lld\n", d * d);
      for (register int i = 0; i < 3; ++i)
        printf("%lld %lld %lld\n", (long long)round(u[i].x),
               (long long)round(u[i].y), (long long)round(u[i].z));
      return 0;
    }
  }
}
