#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dbl = long double;
const int MAXN = 1000;
const ll INF = 1e18;
int n, m, k;
ll a[MAXN][MAXN];
vector<pair<int, pii> > edges;
vector<ll> order;
int renum[200100];
int d[200100];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n >> m >> k;
  for (int i = 0; i < m; i++) {
    int x, y, w;
    cin >> x >> y >> w;
    edges.push_back({w, {x, y}});
  }
  sort(edges.begin(), edges.end());
  if (m > 400) {
    edges.erase(edges.begin() + 400, edges.end());
    for (auto it : edges) {
      int x = it.second.first;
      int y = it.second.second;
      d[x]++;
      d[y]++;
    }
    int k = 0;
    for (int i = 1; i <= n; i++) {
      if (d[i]) {
        renum[i] = ++k;
      }
    }
    for (int i = 0; i < (int)edges.size(); i++) {
      int &x = edges[i].second.first;
      int &y = edges[i].second.second;
      x = renum[x];
      y = renum[y];
    }
    n = k;
    m = 400;
  }
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      a[i][j] = INF;
    }
    a[i][i] = 0;
  }
  for (int i = 0; i < m; i++) {
    int x = edges[i].second.first;
    int y = edges[i].second.second;
    int w = edges[i].first;
    a[x][y] = a[y][x] = w;
  }
  for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
      }
    }
  }
  for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {
      order.push_back(a[i][j]);
    }
  }
  sort(order.begin(), order.end());
  cout << order[k - 1];
  return 0;
}
