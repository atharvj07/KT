#include <bits/stdc++.h>
#pragma warning(disable : 4996)
template <typename T>
T min(T x, T y) {
  return x < y ? x : y;
}
template <typename T>
T max(T x, T y) {
  return x > y ? x : y;
};
const int INF = 2000000005;
const long long mod = 1000000007;
const long long MAXN = 1000005;
const double eps = 1e-6;
int sgn(double x) { return x < -eps ? -1 : x > eps; }
double SQ(double x) { return x * x; }
struct point {
  double x;
  double y;
  point(double X = 0, double Y = 0) { x = X, y = Y; }
  point operator-(point t) { return {x - t.x, y - t.y}; }
  double operator*(point t) { return x * t.y - y * t.x; }
  double operator%(point t) { return x * t.x + y * t.y; }
  double norm() { return sqrt(SQ(x) + SQ(y)); }
};
struct polygon {
  int n;
  std::vector<point> V;
  double S;
  void read() {
    double x, y;
    V.clear();
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%lf %lf", &x, &y);
      V.push_back({x, y});
    }
    S = 0;
    for (int i = 0; i < n - 1; i++) S += V[i] * V[i + 1];
    S += V[n - 1] * V[0];
    S = 0.5 * fabs(S);
  }
  bool in(point p) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
      int j = (i + 1) % n;
      point u = V[i], v = V[j];
      if (sgn(p.y - u.y) == 0 || sgn(p.y - v.y) == 0)
        return in({p.x, p.y + 3 * eps});
      if (sgn(u.y - v.y) <= 0) std::swap(u, v);
      if (sgn(p.y - u.y) > 0 || sgn(p.y - v.y) <= 0) continue;
      cnt += sgn((v - p) * (u - p)) > 0;
    }
    return cnt & 1;
  }
  double dis(point a, point b, point p) {
    point ab = b - a, pa = a - p, pb = b - p;
    if ((ab % pb) * (ab % pa) < 0) return fabs(pa * ab) / ab.norm();
    return min(pa.norm(), pb.norm());
  }
  double dis(double x, double y) {
    double t = 1e15;
    for (int i = 0; i < n; i++) {
      int j = (i + 1) % n;
      point u = V[i], v = V[j];
      t = min(t, dis(u, v, {x, y}));
    }
    return t;
  }
  bool judge(double x, double y, double r) {
    if (dis(x, y) < r + eps) return true;
    return in({x, y});
  }
};
double W, H;
int N, Q;
polygon P[MAXN];
int main() {
  scanf("%lf %lf %d", &W, &H, &N);
  for (int i = 1; i <= N; i++) P[i].read();
  double x, y, r;
  scanf("%d", &Q);
  while (Q--) {
    scanf("%lf %lf %lf", &x, &y, &r);
    std::vector<int> q;
    double t = 0;
    for (int i = 1; i <= N; i++)
      if (P[i].judge(x, y, r)) q.push_back(i - 1), t += P[i].S;
    printf("%lf %d ", t, q.size());
    for (int i = 0; i < q.size(); i++) printf("%d ", q[i]);
    printf("\n");
  }
  return 0;
}
