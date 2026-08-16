#include <bits/stdc++.h>
using namespace std;
const double eps = 1e-7;
const long long INFF = 1e18;
const int INF = 1e9;
const int mod = 1e9 + 7;
const int MAX = 1e3 + 7;
struct Point {
  long long x, y;
  Point(){};
  Point(long long _x, long long _y) { x = _x, y = _y; }
  void read() { scanf("%lld %lld", &x, &y); }
  Point operator+(const Point& P2) { return Point(x + P2.x, y + P2.y); }
  Point operator-(const Point& P2) { return Point(x - P2.x, y - P2.y); }
  Point operator*(const long long& Len) { return Point(x * Len, y * Len); }
  long long operator*(const Point& P2) { return x * P2.x + y * P2.y; }
  long long operator^(const Point& P2) { return x * P2.y - y * P2.x; }
  long long dis() { return x * x + y * y; }
  const bool operator<(const Point& p2) {
    if (x != p2.x) return x < p2.x;
    return y < p2.y;
  }
};
struct Line {
  Point s, e;
  Line(){};
  Line(Point _s, Point _e) { s = _s, e = _e; }
  void read() {
    s.read();
    e.read();
  }
};
int per[MAX];
Point pt[MAX];
Point pos[7];
int n, m, cur;
bool cmp(const int& a, const int& b) {
  Point p1 = pt[a] - pos[cur], p2 = pt[b] - pos[cur];
  long double v1 = atan2(p1.y, p1.x), v2 = atan2(p2.y, p2.x);
  if (fabs(v1 - v2) >= eps) return v1 < v2;
  long long val = p1 ^ p2;
  if (val == 0)
    return p1.dis() < p2.dis();
  else
    return val > 0;
}
vector<int> con[7][MAX];
bitset<MAX> ok;
int in[MAX], cntp;
int main(void) {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < (n); ++i) pos[i].read();
  for (int i = (1); i < (m + 1); ++i) pt[i].read();
  for (int j = (1); j < (m + 1); ++j) per[j] = j;
  for (int i = 0; i < n; ++i) {
    cur = i;
    sort(per + 1, per + m + 1, cmp);
    for (int j = (1); j < (m + 1); ++j) {
      int ll = j, rr = j;
      while (rr < m) {
        if ((pt[per[ll]] - pos[i]) ^ (pt[per[rr + 1]] - pos[i]) ||
            (pt[per[ll]] - pos[i]) * (pt[per[rr + 1]] - pos[i]) <= 0)
          break;
        rr++;
      }
      for (int k = (ll); k < (rr + 1); ++k) {
        for (int kk = (ll); kk < (k); ++kk) {
          con[i][per[k]].push_back(per[kk]);
          if (((int)con[i][per[k]].size()) >= n) break;
        }
      }
      j = rr;
    }
  }
  for (int j = 0; j < (n); ++j) per[j] = j;
  do {
    for (int i = (1); i < (m + 1); ++i)
      if (!ok[i]) {
        cntp++;
        vector<int> stk;
        stk.push_back(i);
        in[i] = cntp;
        for (int j = 0; j < (n); ++j) {
          if (((int)stk.size()) > n - j) break;
          int v = stk.back();
          stk.pop_back();
          for (int x : con[per[j]][v]) {
            if (in[x] == cntp) continue;
            in[x] = cntp;
            stk.push_back(x);
          }
          if (stk.empty()) {
            ok[i] = 1;
            break;
          }
        }
      }
  } while (next_permutation(per, per + n));
  int ans = 0;
  for (int i = (1); i < (m + 1); ++i)
    if (ok[i]) ans++;
  printf("%d\n", ans);
  return 0;
}
