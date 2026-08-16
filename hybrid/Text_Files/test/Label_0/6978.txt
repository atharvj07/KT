#include <bits/stdc++.h>
using namespace std;
const int N = 200005, INF = 200000000;
int n, kk;
pair<int, int> s[N];
struct Node {
  int x, y, t;
} a[N];
inline int lowbit(int x) { return x & -x; }
struct BIT {
  int sz, c[N];
  BIT() { memset(c, 191, sizeof(c)); }
  void add(int x, int v) {
    while (x <= sz) c[x] = max(c[x], v), x += lowbit(x);
  }
  int query(int x) {
    int ret = c[0];
    while (x) {
      ret = max(ret, c[x]);
      x -= lowbit(x);
    }
    return ret;
  }
};
struct TNode {
  int lc, rc, v;
} t[N << 5];
int idx;
void modify(int &pos, int l, int r, int v) {
  int tt = ++idx;
  t[tt] = t[pos];
  pos = tt;
  ++t[tt].v;
  int mid = (l + r) >> 1;
  if (l == r) return;
  if (v <= mid)
    modify(t[pos].lc, l, mid, v);
  else
    modify(t[pos].rc, mid + 1, r, v);
}
int query(int pos, int l, int r, int ql, int qr) {
  if (!t[pos].v || (ql <= l && r <= qr)) return t[pos].v;
  int mid = (l + r) >> 1;
  if (qr <= mid)
    return query(t[pos].lc, l, mid, ql, qr);
  else if (ql > mid)
    return query(t[pos].rc, mid + 1, r, ql, qr);
  return query(t[pos].lc, l, mid, ql, qr) +
         query(t[pos].rc, mid + 1, r, ql, qr);
}
int rt[N];
int qrect(int x1, int x2, int y1, int y2) {
  if (y2 < -INF || y1 > INF) return 0;
  int pl = lower_bound(s + 1, s + kk + 1, pair<int, int>{x1, -INF}) - s - 1,
      pr = lower_bound(s + 1, s + kk + 1, pair<int, int>{x2 + 1, -INF}) - s - 1;
  return query(rt[pr], -INF, INF, y1, y2) - query(rt[pl], -INF, INF, y1, y2);
}
int main() {
  ios::sync_with_stdio(false);
  cin >> n >> kk;
  for (int i = 1; i <= n; i++) cin >> a[i].x >> a[i].y, a[i].t = INF;
  for (int i = 1; i <= kk; i++) cin >> s[i].first >> s[i].second;
  vector<Node> pp;
  for (int i = 1; i <= n; i++) pp.push_back(a[i]);
  for (int i = 1; i <= kk; i++) pp.push_back({s[i].first, s[i].second, -1});
  for (int i = 0; i < 4; i++) {
    sort(pp.begin(), pp.end(), [](Node a, Node b) {
      return a.x < b.x ||
             (a.x == b.x && (a.y < b.y || (a.y == b.y && a.t < b.t)));
    });
    vector<int> vv;
    vv.push_back(-INF);
    for (auto &j : pp) vv.push_back(j.y);
    sort(vv.begin(), vv.end());
    BIT c;
    c.sz = vv.size();
    for (auto &j : pp)
      if (j.t == -1)
        c.add(lower_bound(vv.begin(), vv.end(), j.y) - vv.begin(), j.x + j.y);
      else
        j.t = min(j.t, j.x + j.y -
                           c.query(lower_bound(vv.begin(), vv.end(), j.y) -
                                   vv.begin()));
    for (auto &j : pp)
      if (i & 1)
        j.x = -j.x;
      else
        j.y = -j.y;
  }
  n = 0;
  for (auto &j : pp)
    if (j.t != -1) a[++n] = j;
  for (int i = 1; i <= n; i++) a[i].x += a[i].y, a[i].y = a[i].x - 2 * a[i].y;
  for (int i = 1; i <= kk; i++)
    s[i].first += s[i].second, s[i].second = s[i].first - 2 * s[i].second;
  sort(s + 1, s + kk + 1);
  for (int i = 1; i <= kk; i++)
    modify(rt[i] = rt[i - 1], -INF, INF, s[i].second);
  sort(a + 1, a + n + 1, [](Node a, Node b) { return a.t > b.t; });
  a[n + 1].t = -INF;
  int mnx = INF, mxx = -INF, mny = INF, mxy = -INF, ans = a[1].t;
  for (int i = 1; i <= n; i++) {
    mnx = min(mnx, a[i].x);
    mny = min(mny, a[i].y);
    mxx = max(mxx, a[i].x);
    mxy = max(mxy, a[i].y);
    int l = max({a[i + 1].t, (mxx - mnx + 1) / 2, (mxy - mny + 1) / 2}),
        r = INF;
    if (!kk) {
      if (i == n) ans = l;
      continue;
    }
    while (l < r) {
      int mid = (l + r) >> 1, ex = mid - a[i + 1].t;
      if (qrect(mxx - mid - ex, mnx + mid + ex, mxy - mid - ex, mny + mid + ex))
        r = mid;
      else
        l = mid + 1;
    }
    int ex = l - a[i + 1].t,
        sum = qrect(mxx - l - ex, mnx + l + ex, mxy - l - ex, mny + l + ex);
    mxx -= l;
    mnx += l;
    mxy -= l;
    mny += l;
    if (mxx == mnx && mxy == mny && (mxx + mxy) % 2) {
      ++l;
      --mxx;
      ++mnx;
      --mxy;
      ++mny;
    } else if (i != n) {
      if (mxx == mnx) {
        if ((mxx + mxy) & 1)
          sum -= qrect(mxx - ex, mnx + ex, mxy - ex, mxy - ex);
        if ((mxx + mny) & 1)
          sum -= qrect(mxx - ex, mnx + ex, mny + ex, mny + ex);
      }
      if (mxy == mny) {
        if ((mxy + mxx) & 1)
          sum -= qrect(mxx - ex, mxx - ex, mxy - ex, mny + ex);
        if ((mxy + mnx) & 1)
          sum -= qrect(mnx + ex, mnx + ex, mxy - ex, mny + ex);
      }
      if (!sum) {
        ++l;
        --mxx;
        ++mnx;
        --mxy;
        ++mny;
      }
    }
    ans = min(ans, l);
    mxx += l;
    mnx -= l;
    mxy += l;
    mny -= l;
  }
  cout << ans << endl;
  return 0;
}
