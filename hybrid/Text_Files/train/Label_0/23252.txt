#pragma GCC optimize "Ofast"

#define X first
#define Y second

#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

constexpr int N = 35;

int n, deg[N], nei[N], col[N];
vector<PII> polys[N];
vector<int> adj[N];
int cnt[N][3];

inline int cross(const PII &p0, const PII &p1) {
  return p0.X * p1.Y - p0.Y * p0.X;
}
inline LL cross(LL x0, LL x1, LL y0, LL y1, LL z0, LL z1) {
  LL x = y0 * z1 - z0 * y1;
  LL y = x1 * z0 - x0 * z1;
  LL z = x0 * y1 - x1 * y0;
  return x * x + y * y + z * z;
}
inline bool intersect(LL l0, LL r0, LL l1, LL r1) {
  if(l0 > r0) swap(l0, r0);
  if(l1 > r1) swap(l1, r1);
  if(r1 < r0) {
    swap(r0, r1);
    swap(l0, l1);
  }
  return r0 - l1 > 0;
}
inline bool overlap(const PII &p0, const PII &p1, const PII &p2, const PII &p3) {
  LL a0 = (p1.X - p0.X), b0 = (p0.Y - p1.Y), c0 = p0.Y *  a0 + p0.X * b0;
  LL a1 = (p3.X - p2.X), b1 = (p2.Y - p3.Y), c1 = p2.Y *  a1 + p2.X * b1;
  if(cross(a0, a1, b0, b1, c0, c1) != 0)
    return false;
  if(a0 == 0)
    return intersect(p0.Y, p1.Y, p2.Y, p3.Y);
  else
    return intersect(p0.X, p1.X, p2.X, p3.X);
}
bool touch(int u, int v) {
  for(size_t i = 1; i < polys[u].size(); ++i)
    for(size_t j = 1; j < polys[v].size(); ++j)
      if(overlap(polys[u][i-1], polys[u][i], polys[v][j-1], polys[v][j]))
        return true;
  return false;
}
void init() {
  fill_n(nei, n, 0);
  fill_n(deg, n, 0);
  for(int i = 0; i < n; ++i) {
    polys[i].clear();
    adj[i].clear();
    int m; scanf("%d", &m);
    for(int j = 0; j < m; ++j) {
      int x, y; scanf("%d %d", &x, &y);
      polys[i].emplace_back(x, y);
    }
    polys[i].push_back(polys[i][0]);
  }
  for(int i = 0; i < n; ++i)
    for(int j = i+1; j < n; ++j) {
      if(touch(i, j)) {
        ++deg[i];
        ++deg[j];
        adj[i].push_back(j);
        adj[j].push_back(i);
      }
    }
}
void dfs(int u, vector<bool> &vis, vector<int> &ord) {
  for(int v : adj[u])
    ++nei[v];
  while(true) {
    int mx = -1, mxv = -1;
    for(int v : adj[u])
      if(!vis[v])
        if(nei[v] > mx) {
          mx = nei[v];
          mxv = v;
        }
    if(mxv == -1)
      break;
    ord.push_back(mxv);
    vis[mxv] = true;
    dfs(mxv, vis, ord);
  }
}
bool color(int i, int cc, const int nc, const vector<int> &ord) {
  const int &u = ord[i];
  col[u] = cc;
  for(int v : adj[u])
    ++cnt[v][cc];
  if(i + 1 == (int)ord.size())
    return true;
  for(int c = 0; c < nc; ++c)
    if(cnt[ord[i + 1]][c] == 0)
      if(color(i+1, c, nc, ord))
        return true;
  for(int v : adj[u])
    --cnt[v][cc];
  col[u] = -1;
  return false;
}
bool go(int nc, const vector<int> &ord) {
  for(int x : ord) {
    fill_n(cnt[x], nc, 0);
    col[x] = -1;
  }
  return color(0, 0, nc, ord);
}
int solve() {
  init();
  for(int i = 0; i < n; ++i)
    sort(adj[i].begin(), adj[i].end(), [](int u, int v) { return deg[u] > deg[v]; });
  vector<int> pre_ord(n, 0);
  iota(pre_ord.begin(), pre_ord.end(), 0);
  sort(pre_ord.begin(), pre_ord.end(), [](int i, int j) { return deg[i] > deg[j]; });
  vector<vector<int>> ord;
  vector<bool> vis(n, false);
  for(int i : pre_ord)
    if(!vis[i]) {
      ord.push_back(vector<int>(1, i));
      vis[i] = true;
      dfs(i, vis, ord.back());
    }
  for(int i = 1; i < 4; ++i) {
    size_t j = 0;
    for(; j < ord.size(); ++j)
      if(!go(i, ord[j]))
        break;
    if(j == ord.size()) {
      for(size_t k = 0; k < ord.size(); ++k) {
        for(int u : ord[k]) {
          assert(col[u] != -1);
          for(int v : adj[u])
            assert(col[u] != col[v]);
        }
      }
      return i;
    }
  }
  return 4;
}

int main() {
  while(scanf("%d", &n) == 1 && n)
    printf("%d\n", solve());
}