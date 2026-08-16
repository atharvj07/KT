#include <bits/stdc++.h>
using namespace std;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const long long INF = 1e18;
const double PI = acos(-1);
const long long tam = 1000100;
const long long MOD = 1e9 + 7;
const long long cmplog = 29;
int hijos[tam];
vector<int> g[tam];
pair<long long, long long> pcen;
int n;
void dfs(int u, int pa) {
  hijos[u] = 1;
  int maxx = 0;
  for (int w : g[u]) {
    if (w == pa) continue;
    dfs(w, u);
    hijos[u] += hijos[w];
    maxx = max(maxx, hijos[w]);
  }
  maxx = max(maxx, n - hijos[u]);
  pcen = min(pcen, pair<long long, long long>(maxx, u));
}
vector<pair<long long, long long> > queries[tam];
set<int> sdown[tam];
void dfs2(int u, int pa, int idx) {
  hijos[u] = 1;
  for (int w : g[u]) {
    if (w == pa) continue;
    dfs2(w, u, idx);
    hijos[u] += hijos[w];
  }
  int pup = n - hijos[u];
  queries[idx].push_back({pup, u});
  sdown[idx].insert(hijos[u]);
}
int mejor(multiset<int> &s, int precio) {
  auto it = s.upper_bound(precio / 2);
  int ans = precio;
  if (it != s.end()) {
    ans = min(ans, max(precio - *it, *it));
  }
  if (it != s.begin()) {
    it--;
    ans = min(ans, max(precio - *it, *it));
  }
  return ans;
}
bool fans[tam];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n;
  int iz, der;
  for (long long i = 0; i < n - 1; i++) {
    cin >> iz >> der;
    g[iz].push_back(der);
    g[der].push_back(iz);
  }
  pcen = pair<long long, long long>(n, n);
  dfs(1, 1);
  int ucen = pcen.second;
  multiset<int> siz, sder;
  for (long long i = 0; i < g[ucen].size(); i++) {
    int w = g[ucen][i];
    dfs2(w, ucen, i);
  }
  for (long long idx = 0; idx < g[ucen].size(); idx++) {
    for (int xx : sdown[idx]) sder.insert(xx);
  }
  fans[ucen] = 1;
  for (long long idx = 0; idx < g[ucen].size(); idx++) {
    for (int xx : sdown[idx]) {
      sder.erase(sder.find(xx));
    }
    for (auto par : queries[idx]) {
      int u = par.second;
      int pup = par.first;
      int bst = min(mejor(siz, pup), mejor(sder, pup));
      int otro = n - hijos[g[ucen][idx]];
      bst = min(bst, max(pup - otro, otro));
      if (bst <= n / 2)
        fans[u] = 1;
      else
        fans[u] = 0;
    }
    for (int xx : sdown[idx]) {
      siz.insert(xx);
    }
  }
  for (long long i = 1; i < n + 1; i++) cout << fans[i] << ' ';
}
