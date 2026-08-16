#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 3;
int n, m, q, x, y, zd, l, t, aa, tin[N], tout[N], d[N], up[N][20];
vector<int> a[N], b[N], c[N][20], rez;
vector<int> me(vector<int> u, vector<int> v) {
  vector<int> z;
  int i = 0, j = 0, k = 10;
  int J = v.size();
  int I = u.size();
  if (I == 0) {
    z = v;
  } else if (J == 0) {
    z = u;
  } else {
    while ((i + j < k) && (i + j < I + J)) {
      if (i == I) {
        z.push_back(v[j++]);
      } else if (j == J) {
        z.push_back(u[i++]);
      } else if (u[i] < v[j]) {
        z.push_back(u[i++]);
      } else if (u[i] > v[j]) {
        z.push_back(v[j++]);
      } else {
        ++k;
        ++i;
      }
    }
  }
  return z;
}
void dfs(int v, int p) {
  tin[v] = t++;
  up[v][0] = p;
  d[v] = d[p] + 1;
  for (int i = 1; i <= l; ++i) {
    up[v][i] = up[up[v][i - 1]][i - 1];
    c[v][i] = me(c[v][i - 1], c[up[v][i - 1]][i - 1]);
  }
  for (int u : a[v]) {
    if (u != p) {
      dfs(u, v);
    }
  }
  tout[v] = t++;
}
bool is_parent(int u, int v) { return tin[u] <= tin[v] && tout[u] >= tout[v]; }
void lca(int u, int v) {
  if (is_parent(u, v)) {
    int j = d[v] - d[u];
    for (int i = l; i >= 0; --i) {
      if (j - (1 << i) >= 0) {
        j -= (1 << i);
        rez = me(rez, c[v][i]);
        v = up[v][i];
      }
    }
    rez = me(rez, c[v][0]);
  } else if (!is_parent(v, u)) {
    for (int i = l; i >= 0; --i) {
      if (!is_parent(up[u][i], v)) {
        rez = me(rez, c[u][i]);
        u = up[u][i];
      }
    }
    rez = me(rez, c[u][1]);
  }
}
int main() {
  cin >> n >> m >> q;
  for (int i = 0; i < n - 1; ++i) {
    cin >> x >> y;
    a[x].push_back(y);
    a[y].push_back(x);
  }
  for (int i = 1; i <= m; ++i) {
    cin >> x;
    c[x][0].push_back(i);
  }
  l = ceil(log2(n));
  a[0].push_back(1);
  dfs(0, 0);
  for (int i = 0; i < q; ++i) {
    cin >> x >> y >> aa;
    if (x != y) {
      rez.clear();
      lca(x, y);
      lca(y, x);
      if (aa > rez.size()) {
        aa = rez.size();
      }
      cout << aa << " ";
      for (int j = 0; j < aa; ++j) {
        cout << rez[j] << " ";
      }
      cout << "\n";
    } else {
      if (aa > c[x][0].size()) {
        aa = c[x][0].size();
      }
      cout << aa << " ";
      for (int j = 0; j < aa; ++j) {
        cout << c[x][0][j] << " ";
      }
      cout << "\n";
    }
  }
  return 0;
}
