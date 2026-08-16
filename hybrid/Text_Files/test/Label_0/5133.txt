#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 10;
int b[maxn << 3];
int id[maxn << 3];
int n, m;
struct seg {
  int l, r, t, id;
};
vector<int> val;
int pos(int x) {
  return lower_bound(val.begin(), val.end(), x) - val.begin() + 1;
}
void build(int o, int l, int r) {
  if (r == l) {
    b[o] = -1e9;
    return;
  }
  build((o * 2), l, ((l + r) >> 1));
  build((o * 2 + 1), ((l + r) >> 1) + 1, r);
  b[o] = max(b[(o * 2)], b[(o * 2 + 1)]);
}
void A(int o, int l, int r, int qd, int d1, int d2) {
  if (r == l) {
    b[o] = d1;
    id[o] = d2;
    return;
  }
  if (qd <= ((l + r) >> 1))
    A((o * 2), l, ((l + r) >> 1), qd, d1, d2);
  else
    A((o * 2 + 1), ((l + r) >> 1) + 1, r, qd, d1, d2);
  b[o] = max(b[(o * 2)], b[(o * 2 + 1)]);
}
int Q(int o, int l, int r, int qd, int d) {
  if (b[o] < d) return -1;
  int ans;
  if (r == l) {
    return id[o];
  }
  if (qd <= ((l + r) >> 1)) {
    ans = Q((o * 2), l, ((l + r) >> 1), qd, d);
    if (ans != -1) return ans;
  }
  return Q((o * 2 + 1), ((l + r) >> 1) + 1, r, qd, d);
}
int ans[maxn];
int main() {
  scanf("%d%d", &n, &m);
  vector<seg> v;
  for (int i = 1; i <= n + m; ++i) {
    int l, r, t;
    scanf("%d%d%d", &l, &r, &t);
    v.push_back({l, r, t, i});
    val.push_back(t);
  }
  sort(val.begin(), val.end());
  val.resize(unique(val.begin(), val.end()) - val.begin());
  sort(v.begin(), v.end(), [](const seg& a, const seg& b) {
    if (a.l == b.l) return a.id < b.id;
    return a.l < b.l;
  });
  build(1, 1, val.size());
  for (int i = 0; i < v.size(); ++i) {
    if (v[i].id <= n) {
      A(1, 1, val.size(), pos(v[i].t), v[i].r, v[i].id);
    } else {
      ans[v[i].id - n] = Q(1, 1, val.size(), pos(v[i].t), v[i].r);
    }
  }
  for (int i = 1; i <= m; ++i) printf("%d%c", ans[i], " \n"[i == n]);
}
