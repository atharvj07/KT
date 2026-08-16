#include <bits/stdc++.h>
using namespace std;
constexpr long double eps = 1e-9;
struct Quat {
  long double r = 0, i = 0, j = 0, k = 0;
  Quat operator-(const Quat& q) const {
    return Quat(r - q.r, i - q.i, j - q.j, k - q.k);
  }
  Quat operator*(const Quat& q) const {
    return Quat(r * q.r - i * q.i - j * q.j - k * q.k,
                r * q.i + i * q.r + j * q.k - k * q.j,
                r * q.j - i * q.k + j * q.r + k * q.i,
                r * q.k + i * q.j - j * q.i + k * q.r);
  }
  Quat operator/(const long double d) const {
    return Quat(r / d, i / d, j / d, k / d);
  }
  Quat conj() const { return Quat(r, -i, -j, -k); }
  long double norm() const { return r * r + i * i + j * j + k * k; }
  void round_self() {
    Quat q0(round(r), round(i), round(j), round(k));
    Quat q1(0.5 + round(r - 0.5), 0.5 + round(i - 0.5), 0.5 + round(j - 0.5),
            0.5 + round(k - 0.5));
    *this = (q0.norm() < q1.norm() ? q0 : q1);
  }
  Quat() {}
  Quat inv() const { return conj() / norm(); }
  Quat(const long double _r, const long double _i, const long double _j,
       const long double _k)
      : r(_r), i(_i), j(_j), k(_k) {}
};
Quat gcd(Quat q0, Quat q1) {
  while (q1.norm() > eps) {
    Quat d = (q1.inv() * q0);
    d.round_self();
    Quat q = q0 - q1 * d;
    q0 = q1;
    q1 = q;
  }
  return q0;
}
constexpr int maxn = 1e4 + 10;
struct Node {
  int x, y, z;
} point[maxn];
int main() {
  int N;
  cin >> N;
  for (int i = 0; i < N; i++) cin >> point[i].x >> point[i].y >> point[i].z;
  Quat G;
  vector<Quat> qp;
  for (int i = 0; i < N; i++) {
    qp.emplace_back(0, point[i].x, point[i].y, point[i].z);
    G = gcd(G, qp.back());
  }
  long long Gnorm = round(G.norm());
  vector<long long> div;
  for (long long i = 1; i * i <= Gnorm; i++) {
    if (Gnorm % i == 0) {
      div.push_back(i);
      if (i * i != Gnorm) div.push_back(Gnorm / i);
    }
  }
  sort(div.begin(), div.end(), greater<long long>());
  for (auto d : div) {
    Quat q = gcd(G, Quat(d, 0, 0, 0));
    Quat qconj = q.conj();
    long long r = round(q.norm());
    Quat qprim = q / r;
    Quat qprimconj = qconj / r;
    bool judge = true;
    for (int i = 0; i < N; i++) {
      Quat v = qprimconj * qp[i] * qprim;
      if (abs(round(v.i) - v.i) > eps || abs(round(v.j) - v.j) > eps ||
          abs(round(v.k) - v.k) > eps) {
        judge = false;
        break;
      }
    }
    if (judge) {
      Quat p1 = q * Quat(0, 1, 0, 0) * qconj;
      Quat p2 = q * Quat(0, 0, 1, 0) * qconj;
      Quat p3 = q * Quat(0, 0, 0, 1) * qconj;
      cout << r * r << "\n";
      for (auto u : {p1, p2, p3})
        cout << (long long)round(u.i) << " " << (long long)round(u.j) << " "
             << (long long)round(u.k) << "\n";
      return 0;
    }
  }
}
