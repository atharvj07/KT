#include <bits/stdc++.h>
using namespace std;
bool debug;
const int inf = 1e9 + 5;
const int nax = 6405;
namespace MinCost {
struct Edge {
  int w, c, v, rev;
  Edge(int _w, int _c, int _v, int _rev) : w(_w), c(_c), v(_v), rev(_rev) {}
};
int odl[nax], pot[nax], pop[nax], pop_kraw[nax];
int q[nax * 100], qbeg, qend;
vector<Edge> v[nax];
bool bylo[nax];
queue<int> kolej;
void init(int n) {
  for (int i = 0; i <= n; ++i) v[i].clear();
}
void AddEdge(int a, int b, int cap, int cost) {
  v[a].push_back(Edge(b, cap, cost, int(v[b].size()) + (a == b)));
  v[b].push_back(Edge(a, 0, -cost, int(v[a].size() - 1)));
}
pair<int, int> MinCostMaxFlow(int s, int t, int n) {
  int flow = 0, cost = 0;
  while (true) {
    for (int i = 0; i <= n; ++i) {
      odl[i] = inf;
      bylo[i] = false;
    }
    bylo[s] = true;
    odl[s] = 0;
    qbeg = qend = 0;
    q[qend++] = s;
    while (qbeg < qend) {
      int x = q[qbeg++];
      bylo[x] = false;
      int dl = v[x].size();
      for (int i = 0; i <= (dl)-1; ++i)
        if (v[x][i].c > 0 &&
            odl[v[x][i].w] > odl[x] + pot[x] - pot[v[x][i].w] + v[x][i].v) {
          odl[v[x][i].w] = odl[x] + pot[x] - pot[v[x][i].w] + v[x][i].v;
          if (!bylo[v[x][i].w]) {
            q[qend++] = v[x][i].w;
            bylo[v[x][i].w] = true;
          }
          pop[v[x][i].w] = x;
          pop_kraw[v[x][i].w] = i;
        }
    }
    if (odl[t] == inf) break;
    int x = t;
    int cap = inf;
    while (x != s) {
      cap = min(cap, v[pop[x]][pop_kraw[x]].c);
      x = pop[x];
    }
    flow += cap;
    x = t;
    while (x != s) {
      cost += v[pop[x]][pop_kraw[x]].v * cap;
      v[pop[x]][pop_kraw[x]].c -= cap;
      v[x][v[pop[x]][pop_kraw[x]].rev].c += cap;
      x = pop[x];
    }
  }
  return make_pair(flow, cost);
}
};  // namespace MinCost
using namespace MinCost;
const int naxn = 87;
int n, m;
int t[naxn][naxn];
int main(int argc, char* argv[]) {
  debug = argc > 1;
  scanf("%d%d", &n, &m);
  init(n * m + 1);
  for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= m; ++j) scanf("%d", &t[i][j]);
  for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= m; ++j) {
      int val = (i - 1) * m + j;
      if ((i + j) & 1) {
        MinCost::AddEdge(0, val, 1, 0);
        if (i > 1) AddEdge(val, val - m, 1, t[i][j] != t[i - 1][j]);
        if (j > 1) AddEdge(val, val - 1, 1, t[i][j] != t[i][j - 1]);
        if (i < n) AddEdge(val, val + m, 1, t[i][j] != t[i + 1][j]);
        if (j < m) AddEdge(val, val + 1, 1, t[i][j] != t[i][j + 1]);
      } else
        MinCost::AddEdge(val, n * m + 1, 1, 0);
    }
  printf("%d\n", MinCost::MinCostMaxFlow(0, n * m + 1, n * m + 1).second);
  return 0;
}
