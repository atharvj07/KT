#include <bits/stdc++.h>
using namespace std;
const int maxn = 1000 + 10;
struct Edge {
  int from, to, cap, flow, cost;
  Edge() {}
  Edge(int f, int t, int c, int fl, int co)
      : from(f), to(t), cap(c), flow(fl), cost(co) {}
};
struct MCMF {
  int n, m, s, t;
  vector<Edge> edges;
  vector<int> G[maxn];
  bool inq[maxn];
  int d[maxn];
  int p[maxn];
  int a[maxn];
  void init(int n, int s, int t) {
    this->n = n, this->s = s, this->t = t;
    edges.clear();
    for (int i = 0; i < n; ++i) G[i].clear();
  }
  void AddEdge(int from, int to, int cap, int cost) {
    edges.push_back(Edge(from, to, cap, 0, cost));
    edges.push_back(Edge(to, from, 0, 0, -cost));
    m = edges.size();
    G[from].push_back(m - 2);
    G[to].push_back(m - 1);
  }
  bool BellmanFord(int &flow, int &cost) {
    for (int i = 0; i < n; ++i) d[i] = 1e9;
    memset(inq, 0, sizeof(inq));
    d[s] = 0, a[s] = 1e9, inq[s] = true, p[s] = 0;
    queue<int> Q;
    Q.push(s);
    while (!Q.empty()) {
      int u = Q.front();
      Q.pop();
      inq[u] = false;
      for (int i = 0; i < G[u].size(); ++i) {
        Edge &e = edges[G[u][i]];
        if (e.cap > e.flow && d[e.to] > d[u] + e.cost) {
          d[e.to] = d[u] + e.cost;
          p[e.to] = G[u][i];
          a[e.to] = min(a[u], e.cap - e.flow);
          if (!inq[e.to]) {
            Q.push(e.to);
            inq[e.to] = true;
          }
        }
      }
    }
    if (d[t] == 1e9) return false;
    flow += a[t];
    cost += a[t] * d[t];
    int u = t;
    while (u != s) {
      edges[p[u]].flow += a[t];
      edges[p[u] ^ 1].flow -= a[t];
      u = edges[p[u]].from;
    }
    return true;
  }
  int Min_cost() {
    int flow = 0, cost = 0;
    while (BellmanFord(flow, cost))
      ;
    return cost;
  }
  int solve(int k) {
    int flow = 0, cost = 0;
    while (BellmanFord(flow, cost))
      ;
    return flow == k ? cost : -1;
  }
} mcmf;
int mp['z' + 10], temp['z' + 10];
int a[maxn];
int main() {
  string s;
  int n;
  cin >> s >> n;
  for (int i = 0; i < s.length(); i++) mp[s[i]]++;
  int S = 0, T = 200;
  mcmf.init(n + 501, S, T);
  string t;
  for (int i = 1; i <= n; i++) {
    memset(temp, 0, sizeof(temp));
    cin >> t >> a[i];
    mcmf.AddEdge(S, i, a[i], 0);
    for (int j = 0; j < t.length(); j++) {
      temp[t[j]]++;
    }
    for (int j = 'a'; j <= 'z'; j++) {
      mcmf.AddEdge(i, j + 4, temp[j], i);
    }
  }
  for (int i = 'a'; i <= 'z'; i++) {
    mcmf.AddEdge(i + 4, T, mp[i], 0);
  }
  int ans = mcmf.solve(s.length());
  printf("%d\n", ans);
}
