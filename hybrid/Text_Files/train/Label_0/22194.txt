#include <bits/stdc++.h>
using namespace std;
const long long int N = 200010;
vector<long long int> adj[N];
long long int n, m;
vector<long long int> ar, hr, size, g, b;
bool ans;
void dfs(long long int v, long long int p) {
  size[v] = ar[v];
  long long int gu = 0, bu = 0;
  for (auto u : adj[v]) {
    if (u == p) {
      continue;
    }
    dfs(u, v);
    size[v] += size[u];
    gu += g[u];
    bu += b[u];
  }
  long long int s = size[v];
  long long int h = hr[v];
  if (!((s + h) % 2 == 0 && s - h >= 0)) {
    ans = false;
    return;
  }
  if (!(h >= -s && h <= s)) {
    ans = false;
    return;
  }
  g[v] = (s + h) / 2;
  b[v] = (s - h) / 2;
  if (g[v] + b[v] - gu - bu != ar[v]) {
    ans = false;
    return;
  }
  if (!(g[v] >= gu)) {
    ans = false;
    return;
  }
}
void init() {
  ar.clear();
  hr.clear();
  size.clear();
  g.clear();
  b.clear();
  for (long long int i = 0; i <= n; ++i) {
    adj[i].clear();
  }
  ar.resize(n + 1);
  hr.resize(n + 1);
  size.resize(n + 1);
  g.resize(n + 1);
  b.resize(n + 1);
  ans = true;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int t;
  cin >> t;
  while (t--) {
    cin >> n >> m;
    init();
    for (long long int i = 1; i <= n; ++i) {
      cin >> ar[i];
    }
    for (long long int i = 1; i <= n; ++i) {
      cin >> hr[i];
    }
    for (long long int i = 0; i < n - 1; ++i) {
      long long int a, b;
      cin >> a >> b;
      adj[a].push_back(b);
      adj[b].push_back(a);
    }
    dfs(1, 1);
    if (ans) {
      cout << "YES";
    } else {
      cout << "NO";
    }
    cout << "\n";
  }
  return (0);
}
