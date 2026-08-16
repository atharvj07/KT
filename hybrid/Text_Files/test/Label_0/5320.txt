#include <bits/stdc++.h>
using namespace std;
const long long N = (long long)1e5 + 5;
struct Pt {
  long long x, y;
  Pt operator+(const Pt& a) const { return {x + a.x, y + a.y}; }
  Pt operator-(const Pt& a) const { return {x - a.x, y - a.y}; }
  long long operator^(const Pt& a) const { return x * a.y - y * a.x; }
  bool operator<(const Pt& a) const { return x < a.x || (x == a.x && y > a.y); }
  bool operator==(const Pt& a) const { return x == a.x; }
};
vector<Pt> convexhull(vector<Pt>& v) {
  sort(v.begin(), v.end());
  v.resize(unique(v.begin(), v.end()) - v.begin());
  long long n = (long long)v.size(), m = 0;
  vector<Pt> ret(2 * n);
  long long k = 1;
  for (long long i = n - 1; i >= 0; --i) {
    while (m > k && ((ret[m - 1] - ret[m - 2]) ^ (v[i] - ret[m - 2])) <= 0) m--;
    ret[m++] = v[i];
  }
  ret.resize(m);
  return ret;
}
vector<Pt> v;
long long n;
void init() {
  cin >> n;
  v.resize(n);
  for (long long i = 0; i < n; ++i)
    cin >> v[i].x >> v[i].y, v[i].y -= v[i].x * v[i].x;
}
void solve() {
  v = convexhull(v);
  cout << v.size() - 1 << '\n';
}
int32_t main() {
  init();
  solve();
}
