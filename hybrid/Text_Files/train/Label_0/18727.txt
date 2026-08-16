#include <bits/stdc++.h>
using namespace std;
struct stree {
  int n;
  vector<vector<int> > t, d;
  vector<int> L, R;
  stree(){};
  stree(vector<int> a, vector<int> b) {
    n = 1;
    while (n < a.size()) n *= 2;
    t.resize(n + n);
    d.resize(n + n);
    L.resize(n + n);
    R.resize(n + n);
    for (int i = 0; i < n; ++i) {
      t[i + n].push_back(i < a.size() ? a[i] : 0);
      d[i + n].push_back(i < a.size() ? b[i] : 0);
      L[i + n] = R[i + n] = i;
    }
    for (int i = n - 1; i > 0; --i) {
      L[i] = L[i + i];
      R[i] = R[i + i + 1];
      int p, q, k;
      p = q = 0;
      k = t[i + i].size();
      bool fl;
      while (p < k || q < k) {
        if (p == k)
          fl = true;
        else if (q == k)
          fl = false;
        else
          fl = (d[i + i + 1][q] < d[i + i][p]);
        if (fl) {
          t[i].push_back(t[i + i + 1][q]);
          d[i].push_back(d[i + i + 1][q++]);
        } else {
          t[i].push_back(t[i + i][p]);
          d[i].push_back(d[i + i][p++]);
        }
      }
      for (int j = 1; j < t[i].size(); ++j) t[i][j] = min(t[i][j], t[i][j - 1]);
    }
  }
  long long num(int v, int l, int r, int dep) {
    if (L[v] > r || l > R[v]) return 1e9 + 5;
    if (L[v] == l && R[v] == r) {
      int j = upper_bound(d[v].begin(), d[v].end(), dep) - d[v].begin();
      return (j ? t[v][j - 1] : 1e9 + 5);
    } else {
      int tm = (L[v] + R[v]) / 2;
      return min(num(v + v, l, min(r, tm), dep),
                 num(v + v + 1, max(l, tm + 1), r, dep));
    }
  }
};
int n, r, x, y, k, q, last;
vector<vector<int> > g;
vector<int> a, aa, bb, u, in, ou, de;
void dfs(int v, int dep) {
  u[v] = 1;
  aa.push_back(a[v]);
  bb.push_back(dep);
  de[v] = dep;
  in[v] = aa.size() - 1;
  for (int i = 0; i < g[v].size(); ++i) {
    int to = g[v][i];
    if (!u[to]) dfs(to, dep + 1);
  }
  ou[v] = aa.size() - 1;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin >> n >> r;
  --r;
  a.resize(n);
  for (int i = 0; i < n; ++i) cin >> a[i];
  g.resize(n);
  for (int i = 0; i < n - 1; ++i) {
    cin >> x >> y;
    --x;
    --y;
    g[x].push_back(y);
    g[y].push_back(x);
  }
  de.resize(n);
  in.resize(n);
  ou.resize(n);
  u.assign(n, 0);
  dfs(r, 0);
  stree t(aa, bb);
  last = 0;
  cin >> q;
  while (q--) {
    cin >> x >> k;
    x = (x + last) % n;
    k = (k + last) % n;
    last = t.num(1, in[x], ou[x], de[x] + k);
    cout << last << "\n";
  }
  return 0;
}
