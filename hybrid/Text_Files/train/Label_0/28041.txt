#include <bits/stdc++.h>
using namespace std;
mt19937 rnd;
struct Edge {
  int u, v, t;
};
const int N = 1e5 + 10;
const int inf = 1e9 + 10;
vector<pair<int, int> > g[N];
Edge edges[N];
int dist[N];
pair<int, int> par[N];
priority_queue<pair<int, int> > pq;
bool onpath[N];
vector<Edge> ans;
pair<int, int> Dijkstra(int n, int x, int y) {
  for (int i = 1; i <= n; i++) {
    dist[i] = inf;
  }
  dist[1] = 0;
  pq.push({0, 1});
  while (!pq.empty()) {
    int v = pq.top().second;
    pq.pop();
    for (pair<int, int> e : g[v]) {
      int to = e.first, id = e.second;
      int type = edges[id].t;
      if (dist[to] > dist[v] + x * (type == 1) + y * (type == 0)) {
        dist[to] = dist[v] + x * (type == 1) + y * (type == 0);
        par[to] = {v, id};
        pq.push({-dist[to], to});
      }
    }
  }
  int g = 0, b = 0;
  int v = n;
  while (v != 1) {
    if (edges[par[v].second].t)
      g++;
    else
      b++;
    v = par[v].first;
  }
  return {g, b};
}
int get_dist(int n) {
  pair<int, int> cur = Dijkstra(n, 1, 1);
  return cur.first + cur.second;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  int G = 0, B = 0;
  for (int i = 1; i <= m; i++) {
    int u, v, t;
    cin >> u >> v >> t;
    g[u].push_back({v, i});
    g[v].push_back({u, i});
    edges[i] = {u, v, t};
    if (t)
      G++;
    else
      B++;
  }
  int length = get_dist(n);
  int best = m + 10;
  pair<int, int> rem;
  for (int kk = 1; kk <= 50; kk++) {
    int x = rnd() % 1000 + 1;
    int y = rnd() % 1000 + 1;
    pair<int, int> cur = Dijkstra(n, x, y);
    if (cur.first + cur.second > length) {
      continue;
    }
    if (best > G + cur.second - cur.first) {
      best = G + cur.second - cur.first;
      rem = {x, y};
    }
  }
  Dijkstra(n, rem.first, rem.second);
  int v = n;
  while (v != 1) {
    onpath[par[v].second] = 1;
    v = par[v].first;
  }
  for (int i = 1; i <= m; i++) {
    if (onpath[i] && edges[i].t == 0) {
      ans.push_back({edges[i].u, edges[i].v, 1});
    } else if (!onpath[i] && edges[i].t == 1) {
      ans.push_back({edges[i].u, edges[i].v, 0});
    }
  }
  cout << ans.size() << "\n";
  for (Edge cur : ans) {
    cout << cur.u << " " << cur.v << " " << cur.t << "\n";
  }
  return 0;
}
