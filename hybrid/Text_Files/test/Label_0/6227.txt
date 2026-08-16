#include <bits/stdc++.h>
using namespace std;
const int maxn = 1079;
class edge {
 public:
  int u, v, w;
};
class dsu {
  vector<int> p, b, siz;
  int highest(int v) {
    if (v == p[v]) return v;
    int r = highest(p[v]);
    b[v] = b[p[v]] ^ b[v];
    return p[v] = r;
  }

 public:
  dsu(int n) : p(vector<int>(n)), b(vector<int>(n, 0)), siz(vector<int>(n, 1)) {
    clear();
  }
  void clear() {
    for (int i = 0; i < b.size(); i++) {
      b[i] = 0, siz[i] = 1, p[i] = i;
    }
  }
  bool parity(int v) {
    highest(v);
    return b[v];
  }
  int merge(int u, int v) {
    int ua = highest(u), va = highest(v);
    if (ua == va) {
      if (parity(u) == parity(v)) return 0;
      return 1;
    }
    if (siz[ua] < siz[va]) swap(ua, va);
    b[va] = parity(u) ^ 1 ^ parity(v);
    siz[ua] += siz[va];
    p[va] = ua;
    return 2;
  }
};
dsu u(maxn);
vector<vector<edge> > st;
vector<edge> merge(vector<edge>& a, vector<edge>& b) {
  u.clear();
  vector<edge> c;
  int ai = 0, bi = 0;
  while (ai < a.size() || bi < b.size()) {
    edge i;
    if (bi == b.size() || (ai < a.size() && a[ai].w > b[bi].w))
      i = a[ai++];
    else
      i = b[bi++];
    int res = u.merge(i.u, i.v);
    if (res == 0 || res == 2) c.push_back(i);
    if (!res) break;
  }
  return c;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m, q;
  cin >> n >> m >> q;
  vector<edge> e(m);
  st.resize(2 * m);
  for (int i = 0; i < m; i++) {
    cin >> e[i].u >> e[i].v >> e[i].w;
    e[i].u--;
    e[i].v--;
    st[m + i].push_back(e[i]);
  }
  for (int i = m - 1; i; i--) st[i] = merge(st[i << 1], st[i << 1 | 1]);
  while (q--) {
    int l, r;
    cin >> l >> r;
    l--;
    vector<edge> v;
    for (l += m, r += m; l < r; l >>= 1, r >>= 1) {
      if (l & 1) v = merge(v, st[l++]);
      if (r & 1) v = merge(v, st[--r]);
    }
    u.clear();
    int ans = -1;
    for (int i = 0; i < v.size(); i++) {
      if (!u.merge(v[i].u, v[i].v)) {
        ans = v[i].w;
        break;
      }
    }
    cout << ans << "\n";
  }
  return 0;
}
