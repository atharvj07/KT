#include <bits/stdc++.h>
const int inf = 1 << 30;
const long long INF = 1LL << 61;
void judge() {}
inline char nc() {
  static char buf[1000000], *p1 = buf, *p2 = buf;
  return p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1000000, stdin), p1 == p2)
             ? EOF
             : *p1++;
}
template <class Tp>
inline void read(register Tp &s) {
  s = 0;
  bool neg = 0;
  char c = nc();
  for (; c < '0' || c > '9'; neg |= (c == '-'), c = nc())
    ;
  for (; c >= '0' && c <= '9'; s = 10 * s + (c ^ 48), c = nc())
    ;
  neg && (s = -s);
}
long long s1, s2;
bool check(long long x1, long long y1, long long x2, long long y2, long long x3,
           long long y3, long long x4, long long y4) {
  long long u = std::max(x1, x3);
  long long d = std::min(x2, x4);
  long long l = std::max(y1, y3);
  long long r = std::min(y2, y4);
  return u <= d && l <= r;
}
long long getblack(long long x1, long long y1, long long x2, long long y2) {
  bool opt = (x1 + y1) & 1;
  long long n = x2 - x1 + 1, m = y2 - y1 + 1;
  if (opt) {
    return 1LL * n * (m / 2) + ((m & 1) ? (n / 2) + (n & 1) : 0);
  } else {
    return 1LL * n * (m / 2) + ((m & 1) ? (n / 2) : 0);
  }
}
long long getwhite(long long x1, long long y1, long long x2, long long y2) {
  return 1LL * (x2 - x1 + 1) * (y2 - y1 + 1) - getblack(x1, y1, x2, y2);
}
void solve() {
  long long n, m;
  scanf("%I64d%I64d", &n, &m);
  std::swap(n, m);
  s2 = getblack(1, 1, n, m);
  s1 = getwhite(1, 1, n, m);
  long long x1, y1, x2, y2;
  scanf("%I64d%I64d%I64d%I64d", &x1, &y1, &x2, &y2);
  long long x3, y3, x4, y4;
  scanf("%I64d%I64d%I64d%I64d", &x3, &y3, &x4, &y4);
  if (check(x1, y1, x2, y2, x3, y3, x4, y4)) {
    long long u = std::max(x1, x3);
    long long d = std::min(x2, x4);
    long long l = std::max(y1, y3);
    long long r = std::min(y2, y4);
    s1 += getblack(x1, y1, x2, y2) - getblack(u, l, d, r);
    s2 -= getblack(x1, y1, x2, y2) - getblack(u, l, d, r);
    s2 += getwhite(x3, y3, x4, y4);
    s1 -= getwhite(x3, y3, x4, y4);
  } else {
    s1 += getblack(x1, y1, x2, y2);
    s2 -= getblack(x1, y1, x2, y2);
    s2 += getwhite(x3, y3, x4, y4);
    s1 -= getwhite(x3, y3, x4, y4);
  }
  printf("%I64d %I64d\n", s1, s2);
}
signed main() {
  long long T;
  for (scanf("%I64d", &T); T--;) {
    solve();
  }
  return 0;
}
