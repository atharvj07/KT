#include <bits/stdc++.h>
using namespace std;
const int N = 300005;
const int K = 26;
vector<pair<int, char> > g[N];
int n, tr[N << 1][K], sz[N << 1];
int ans[N], ptr;
void dfs(int v, int p) {
  sz[v] = 1;
  for (auto x : g[v]) {
    if (x.first != p) {
      tr[v][x.second - 'a'] = x.first;
      dfs(x.first, v);
      sz[v] += sz[x.first];
    }
  }
}
void clear() {
  for (int i = 0; i < K; i++) {
    tr[ptr][i] = -1;
  }
}
int combine(int u, int v) {
  clear();
  int rt = ptr;
  ptr++;
  for (int i = 0; i < K; i++) {
    if (tr[u][i] != -1 && tr[v][i] != -1)
      tr[rt][i] = combine(tr[u][i], tr[v][i]);
    else if (tr[u][i] != -1)
      tr[rt][i] = tr[u][i];
    else if (tr[v][i] != -1)
      tr[rt][i] = tr[v][i];
  }
  sz[rt] = 1;
  for (int i = 0; i < K; i++) {
    if (tr[rt][i] != -1) sz[rt] += sz[tr[rt][i]];
  }
  return rt;
}
void compute(int v, int dep) {
  if (sz[v] == 1) return;
  int bg = -1;
  for (int i = 0; i < K; i++) {
    if (tr[v][i] != -1) {
      compute(tr[v][i], dep + 1);
      if (bg == -1 || sz[tr[v][bg]] < sz[tr[v][i]]) bg = i;
    }
  }
  int tot = 0;
  ptr = n + 1;
  int rt = tr[v][bg];
  for (int i = 0; i < K; i++) {
    if (tr[v][i] != -1 && bg != i) {
      rt = combine(rt, tr[v][i]);
    }
  }
  ans[dep] += sz[v] - sz[rt];
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cout << setprecision(32);
  cin >> n;
  memset(tr, -1, sizeof(tr));
  memset(sz, 0, sizeof(sz));
  int u, v;
  char ch;
  for (int i = 1; i < n; i++) {
    cin >> u >> v >> ch;
    g[u].push_back({v, ch});
    g[v].push_back({u, ch});
  }
  dfs(1, 0);
  memset(ans, 0, sizeof(ans));
  compute(1, 1);
  int ind = 1;
  for (int i = 1; i <= n; i++) {
    if (ans[ind] < ans[i]) ind = i;
  }
  cout << n - ans[ind] << '\n';
  cout << ind << '\n';
  return 0;
}
