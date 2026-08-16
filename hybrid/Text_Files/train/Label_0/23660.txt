#include <bits/stdc++.h>
using LL = long long;
const int MOD = (int)1e9 + 7;
const int N = 500000 + 5;
int n;
struct Point {
  LL x, y;
  Point() {}
  Point(LL _x, LL _y) : x(_x), y(_y) {}
  Point operator-(const Point &rhs) const {
    return Point(x - rhs.x, y - rhs.y);
  }
  Point operator*(LL t) const { return Point(x * t, y * t); }
  Point operator+(const Point &rhs) const {
    return Point(x + rhs.x, y + rhs.y);
  }
};
LL det(const Point &a, const Point &b) { return a.x * b.y - a.y * b.x; }
LL det(const Point &a, const Point &b, const Point &c) {
  return det(b - a, c - a);
}
Point points[N + N];
int brute() {
  LL ret = 0;
  LL area = 0;
  for (int i = 0; i < n; ++i) {
    area += det(points[i], points[(i + 1) % n], points[0]);
  }
  for (int i = 0; i < n; ++i) {
    for (int j = i + 2; j < n; ++j) {
      if (i + n - j < 2) continue;
      LL a = 0;
      for (int k = i + 1; k < j; ++k) {
        a += det(points[i], points[k], points[k + 1]);
      }
      ret += std::abs(area - a - a);
      ret %= MOD;
    }
  }
  return (ret % MOD + MOD) % MOD;
}
int work() {
  std::copy(points, points + n, points + n);
  LL area = 0;
  for (int i = 0; i < n; ++i) {
    area += det(points[i], points[i + 1]);
  }
  LL a = 0, d = 0;
  Point b(0, 0), c(0, 0);
  LL now = 0;
  LL small = 0;
  int cnt = 0;
  for (int i = 0, j = 0; i < n; ++i) {
    for (; j < i + n; ++j) {
      LL tmp = det(points[j], points[j + 1], points[i]);
      if (1ull * now + tmp << 1 > area) break;
      now += tmp;
      a += det(points[j], points[j + 1]) % MOD * j;
      a %= MOD;
      b = b + points[j + 1] * j;
      b.x %= MOD;
      b.y %= MOD;
      c = c + points[j] * j;
      c.x %= MOD;
      c.y %= MOD;
      d += det(points[j], points[j + 1]);
      d %= MOD;
    }
    LL tmp = -(a + det(b, points[i]) % MOD + det(points[i], c) % MOD) +
             j * (d + det(points[j], points[i]) % MOD);
    tmp %= MOD;
    small += tmp;
    small %= MOD;
    a -= det(points[i], points[i + 1]) % MOD * i;
    a %= MOD;
    b = b - points[i + 1] * i;
    b.x %= MOD;
    b.y %= MOD;
    c = c - points[i] * i;
    c.x %= MOD;
    c.y %= MOD;
    d -= det(points[i], points[i + 1]);
    d %= MOD;
    if (now * 2 == area) cnt++;
    now -= det(points[i], points[i + 1], points[j]);
  }
  return ((n * 1ll * (n - 3) / 2 % MOD * (area % MOD) % MOD - small * 2 +
           (cnt / 2 * 1ll * (area % MOD)) % MOD) %
              MOD +
          MOD) %
         MOD;
}
int main() {
  std::ios::sync_with_stdio(false);
  std::cin >> n;
  for (int i = 0; i < n; ++i) {
    std::cin >> points[i].x >> points[i].y;
  }
  std::reverse(points, points + n);
  std::cout << work() << std::endl;
}
