#include <bits/stdc++.h>
using namespace std;
using LL = long long;
using DO = double;
using pii = pair<int, int>;
using VI = vector<int>;
const int NN = (1 << 17) + 10, inf = 1e9;
VI adj[NN];
int deg[NN];
int n, m;
void check(int u, int fa = 0, int deep = 0) {
  if (deep >= n) {
    puts("0");
    exit(0);
  }
  int deg = 0;
  for (auto v : adj[u])
    if (v != fa) {
      check(v, u, deep + 1);
      deg++;
    }
  if (deg > 2) {
    puts("0");
    exit(0);
  }
}
int solve1() {
  int root = -1;
  int ans = -1;
  for (int i = 1; i <= m; i++)
    if (deg[i] == 2) {
      int ok = 1;
      for (auto v : adj[i])
        if (deg[v] == 1) ok = 0;
      if (ok) {
        if (root != -1) return puts("0"), 0;
        root = i;
      } else {
        if (ans != -1) return puts("0"), 0;
        ans = i;
      }
    }
  if (root == -1 || ans == -1) return puts("0"), 0;
  check(root);
  cout << 1 << endl;
  cout << ans << endl;
}
int mx[NN][2];
void get_mx(int u, int fa = 0) {
  for (auto v : adj[u])
    if (v != fa) {
      get_mx(v, u);
      if (mx[v][0] + 1 > mx[u][1]) mx[u][1] = mx[v][0] + 1;
      if (mx[u][0] < mx[u][1]) swap(mx[u][0], mx[u][1]);
    }
}
void rget_mx(int u, int fa = 0) {
  for (auto v : adj[u])
    if (v != fa) {
      if (mx[v][0] == mx[u][0] - 1) {
        if (mx[v][1] < mx[u][1] + 1) mx[v][1] = mx[u][1] + 1;
      } else {
        if (mx[v][1] < mx[u][0] + 1) mx[v][1] = mx[u][0] + 1;
      }
      if (mx[v][0] < mx[v][1]) swap(mx[v][0], mx[v][1]);
      rget_mx(v, u);
    }
}
int per[NN];
int mxdp[NN], mndp[NN];
void dfs(int u, int fa = 0) {
  per[u] = 0;
  mxdp[u] = 0;
  mndp[u] = inf;
  int deg = 0;
  for (auto v : adj[u])
    if (v != fa) {
      dfs(v, u);
      if (per[v] == 0) per[u] = -1;
      deg++;
      mxdp[u] = max(mxdp[u], mxdp[v] + 1);
      mndp[u] = min(mndp[u], mndp[v] + 1);
    }
  if (mndp[u] == inf) mndp[u] = 0;
  if (deg == 0)
    per[u] = 1;
  else if (deg == 2) {
    if (per[u] == -1) {
      per[u] = 0;
      return;
    }
    if (mndp[u] != mxdp[u])
      per[u] = 0;
    else
      per[u] = 1;
  } else
    per[u] = 0;
}
int key;
void DFS(int u, int fa = 0, int dp = 0) {
  int deg = 0, u1 = -1, u2 = -1, u3 = -1;
  for (auto v : adj[u])
    if (v != fa) {
      deg++;
      if (u1 == -1)
        u1 = v;
      else if (u2 == -1)
        u2 = v;
      else
        u3 = v;
    }
  if (deg < 2) return;
  if (deg == 2) {
    if (per[u1] == 0 && per[u2] == 0) return;
    if (per[u1] && per[u2]) return;
    if (per[u1]) swap(u1, u2);
    if (mxdp[u2] + dp != n - 2) return;
    DFS(u1, u, dp + 1);
  } else {
    if (per[u1] == 0 || per[u2] == 0 || per[u3] == 0) return;
    if (mxdp[u1] > mxdp[u2]) swap(u1, u2);
    if (mxdp[u2] > mxdp[u3]) swap(u2, u3);
    if (mxdp[u1] > mxdp[u2]) swap(u1, u2);
    if (mxdp[u1] != mxdp[u2] || mxdp[u1] + 1 != mxdp[u3] ||
        mxdp[u3] + dp != n - 2)
      return;
    key = u;
  }
}
int can(int root) {
  dfs(root);
  if (mxdp[root] != n - 1 || mndp[root] != n - 2) return 0;
  key = 0;
  DFS(root);
  return key;
}
void solve() {
  get_mx(1);
  rget_mx(1);
  int root = -1, deg4 = 0;
  for (int i = 1; i <= m; i++)
    if (deg[i]) {
      if (deg[i] == 2) {
        if (root != -1) {
          puts("0");
          exit(0);
        }
        root = i;
      }
      if (deg[i] == 4) deg4++;
    }
  VI res;
  if (deg4 > 1) {
    puts("0");
    exit(0);
  }
  if (root != -1) {
    int t = can(root);
    if (t) res.push_back(t);
  } else {
    for (int i = 1; i <= m; i++)
      if (deg[i] && mx[i][0] <= n - 1) {
        int t = can(i);
        if (t) res.push_back(t);
      }
  }
  sort(res.begin(), res.end());
  res.resize(unique(res.begin(), res.end()) - res.begin());
  cout << res.size() << endl;
  for (auto r : res) cout << r << ' ';
}
int main() {
  cin >> n;
  m = (1 << n) - 1;
  for (int i = 0; i < m - 2; i++) {
    int u, v;
    scanf("%d %d", &u, &v);
    adj[u].push_back(v);
    adj[v].push_back(u);
    deg[u]++;
    deg[v]++;
  }
  if (n == 2) {
    puts("2");
    for (int i = 1; i <= 3; i++)
      if (deg[i]) cout << i << ' ';
    return 0;
  }
  int leaf = 0;
  for (int i = 1; i <= m; i++) {
    if (deg[i] == 1) leaf++;
    if (deg[i] > 4) return puts("0"), 0;
  }
  if (leaf < (m + 1) / 2 - 1 || leaf > (m + 1) / 2) return puts("0"), 0;
  if (leaf == (m + 1) / 2 - 1)
    solve1();
  else
    solve();
  return 0;
}
