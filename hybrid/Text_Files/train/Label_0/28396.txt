#include <bits/stdc++.h>
using namespace std;
const int N = 500 * 1000 + 10;
int t, n, m, par[N], deg[N], st, en, h[N], mn, comp[N], sv[2][N];
vector<int> adj[N];
bool vis[N], ans[N];
void gclear() {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 2; j++) sv[j][i] = -1;
    adj[i].clear();
    comp[i] = ans[i] = vis[i] = 0;
    par[i] = -1;
  }
  mn = 1 << 30;
  st = en = -1;
}
void print() {
  int res = n;
  for (int v = 0; v < n; v++) res -= ans[v];
  if (!res) return cout << "No\n", void();
  cout << "Yes\n" << res << '\n';
  for (int v = 0; v < n; v++)
    if (!ans[v]) cout << v + 1 << ' ';
  cout << '\n';
}
void dfs(int v) {
  vis[v] = true;
  for (int u : adj[v]) {
    if (deg[u] ^ 2) continue;
    if (!vis[u])
      h[u] = h[v] + 1, par[u] = v, dfs(u);
    else if (par[v] ^ u && abs(h[v] - h[u]) < mn) {
      st = u, en = v;
      if (h[st] > h[en]) swap(st, en);
      mn = h[en] - h[st];
    }
  }
}
void bfs(int x) {
  queue<int> q;
  fill(vis, vis + n, 0);
  q.push(x), vis[x] = true;
  while (!q.empty()) {
    int v = q.front();
    if (deg[v] == 1 && x ^ v) {
      en = v;
      break;
    }
    q.pop();
    for (int u : adj[v])
      if (!vis[u]) vis[u] = true, par[u] = v, q.push(u);
  }
  while (en ^ -1) ans[en] = true, en = par[en];
  print();
}
void bf(int v, int x) {
  comp[v] = x;
  for (int u : adj[v])
    if (!comp[u]) h[u] = h[v] + 1, par[u] = v, bf(u, x);
}
bool chck(int s, int e) {
  while (e ^ -1) {
    if (s == e) return 1;
    e = par[e];
  }
  return 0;
}
void solve() {
  int lst = -1, cnt = 0;
  for (int v = 0; v < n; v++) {
    deg[v] = (int)adj[v].size() % 3;
    if (!deg[v]) {
      ans[v] = true;
      return print();
    } else if (deg[v] == 1)
      lst = v, cnt++;
  }
  if (cnt > 1) return bfs(lst);
  for (int v = 0; v < n; v++)
    if (deg[v] == 2 && !vis[v]) {
      dfs(v);
      if (st ^ -1 && en ^ -1) {
        if (chck(st, en)) {
          while (en ^ st) ans[en] = true, en = par[en];
          ans[st] = true;
          return print();
        } else
          st = -1, en = -1, mn = 1 << 30;
      }
    }
  if (cnt) {
    fill(par, par + n, -1);
    cnt = 0;
    comp[lst] = -1;
    set<int> num;
    for (int v : adj[lst]) {
      if (!comp[v])
        sv[0][++cnt] = v, bf(v, cnt);
      else {
        num.insert(comp[v]);
        if ((sv[1][comp[v]] ^ -1 && h[sv[1][comp[v]]] > h[v]) ||
            sv[1][comp[v]] == -1)
          sv[1][comp[v]] = v;
      }
    }
    cnt = 0;
    if (num.size() > 1) {
      ans[lst] = true;
      for (int x : num) {
        cnt++;
        if (cnt > 2) break;
        while (sv[0][x] ^ sv[1][x])
          ans[sv[1][x]] = true, sv[1][x] = par[sv[1][x]];
        ans[sv[0][x]] = true;
      }
      return print();
    }
  }
  cout << "No\n";
}
int main() {
  ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
  cin >> t;
  while (t--) {
    cin >> n >> m;
    gclear();
    for (int i = 0, u, v; i < m; i++)
      cin >> u >> v, adj[--u].push_back(--v), adj[v].push_back(u);
    solve();
  }
}
