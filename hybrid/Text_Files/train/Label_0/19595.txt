#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 1;
const int M = 1e9 + 7;
const double eps = 1e-6;
const int inf = 1e9;
const long long INF = 1e18;
const double PI(acos(-1.0));
vector<int> g[N];
set<int> G[N];
map<vector<int>, int> mp;
int ans[N];
int n, m;
int t = 1, id[N];
int main() {
  cin >> n >> m;
  for (int i = 0; i < (m); i++) {
    int u, v;
    cin >> u >> v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  for (int i = (1); i <= (n); i++) {
    g[i].push_back(i);
    sort((g[i]).begin(), (g[i]).end());
    if (!mp[g[i]]) mp[g[i]] = mp.size();
    id[i] = mp[g[i]];
  }
  for (int i = (1); i <= (n); i++)
    for (auto j : g[i])
      if (id[i] != id[j]) G[id[i]].insert(id[j]);
  int s = 0;
  for (int i = (1); i <= (((int)mp.size())); i++) {
    if (((int)G[i].size()) > 2) {
      return cout << "NO\n", 0;
    }
    if (((int)G[i].size()) < 2) s = i;
  }
  for (int i = (1); i <= (((int)mp.size())); i++) {
    ans[s] = i;
    for (auto t : G[s])
      if (!ans[t]) s = t;
  }
  cout << "YES\n";
  for (int i = (1); i <= (n); i++) cout << ans[id[i]] << " ";
  cout << "\n";
}
