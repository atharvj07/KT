#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100006;
const int MOD = 1000000007;
int n, m;
vector<int> adj[MAXN];
bool co[MAXN];
int dp[MAXN];
vector<int> ts;
bool vis[MAXN];
void topdfs(int x) {
  vis[x] = true;
  for (int v : adj[x]) {
    if (!vis[v]) topdfs(v);
  }
  ts.push_back(x);
}
void topSort() {
  for (int i = 0; i < n; i++) {
    if (!vis[i]) topdfs(i);
  }
  reverse(ts.begin(), ts.end());
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++) cin >> co[i], dp[i] = co[i];
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    adj[b].push_back(a);
  }
  topSort();
  for (int i = 0; i < n; i++) {
    int x = ts[i];
    for (int v : adj[x]) {
      if (!co[x] && co[v]) {
        dp[v] = max(dp[v], dp[x] + 1);
      } else
        dp[v] = max(dp[v], dp[x]);
    }
  }
  int mx = 0;
  for (int i = 0; i < n; i++) {
    mx = max(mx, dp[i]);
  }
  cout << mx << endl;
}
