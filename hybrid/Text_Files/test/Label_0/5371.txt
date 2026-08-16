#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 100;
struct Point {
  double x, y;
  Point(double _x = 0, double _y = 0) {
    x = _x;
    y = _y;
  }
} point[maxn];
Point operator-(const Point &a, const Point &b) {
  return Point(a.x - b.x, a.y - b.y);
}
Point operator+(const Point &a, const Point &b) {
  return Point(a.x + b.x, a.y + b.y);
}
double operator*(const Point &a, const Point &b) {
  return a.x * b.y - b.x * a.y;
}
double dis(const Point &a, const Point &b) {
  return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%lf %lf", &point[i].x, &point[i].y);
  for (int i = n; i < n * 2; i++) point[i] = point[i - n];
  double ans = 1e18;
  for (int i = 0; i < n; i++) {
    double tmp = (point[i + 2] - point[i]) * (point[i + 1] - point[i]) / 2;
    ans = min(ans, tmp / dis(point[i], point[i + 2]));
  }
  printf("%.10f\n", ans);
}
