#include <bits/stdc++.h>
using namespace std;
const int MAXN = 500 + 17, inf = 1e9 + 17;
int n, m, dp[MAXN][MAXN];
pair<int, int> par[MAXN][MAXN];
vector<int> adj[MAXN], ans1, ans2;
void bfs() {
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++) dp[i][j] = inf;
  dp[1][n] = 0;
  queue<pair<int, int> > q;
  q.push({1, n});
  while (q.size()) {
    pair<int, int> fr = q.front();
    q.pop();
    for (auto i : adj[fr.first])
      for (auto j : adj[fr.second])
        if (i != j && dp[fr.first][fr.second] + 1 < dp[i][j]) {
          dp[i][j] = dp[fr.first][fr.second] + 1;
          par[i][j] = {fr.first, fr.second};
          q.push({i, j});
        }
  }
}
void pp(int i = n, int j = 1) {
  ans1.push_back(i);
  ans2.push_back(j);
  if (i == 1 && j == n) return;
  pp(par[i][j].first, par[i][j].second);
}
int main() {
  ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
  cin >> n >> m;
  for (int i = 1; i <= m; i++) {
    int v, u;
    cin >> v >> u;
    adj[v].push_back(u);
    adj[u].push_back(v);
  }
  bfs();
  if (dp[n][1] == inf) return cout << -1 << endl, 0;
  cout << dp[n][1] << endl;
  pp();
  reverse(ans1.begin(), ans1.end());
  reverse(ans2.begin(), ans2.end());
  for (auto i : ans1) cout << i << ' ';
  cout << endl;
  for (auto i : ans2) cout << i << ' ';
  cout << endl;
  return 0;
}
