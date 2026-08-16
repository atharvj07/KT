#include <bits/stdc++.h>
using namespace std;
const double PI = acos(-1), eps = 1e-8;
int n, Q, tp, sl, fh;
double sum[100010];
struct Point {
  double x, y;
  bool operator<(const Point &p) const {
    return x < p.x || (x == p.x && y < p.y);
  }
  bool operator>(const Point &p) const {
    return x > p.x || (x == p.x && y > p.y);
  }
} q, O, a[100010];
double operator^(const Point &p, const Point &q) {
  return p.x * q.y - q.x * p.y;
}
Point operator*(const Point &p, const double &q) {
  return (Point){p.x * q, p.y * q};
}
Point operator-(const Point &p, const Point &q) {
  return (Point){p.x - q.x, p.y - q.y};
}
Point operator+(const Point &p, const Point &q) {
  return (Point){p.x + q.x, p.y + q.y};
}
int rd() {
  sl = 0;
  fh = 1;
  char ch = getchar();
  while (ch < '0' || '9' < ch) {
    if (ch == '-') fh = -1;
    ch = getchar();
  }
  while ('0' <= ch && ch <= '9') sl = sl * 10 + ch - '0', ch = getchar();
  return sl * fh;
}
int cmpd(double v) {
  if (fabs(v) < eps)
    return 0;
  else if (v > 0)
    return 1;
  else
    return -1;
}
int getpt(bool X, bool Y, Point v) {
  int ret, mid, l = 1, r = n;
  while (l <= r) {
    mid = (l + r) >> 1;
    if (((v ^ (a[mid] - q)) <= 0) == X) {
      ret = mid;
      if (Y)
        r = mid - 1;
      else
        l = mid + 1;
    } else if (((a[1] - q) ^ (a[mid] - q)) < 0)
      r = mid - 1;
    else
      l = mid + 1;
  }
  return ret;
}
Point intersect(Point faqx1, Point faqy1, Point faqx2, Point faqy2) {
  faqy1 = faqy1 - faqx1;
  faqy2 = faqy2 - faqx2;
  Point v = faqx2 - faqx1;
  return faqx2 + faqy2 * (fabs(v ^ faqy1) / fabs(faqy1 ^ faqy2));
}
double getf(double p) {
  Point v = (Point){cos(p), sin(p)};
  int A, B;
  if ((v ^ (a[1] - q)) > 0)
    A = getpt(1, 1, v), B = getpt(1, 0, v);
  else
    A = getpt(0, 1, v), B = getpt(0, 0, v);
  double S2, S1 = sum[B - 1] - sum[A - 1];
  Point P1 = intersect(q, v + q, a[A - 1], a[A]),
        P2 = intersect(q, v + q, a[B], a[B + 1]);
  S1 += P1 ^ a[A];
  S1 += a[B] ^ P2;
  S1 += P2 ^ P1;
  S1 = fabs(S1);
  S2 = fabs(sum[n]) - S1;
  if ((v ^ (a[1] - q)) <= 0) swap(S1, S2);
  return S1 - S2;
}
double solve(double l, double r, int lv, int rv, int d) {
  if (d >= 60) return l;
  double mid = (l + r) / 2;
  double v = getf(mid);
  if (!cmpd(v)) return mid;
  if (cmpd(v) * lv > 0)
    return solve(mid, r, lv, rv, d + 1);
  else
    return solve(l, mid, lv, rv, d + 1);
}
int main() {
  n = rd();
  Q = rd();
  int p, x = n;
  O = (Point){0, 0};
  for (int i = 1; i <= n; ++i) {
    p = n - i + 1;
    a[p].x = rd(), a[p].y = rd();
    if (a[p] < a[x]) x = p;
  }
  for (int i = 1; i < x; ++i) a[i + n] = a[i];
  tp = 1;
  for (int i = 1; i <= n; ++i) {
    a[i] = a[x + i - 1];
    if (a[i] > a[tp]) tp = i;
  }
  for (int i = 1; i < n; ++i) a[i + n] = a[i];
  for (int i = 1; i <= n; ++i) sum[i] = sum[i - 1] + (a[i] ^ a[i + 1]);
  for (; Q; --Q) {
    q.x = rd();
    q.y = rd();
    double v = getf(0);
    if (!cmpd(v)) {
      printf("%.20lf\n", 0.0);
      continue;
    } else if (cmpd(v) < 0)
      x = -1;
    else
      x = 1;
    printf("%.20lf\n", solve(0, PI, x, -x, 0));
  }
  return 0;
}
