#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9 + 1;
struct Point {
  int x, y;
};
bool operator<(const Point &a, const Point &b) {
  return make_pair(a.x, a.y) < make_pair(b.x, b.y);
}
struct Val {
  double slope;
  bool sense;
};
bool operator<(const Val &a, const Val &b) {
  return make_pair(a.sense, a.slope) < make_pair(b.sense, b.slope);
}
Val getVal(const Point &a, const Point &b) {
  if (b.x == a.x) {
    if (a.y < b.y)
      return Val{+INF, 1};
    else
      return Val{-INF, 0};
  }
  return Val{1.0 * (b.y - a.y) / (b.x - a.x), a.x <= b.x};
}
int n, q;
int m;
Point points[300002];
Val v[300002];
int polygon[300002];
struct Query {
  int l, r;
  int index;
};
bool operator<(const Query &a, const Query &b) { return a.l < b.l; }
Query queries[100002];
map<Val, int> last;
int nextAp[300002];
int aib[300002];
void update(int pos, int val) {
  for (int i = pos; i <= m; i += i & (-i)) aib[i] += val;
}
int query(int pos) {
  int ans = 0;
  for (int i = pos; i >= 1; i -= i & (-i)) ans += aib[i];
  return ans;
}
int rp[100002];
int ans[100002];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n;
  for (int i = 1; i <= n; i++) {
    int cnt;
    cin >> cnt;
    for (int j = 1; j <= cnt; j++) cin >> points[j].x >> points[j].y;
    if (getVal(points[1], points[2]) < getVal(points[2], points[3]))
      ;
    reverse(points + 1, points + cnt + 1);
    int mip = -1;
    for (int j = 1; j <= cnt; j++)
      if (mip == -1 || points[j] < points[mip]) mip = j;
    int j = mip;
    do {
      int j1 = j + 1;
      if (j1 == cnt + 1) j1 = 1;
      v[++m] = getVal(points[j], points[j1]);
      polygon[m] = i;
      j = j1;
    } while (j != mip);
  }
  for (int i = m; i >= 1; i--) {
    if (last.find(v[i]) != last.end()) nextAp[i] = last[v[i]];
    last[v[i]] = i;
  }
  cin >> q;
  for (int i = 1; i <= q; i++) {
    cin >> queries[i].l >> queries[i].r;
    queries[i].index = i;
  }
  sort(queries + 1, queries + q + 1);
  int lpos = 0;
  for (int i = 1; i <= m; i++) {
    if (last[v[i]] == i) update(i, +1);
    rp[polygon[i]] = i;
  }
  for (int i = 1; i <= q; i++) {
    while (lpos < m && polygon[lpos] < queries[i].l) {
      if (lpos != 0) update(lpos, -1);
      if (nextAp[lpos] != 0) update(nextAp[lpos], +1);
      lpos++;
    }
    ans[queries[i].index] = query(rp[queries[i].r]);
  }
  for (int i = 1; i <= q; i++) cout << ans[i] << "\n";
  return 0;
}
