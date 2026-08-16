#include <bits/stdc++.h>
using namespace std;
long long int INF = 1e18;
const int N = 3e+5 + 5;
long long int cnt[2][N], vis[2][N], visup[2][N];
long long int n, m, k, x, u, v, ans, ct;
vector<pair<long long int, long long int>> adj[N];
string s;
queue<pair<long long int, long long int>> q;
void dfs(long long int i, int key) {
  if (!vis[key][i]) {
    vis[key][i] = 1;
    ct += 1;
    for (auto it : adj[i]) {
      if (it.second == key) dfs(it.first, key);
    }
  }
}
void dfsup(long long int i, int key) {
  if (!visup[key][i]) {
    visup[key][i] = 1;
    cnt[key][i] = ct;
    for (auto it : adj[i]) {
      if (it.second == key) dfsup(it.first, key);
    }
  }
}
int main() {
  cin >> n;
  for (int i = 1; i <= n - 1; i++) {
    cin >> u >> v >> x;
    adj[u].push_back({v, x});
    adj[v].push_back({u, x});
  }
  for (int i = 1; i <= n; i++) {
    ct = 0;
    if (!vis[0][i]) {
      dfs(i, 0);
      dfsup(i, 0);
    }
    ans += ct * (ct - 1);
    ct = 0;
    if (!vis[1][i]) {
      dfs(i, 1);
      dfsup(i, 1);
    }
    ans += ct * (ct - 1);
  }
  for (int i = 1; i <= n; i++) {
    ans += (cnt[0][i] - 1) * (cnt[1][i] - 1);
  }
  cout << ans << endl;
}
