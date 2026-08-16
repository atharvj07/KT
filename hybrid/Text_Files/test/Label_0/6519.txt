#include <bits/stdc++.h>
using namespace std;
int N, M;
int u, v;
vector<int> adj[100005];
int ans[100005];
bool vis[100005];
int par[100005];
bool can[100005];
vector<int> leaf;
vector<int> body;
bool AC;
void print() {
  if (AC) return;
  cout << "YES\n";
  for (int i = 1; i <= N; i++) {
    cout << ans[i];
    if (i < N)
      cout << " ";
    else
      cout << "\n";
  }
  AC = 1;
}
void DFS(int u, int p = 0) {
  vis[u] = 1;
  par[u] = p;
  if (AC) return;
  for (int v : adj[u]) {
    if (v == p) continue;
    if (AC) continue;
    if (vis[v]) {
      int tmp = u;
      while (tmp != 0) {
        ans[tmp] = 1;
        tmp = par[tmp];
      }
      print();
    } else
      DFS(v, u);
  }
}
void DFS2(int u) {
  vis[u] = 1;
  if (adj[u].size() <= 1)
    leaf.push_back(u);
  else
    body.push_back(u);
  for (int v : adj[u]) {
    if (vis[v]) continue;
    DFS2(v);
  }
}
void DFS3(int u, int p, vector<int> &pp) {
  pp.push_back(u);
  for (int v : adj[u]) {
    if (v == p) continue;
    DFS3(v, u, pp);
  }
}
long long cek(int u, int p) {
  long long res = -1LL * ans[u] * ans[u];
  for (int v : adj[u]) {
    if (v == p) continue;
    res += cek(v, u) + 1LL * ans[u] * ans[v];
  }
  return res;
}
void solve() {
  AC = 0;
  cin >> N >> M;
  for (int i = 1; i <= N; i++) {
    par[i] = 0;
    vis[i] = 0;
    adj[i].clear();
    ans[i] = 0;
  }
  for (int i = 1; i <= M; i++) {
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  bool ok = 0;
  for (int i = 1; i <= N; i++) {
    if (AC) break;
    if (vis[i] == 0) DFS(i);
    if (adj[i].size() > 2) ok = 1;
  }
  for (int i = 1; i <= N; i++) vis[i] = 0;
  for (int i = 1; i <= N; i++) {
    if (AC) break;
    if (vis[i] == 0) {
      leaf.clear();
      body.clear();
      DFS2(i);
      if (leaf.size() > 3) {
        for (int now : leaf) {
          ans[now] = 1;
        }
        for (int now : body) ans[now] = 2;
        print();
        break;
      }
    }
  }
  vector<int> ver[3];
  for (int u = 1; u <= N; u++) {
    if (AC) break;
    if (adj[u].size() != 3) continue;
    int cnt = 0;
    for (int v : adj[u]) {
      ver[cnt].clear();
      DFS3(v, u, ver[cnt]);
      cnt++;
    }
    if (ver[0].size() > ver[1].size()) swap(ver[1], ver[0]);
    if (ver[1].size() > ver[2].size()) swap(ver[1], ver[2]);
    if (ver[0].size() > ver[1].size()) swap(ver[1], ver[0]);
    if (ver[0].size() > 1) {
      int aa = 2;
      ans[u] = 3;
      ans[ver[0][0]] = 2;
      ans[ver[1][0]] = 2;
      ans[ver[2][0]] = 2;
      ans[ver[0][1]] = 1;
      ans[ver[1][1]] = 1;
      ans[ver[2][1]] = 1;
      print();
    } else if (ver[0].size() == 1 && ver[1].size() > 1) {
      if (ver[2].size() > 500) ver[2].resize(500);
      if (ver[1].size() > 500) ver[1].resize(500);
      int now = 2 * (ver[1].size() + 1) * (ver[2].size() + 1);
      ans[u] = now;
      ans[ver[0][0]] = now / 2;
      int krg = now / (ver[1].size() + 1), tmp = now - krg;
      for (int aa : ver[1]) {
        ans[aa] = tmp;
        tmp -= krg;
      }
      krg = now / (ver[2].size() + 1), tmp = now - krg;
      for (int aa : ver[2]) {
        ans[aa] = tmp;
        tmp -= krg;
      }
      if (cek(u, 0) >= 0) print();
      for (int aa : ver[0]) ans[aa] = 0;
      for (int aa : ver[1]) ans[aa] = 0;
      for (int aa : ver[2]) ans[aa] = 0;
    }
  }
  if (!AC) cout << "NO\n";
}
int main() {
  ios_base::sync_with_stdio(0);
  int tc;
  cin >> tc;
  while (tc--) {
    solve();
  }
  cin >> N;
}
