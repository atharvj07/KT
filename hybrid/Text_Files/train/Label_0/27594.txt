#include <bits/stdc++.h>
using namespace std;
vector<long long int> adj[100005];
long long int n;
long long int p[100005][35];
long long int parent[100005];
long long int level[100005];
void dfs(long long int v, long long int prev) {
  for (auto i : adj[v]) {
    if (i == prev) continue;
    parent[i] = v;
    level[i] = level[v] + 1;
    dfs(i, v);
  }
}
void preprocess() {
  for (long long int i = 1; i < 100005; i++) {
    for (long long int j = 0; j < 35; j++) {
      p[i][j] = -1;
    }
  }
  for (long long int i = 1; i < n + 1; i++) {
    p[i][0] = parent[i];
  }
  for (long long int j = 1; j < int(log2(n)) + 1; j++) {
    for (long long int i = 1; i < n + 1; i++) {
      if (p[i][j - 1] != -1) p[i][j] = p[p[i][j - 1]][j - 1];
    }
  }
}
long long int findnparent(long long int u, long long int dist) {
  while (dist > 0) {
    int raise_by = log2(dist);
    u = p[u][raise_by];
    dist -= (1 << raise_by);
  }
  return u;
}
long long int LCA(long long int u, long long int v) {
  if (level[u] < level[v]) swap(u, v);
  int dist = level[u] - level[v];
  u = findnparent(u, dist);
  if (u == v) return u;
  for (long long int j = 35 - 1; j > -1; j--) {
    if (p[u][j] != -1 and (p[u][j] != p[v][j])) {
      u = p[u][j];
      v = p[v][j];
    }
  }
  return parent[u];
}
long long dis(long long x, long long y) {
  long long l1 = LCA(x, y);
  return level[x] + level[y] - 2 * level[l1];
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cout.precision(15);
  long long int e, f, q;
  cin >> n;
  for (long long int i = 0; i < n - 1; i++) {
    cin >> e >> f;
    adj[e].push_back(f);
    adj[f].push_back(e);
  }
  level[1] = 0;
  parent[1] = 1;
  dfs(1, 0);
  preprocess();
  cin >> q;
  while (q--) {
    long long int x, y, a, b, k;
    cin >> x >> y >> a >> b >> k;
    long long int lab = LCA(a, b);
    long long int dab = level[a] + level[b] - 2 * level[lab];
    long long int lax = LCA(a, x);
    long long int dax = level[a] + level[x] - 2 * level[lax];
    long long int lby = LCA(y, b);
    long long int dby = level[b] + level[y] - 2 * level[lby];
    long long int lay = LCA(a, y);
    long long int day = level[a] + level[y] - 2 * level[lay];
    long long int lbx = LCA(x, b);
    long long int dbx = level[x] + level[b] - 2 * level[lbx];
    if (k >= (1 + dax + dby) && (k - 1 - dax - dby) % 2 == 0)
      cout << "YES\n";
    else if (k >= (1 + day + dbx) && (k - 1 - day - dbx) % 2 == 0)
      cout << "YES\n";
    else if (k >= dab && (k - dab) % 2 == 0)
      cout << "YES\n";
    else
      cout << "NO\n";
  }
}
