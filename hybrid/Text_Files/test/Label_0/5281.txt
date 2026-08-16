#include <bits/stdc++.h>
using namespace std;
const long long EPS = 1e-7;
struct PT {
  long long x, y;
  PT() {}
  PT(long long x, long long y) : x(x), y(y) {}
  bool operator<(const PT &rhs) const {
    return make_pair(y, x) < make_pair(rhs.y, rhs.x);
  }
  bool operator==(const PT &rhs) const {
    return make_pair(y, x) == make_pair(rhs.y, rhs.x);
  }
};
long long cross(PT p, PT q) { return p.x * q.y - p.y * q.x; }
long long area2(PT a, PT b, PT c) {
  return cross(a, b) + cross(b, c) + cross(c, a);
}
void ConvexHull(vector<PT> &pts) {
  sort(pts.begin(), pts.end());
  pts.erase(unique(pts.begin(), pts.end()), pts.end());
  vector<PT> up, dn;
  for (int i = 0; i < pts.size(); i++) {
    while (up.size() > 1 && area2(up[up.size() - 2], up.back(), pts[i]) > 0)
      up.pop_back();
    while (dn.size() > 1 && area2(dn[dn.size() - 2], dn.back(), pts[i]) < 0)
      dn.pop_back();
    up.push_back(pts[i]);
    dn.push_back(pts[i]);
  }
  pts = dn;
  for (int i = (int)up.size() - 2; i >= 1; i--) pts.push_back(up[i]);
}
vector<PT> ar;
map<pair<long long, long long>, int> mp;
void solve() {
  int n, m, fl = 0;
  PT p;
  scanf("%d", &n);
  ;
  for (int i = 0; i < n; i++) {
    cin >> p.x >> p.y;
    mp[make_pair(p.x, p.y)] = 1;
    ar.push_back(p);
  }
  scanf("%d", &m);
  ;
  for (int i = 0; i < m; i++) {
    cin >> p.x >> p.y;
    if (mp[make_pair(p.x, p.y)] == 1) {
      fl = 1;
    }
    mp[make_pair(p.x, p.y)] = 2;
    ar.push_back(p);
  }
  if (fl == 1) {
    printf("NO\n");
    return;
  }
  ConvexHull(ar);
  for (int i = 0; i < ar.size(); i++) {
    if (mp[make_pair(ar[i].x, ar[i].y)] == 2) {
      printf("NO\n");
      return;
    }
  }
  printf("YES\n");
}
int main() {
  int t = 1;
  for (int i = 1; i <= t; i++) {
    solve();
  }
}
