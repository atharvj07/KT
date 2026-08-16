#include <bits/stdc++.h>
using namespace std;
struct pt {
  int x, y;
  inline pt() {}
  inline pt(int _x, int _y) : x(_x), y(_y) {}
} p[5], tar;
int a, b, c, n;
long long t[5];
int dis(const pt &a, const pt &b) {
  return (a.x < b.x ? b.x - a.x : a.x - b.x) +
         (a.y < b.y ? b.y - a.y : a.y - b.y);
}
long long minsum(pt s, pt p) {
  int md = max(s.x - p.x, 0) + max(s.y - p.y, 0), ds = dis(s, p),
      dt = dis(p, tar);
  return ((long long)(md + ds) * (ds - md + 1) >> 1) +
         ((long long)(md + dt) * (dt - md + 1) >> 1) - md;
}
bool check(int x, int y) {
  pt cur = pt(x, y);
  for (int i = 0; i < 4; ++i)
    if (minsum(cur, p[i]) > t[i]) return 0;
  return 1;
}
void solve() {
  pt cur = pt(1, 1);
  while (cur.x < n || cur.y < n) {
    if (cur.x < n && check(cur.x + 1, cur.y))
      ++cur.x, putchar('R');
    else
      ++cur.y, putchar('U');
    for (int i = 0; i < 4; ++i) t[i] -= dis(cur, p[i]);
  }
}
int main() {
  scanf("%d%I64d%d%d%d", &n, &t[0], &a, &b, &c);
  --c;
  t[1] = t[2] = t[3] = t[0];
  p[0] = pt(a, b);
  p[1] = pt(a + c, b);
  p[2] = pt(a, b + c);
  p[3] = pt(a + c, b + c);
  tar = pt(n, n);
  if (check(1, 2) || check(2, 1))
    solve();
  else
    puts("Impossible");
  return 0;
}
