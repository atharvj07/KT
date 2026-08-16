#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;
void set_io(string s) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  freopen((s + ".in").c_str(), "r", stdin);
  freopen((s + ".out").c_str(), "w", stdout);
}
vector<int> d(200001);
map<int, vector<int> > cc;
int cc_count(0), n, m;
vector<bool> vis(200001, false);
vector<vector<int> > adj_list(200001);
int ans(0);
void dfs(int i) {
  vis[i] = true;
  cc[cc_count].push_back(i);
  for (auto v : adj_list[i]) {
    if (!vis[v]) dfs(v);
  }
}
bool check(int k) {
  for (auto i : cc[k]) {
    if (d[i] != 2) return false;
  }
  return true;
}
int main() {
  ios_base::sync_with_stdio;
  cin.tie(NULL);
  cin >> n >> m;
  for (int i = 1; i <= m; i++) {
    int x, y;
    cin >> x >> y;
    adj_list[x].push_back(y);
    adj_list[y].push_back(x);
    d[x]++;
    d[y]++;
  }
  for (int i = 1; i <= n; i++) {
    if (!vis[i]) {
      cc_count++;
      dfs(i);
    }
  }
  for (int i = 1; i <= cc_count; i++) {
    ans += check(i);
  }
  cout << ans;
}
