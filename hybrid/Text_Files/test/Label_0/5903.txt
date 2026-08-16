#include <bits/stdc++.h>
using namespace std;
int n, m;
const int N = 100 * 1000 + 20;
map<pair<int, int>, int> e;
vector<int> gr[N];
int mark[N], par[N];
vector<pair<int, pair<int, int> > > ans;
void getInput() {
  cin >> n >> m;
  if (m % 2 == 1) {
    cout << "No solution";
    exit(0);
  }
  for (int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;
    x--, y--;
    gr[x].push_back(y), gr[y].push_back(x);
  }
  return;
}
void dfs(int v, int par) {
  mark[v] = 1;
  for (auto u : gr[v]) {
    if (!mark[u]) {
      dfs(u, v);
    }
  }
  vector<int> rtr;
  for (auto u : gr[v]) {
    if (!e[{u, v}] and u != par) {
      rtr.push_back(u);
      e[{u, v}] = e[{v, u}] = 1;
    }
  }
  if (rtr.size() % 2 == 1) {
    rtr.push_back(par);
    e[{par, v}] = e[{v, par}] = 1;
  }
  for (int i = 0; i < rtr.size(); i += 2) {
    ans.push_back({rtr[i], {v, rtr[i + 1]}});
  }
  return;
}
int main() {
  getInput();
  dfs(0, 0);
  for (int i = 0; i < ans.size(); i++) {
    cout << ans[i].first + 1 << " " << ans[i].second.first + 1 << " "
         << ans[i].second.second + 1 << endl;
  }
  return 0;
}
