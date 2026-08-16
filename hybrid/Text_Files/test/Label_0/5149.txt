#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
struct Res {
  int u, v;
  long long w;
  void read() { scanf("%d %d %lld", &u, &v, &w); }
  bool operator<(const Res &t) const { return w < t.w; }
} edge[N];
struct Node {
  int u;
  long long w;
  bool operator<(const Node &t) const { return w > t.w; }
};
int n, m, k, vis[N], fa[N], pre[N];
long long dis[N];
vector<pair<int, int> > G[N];
int find(int rt) { return rt == fa[rt] ? rt : fa[rt] = find(fa[rt]); }
int main() {
  scanf("%d %d", &n, &m);
  for (int i = 1; i <= m; i++) {
    edge[i].read();
    G[edge[i].u].push_back({edge[i].v, edge[i].w});
    G[edge[i].v].push_back({edge[i].u, edge[i].w});
  }
  scanf("%d", &k);
  priority_queue<Node> q;
  memset(dis, 0x3f, sizeof dis);
  for (int i = 1, x; i <= k; i++) {
    scanf("%d", &x);
    q.push({x, 0});
    pre[x] = x;
    dis[x] = 0;
  }
  while (q.size()) {
    auto u = q.top().u;
    q.pop();
    if (vis[u]) {
      continue;
    }
    vis[u] = 1;
    for (auto &to : G[u]) {
      if (dis[to.first] > dis[u] + to.second) {
        dis[to.first] = dis[u] + to.second;
        pre[to.first] = pre[u];
        q.push({to.first, dis[to.first]});
      }
    }
  }
  long long ans = dis[1];
  for (int i = 1; i <= m; i++) {
    edge[i].w += dis[edge[i].u] + dis[edge[i].v];
    edge[i].u = pre[edge[i].u], edge[i].v = pre[edge[i].v];
  }
  sort(edge + 1, edge + 1 + m);
  for (int i = 1; i <= n; i++) {
    fa[i] = i;
  }
  for (int i = 1, cur = 1; i <= m && cur < n; i++) {
    int u = find(edge[i].u), v = find(edge[i].v);
    if (u ^ v) {
      cur++;
      fa[u] = v;
      ans += edge[i].w;
    }
  }
  printf("%lld\n", ans);
  return 0;
}
