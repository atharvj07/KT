#include <bits/stdc++.h>
using namespace std;
const long long mod = 1000000007;
const long long OO = (long long)1e18;
const int dx[] = {0, 1, 0, -1, 1, -1, 1, -1};
const int dy[] = {1, 0, -1, 0, 1, -1, -1, 1};
long long gcd(long long a, long long b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
}
long long fast_power(long long base, long long power) {
  if (power == 1) return base;
  if (power % 2 == 0)
    return fast_power((base * base), power / 2);
  else
    return (base * fast_power((base * base), power / 2));
}
void Qalbaz() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cout << fixed << setprecision(1);
}
vector<vector<int> > adj;
int cnt;
vector<int> vis, vvv, vv, vec;
void dfs(int u) {
  vis[u] = 1;
  vvv.push_back(u);
  vv.push_back(vec[u]);
  int v;
  for (int i = 0; i < adj[u].size(); i++) {
    v = adj[u][i];
    if (vis[v] == 0) {
      dfs(v);
    }
  }
}
int main() {
  Qalbaz();
  int n, m, u, v;
  cin >> n >> m;
  adj.resize(n + 1);
  vec.resize(n + 1);
  for (int i = 1; i <= n; i++) cin >> vec[i];
  for (int i = 0; i < m; i++) {
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  vis.resize(n + 1);
  for (int i = 1; i <= n; i++) {
    if (vis[i] == 0) {
      vv.clear();
      vvv.clear();
      dfs(i);
      sort(vv.begin(), vv.end());
      sort(vvv.begin(), vvv.end());
      for (int j = 0, k = vv.size() - 1; k >= 0 && j < vv.size(); j++, k--)
        vec[vvv[j]] = vv[k], cnt++;
    }
  }
  for (int i = 0; i < n; i++) cout << vec[i + 1] << " ";
  return 0;
}
