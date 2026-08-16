#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e4;
const long double eps = 1e-7;
struct quat {
  long double s = 0, x = 0, y = 0, z = 0;
  quat() {}
  quat(const long double _s, const long double _x, const long double _y,
       const long double _z)
      : s(_s), x(_x), y(_y), z(_z) {}
  quat operator+(quat q) { return quat(s + q.s, x + q.x, y + q.y, z + q.z); }
  quat operator-(quat q) { return quat(s - q.s, x - q.x, y - q.y, z - q.z); }
  quat operator*(long double q) { return quat(q * s, q * x, q * y, q * z); }
  quat operator/(long double d) { return quat(s / d, x / d, y / d, z / d); }
  quat operator*(quat q) {
    return quat(s * q.s - x * q.x - y * q.y - z * q.z,
                s * q.x + x * q.s + y * q.z - z * q.y,
                s * q.y - x * q.z + y * q.s + z * q.x,
                s * q.z + x * q.y - y * q.x + z * q.s);
  }
  long double slen() { return s * s + x * x + y * y + z * z; }
  quat conj() { return quat(s, -x, -y, -z); }
  quat inv() { return conj() * (1 / slen()); }
  quat qround() const {
    quat q1 = quat(round(s), round(x), round(y), round(z));
    quat q2 = quat(round(s - 0.5) + 0.5, round(x - 0.5) + 0.5,
                   round(y - 0.5) + 0.5, round(z - 0.5) + 0.5);
    return (q1 - *this).slen() < (q2 - *this).slen() ? q1 : q2;
  }
  quat operator/(quat q) { return q.inv() * *this; }
  quat operator%(quat q) { return (*this) - q * ((*this) / q).qround(); }
  bool isint() {
    return abs(round(s) - s) < eps && abs(round(x) - x) < eps &&
           abs(round(y) - y) < eps && abs(round(z) - z) < eps;
  }
  void print() {
    printf("%lld %lld %lld\n", (long long)round(x), (long long)round(y),
           (long long)round(z));
  }
};
quat gcd(quat q0, quat q1) {
  while (q1.slen() > eps) {
    quat a;
    a = q0 % q1;
    q0 = q1;
    q1 = a;
  }
  return q0;
}
long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
quat q[maxn], ans, ii, ji, ki;
long long n, m, res, w[maxn], no;
int main() {
  scanf("%lld", &n);
  for (int i = 1; i <= n; i++) {
    long long x, y, z;
    scanf("%lld%lld%lld", &x, &y, &z);
    q[i] = quat(0, x, y, z);
    if (i == 1)
      res = q[i].slen();
    else
      res = gcd(res, q[i].slen());
    if (i == 1)
      ans = q[i];
    else
      ans = gcd(ans, q[i]);
  }
  no = 0;
  for (long long i = 1; i * i <= res; i++) {
    if (res % i == 0) {
      no++;
      w[no] = i;
      if (i * i != res) {
        no++;
        w[no] = res / i;
      }
    }
  }
  sort(w + 1, w + no + 1);
  long long an = 0;
  for (int i = 1; i <= no; i++) {
    quat k = gcd(ans, quat(w[i], 0, 0, 0));
    if ((long long)(k.slen()) != w[i]) continue;
    long long r = (long long)k.slen();
    bool flag = 1;
    for (int i = 1; i <= n; i++) {
      if (!(k.inv() / r * q[i] * k).isint()) {
        flag = false;
        break;
      }
    }
    if (flag) {
      if (r * r > an) {
        an = r * r;
        ii = k * quat(0, 1, 0, 0) * k.conj();
        ji = k * quat(0, 0, 1, 0) * k.conj();
        ki = k * quat(0, 0, 0, 1) * k.conj();
      }
    }
  }
  printf("%lld\n", an);
  printf("%lld %lld %lld\n", (long long)round(ii.x), (long long)round(ii.y),
         (long long)round(ii.z));
  printf("%lld %lld %lld\n", (long long)round(ji.x), (long long)round(ji.y),
         (long long)round(ji.z));
  printf("%lld %lld %lld\n", (long long)round(ki.x), (long long)round(ki.y),
         (long long)round(ki.z));
  return 0;
}
