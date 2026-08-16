#include <bits/stdc++.h>
using namespace std;
const int maxm = 200000 + 5;
const int maxn = 200000 + 5;
struct Edge {
  int from, to, w, id;
};
vector<Edge> edges;
vector<int> G[maxn];
int ans[maxm];
int n, m;
int win[maxn], wall[maxn];
inline void solve() {
  memset(ans, -1, sizeof ans);
  queue<int> Q;
  Q.push(1);
  while (!Q.empty()) {
    int now = Q.front();
    Q.pop();
    vector<int> tocheck;
    for (const int& i : G[now]) {
      Edge& e = edges[i];
      if (ans[e.id] != -1) continue;
      int to;
      if (now == e.from)
        to = e.to, ans[e.id] = 0;
      else
        to = e.from, ans[e.id] = 1;
      win[to] += e.w;
      wall[to] -= e.w;
      if (to != n) tocheck.push_back(to);
    }
    for (const int& nx : tocheck)
      if (win[nx] == wall[nx]) Q.push(nx);
  }
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 0, a, b, c; i < m; i++) {
    scanf("%d%d%d", &a, &b, &c);
    edges.push_back((Edge){a, b, c, i});
    G[a].push_back((int)edges.size() - 1);
    G[b].push_back((int)edges.size() - 1);
    wall[a] += c;
    wall[b] += c;
  }
  solve();
  for (int i = 0; i < m; i++) printf("%d\n", ans[i]);
}
