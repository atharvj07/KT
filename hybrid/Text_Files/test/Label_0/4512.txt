#include <bits/stdc++.h>
using namespace std;
long long int t[4000005], lazy[4000005];
vector<pair<long long int, long long int> > v1;
void push(int v) {
  t[v * 2] += lazy[v];
  lazy[v * 2] += lazy[v];
  t[v * 2 + 1] += lazy[v];
  lazy[v * 2 + 1] += lazy[v];
  lazy[v] = 0;
}
void build(long long int v, long long int tl, long long int tr) {
  if (tl == tr) {
    t[v] = 0 - v1[tl].second;
  } else {
    int tm = (tl + tr) / 2;
    build(v * 2, tl, tm);
    build(v * 2 + 1, tm + 1, tr);
    t[v] = max(t[v * 2], t[v * 2 + 1]);
  }
}
void update(int v, int tl, int tr, int l, int r, int addend) {
  if (l > r) return;
  if (l == tl && tr == r) {
    t[v] += addend;
    lazy[v] += addend;
  } else {
    push(v);
    int tm = (tl + tr) / 2;
    update(v * 2, tl, tm, l, min(r, tm), addend);
    update(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, addend);
    t[v] = max(t[v * 2], t[v * 2 + 1]);
  }
}
int query(int v, int tl, int tr, int l, int r) {
  if (l > r) return -100000000000000;
  if (l <= tl && tr <= r) return t[v];
  push(v);
  int tm = (tl + tr) / 2;
  return max(query(v * 2, tl, tm, l, min(r, tm)),
             query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r));
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long int n, m, p, l, r, i, f;
  cin >> n >> m >> p;
  vector<pair<long long int, long long int> > a;
  vector<pair<pair<long long int, long long int>, long long int> > vv;
  map<pair<long long int, long long int>, long long int> mm;
  for (i = 0; i < n; i++) {
    cin >> l >> r;
    a.push_back({l, r});
  }
  v1.push_back({0, 0});
  for (i = 0; i < m; i++) {
    cin >> l >> r;
    v1.push_back({l, r});
  }
  sort(v1.begin(), v1.end());
  vector<long long int> h;
  for (i = 1; i <= m; i++) {
    h.push_back(v1[i].first);
  }
  for (i = 0; i < p; i++) {
    cin >> l >> r >> f;
    vv.push_back({{l, r}, f});
  }
  sort(vv.begin(), vv.end());
  sort(a.begin(), a.end());
  build(1, 1, m);
  long long int pt = 0;
  long long int ans = -100000000000000;
  long long int d;
  for (i = 0; i < n; i++) {
    while (1) {
      if (pt >= p) break;
      if (vv[pt].first.first >= a[i].first) break;
      d = upper_bound(h.begin(), h.end(), vv[pt].first.second) - h.begin();
      update(1, 1, m, d + 1, m, vv[pt].second);
      pt++;
    }
    ans = max(ans, t[1] - a[i].second);
  }
  cout << ans;
}
