#include <bits/stdc++.h>
using namespace std;
const int N = 100100;
struct point {
  double x, y;
  int id;
  point() {}
  point(int _x, int _y, int _id) : x(_x), y(_y), id(_id) {}
  point operator-(const point &other) const {
    return point(x - other.x, y - other.y, 0);
  }
  bool operator<(const point &other) const {
    if (x == other.x) {
      return y < other.y;
    } else {
      return x < other.x;
    }
  }
} pts[N];
double cross(const point &a, const point &b) { return a.x * b.y - a.y * b.x; }
bool collinear(const point &a, const point &b, const point &c) {
  return cross(b - a, c - a) == 0;
}
double calc(const point &one, const point &two, const point &p) {
  double a, b, c;
  if (one.x == two.x) {
    a = 1;
    b = 0;
    c = -one.x;
  } else {
    a = -(double)(one.y - two.y) / (one.x - two.x);
    b = 1;
    c = -(double)(a * one.x) - one.y;
  }
  return fabs(a * p.x + b * p.y + c) / sqrt(a * a + b * b);
}
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%lf %lf", &pts[i].x, &pts[i].y);
    pts[i].id = i + 1;
  }
  sort(pts, pts + n);
  int ans = 0;
  double min_dist = DBL_MAX;
  for (int i = 2; i < n; ++i) {
    if (!collinear(pts[0], pts[1], pts[i])) {
      double dist = calc(pts[0], pts[1], pts[i]);
      if (dist < min_dist) {
        min_dist = dist;
        ans = i;
      }
    }
  }
  printf("%d %d %d\n", pts[0].id, pts[1].id, pts[ans].id);
  return 0;
}
