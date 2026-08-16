#include <bits/stdc++.h>
using namespace std;
struct Edge {
  int from, to, index;
  long long cap, flow;
  Edge(int from, int to, long long cap, long long flow, int index)
      : from(from), to(to), index(index), cap(cap), flow(flow) {}
};
struct Dinic {
  int N;
  vector<vector<Edge>> G;
  vector<Edge *> dad;
  vector<int> Q;
  Dinic(int N) : N(N), G(N), dad(N), Q(N) {}
  void AddEdge(int from, int to, long long cap) {
    G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
    if (from == to) G[from].back().index++;
    G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
  }
  long long BlockingFlow(int s, int t) {
    fill(dad.begin(), dad.end(), nullptr);
    dad[s] = &G[0][0] - 1;
    int head = 0, tail = 0;
    Q[tail++] = s;
    while (head < tail) {
      int x = Q[head++];
      for (int i = 0; i < G[x].size(); i++) {
        Edge &e = G[x][i];
        if (!dad[e.to] && e.cap - e.flow > 0) {
          dad[e.to] = &G[x][i];
          Q[tail++] = e.to;
        }
      }
    }
    if (!dad[t]) return 0;
    long long totflow = 0;
    for (int i = 0; i < G[t].size(); i++) {
      Edge *start = &G[G[t][i].to][G[t][i].index];
      long long amt = 1e18;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
        if (!e) {
          amt = 0;
          break;
        }
        amt = min(amt, e->cap - e->flow);
      }
      if (amt == 0) continue;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
        e->flow += amt;
        G[e->to][e->index].flow -= amt;
      }
      totflow += amt;
    }
    return totflow;
  }
  long long GetMaxFlow(int s, int t) {
    long long totflow = 0;
    while (long long flow = BlockingFlow(s, t)) totflow += flow;
    return totflow;
  }
};
int n, m, k, s, b;
int d[100][100];
int sa[100000];
long long sp[100000], sbest[100000];
vector<int> rs[100];
map<int, long long> gold[100];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j) d[i][j] = -1;
  for (int i = 0; i < n; ++i) d[i][i] = 0;
  for (int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    if (d[u][v] == -1) d[u][v] = d[v][u] = 1;
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j)
      for (int k = 0; k < n; ++k) {
        if (d[j][i] == -1 || d[i][k] == -1) continue;
        d[j][k] = min(d[j][k] == -1 ? (int)1e9 : d[j][k], d[j][i] + d[i][k]);
      }
  }
  cin >> s >> b >> k;
  for (int i = 0; i < s; ++i) {
    int sx, sf;
    cin >> sx >> sa[i] >> sf >> sp[i];
    sx--;
    sbest[i] = -1e18;
    for (int j = 0; j < n; ++j) {
      if (d[sx][j] != -1 && sf >= d[sx][j]) rs[j].push_back(i);
    }
  }
  for (int i = 0; i < b; ++i) {
    int bx, bd, bg;
    cin >> bx >> bd >> bg;
    bx--;
    gold[bx][bd] = max(gold[bx][bd], (long long)bg);
  }
  for (int i = 0; i < n; ++i) {
    vector<pair<int, long long>> v;
    for (auto it : gold[i])
      v.push_back({it.first, max(v.empty() ? 0 : v.back().second, it.second)});
    sort(rs[i].begin(), rs[i].end(),
         [](int a, int b) { return sa[a] < sa[b]; });
    int j = 0;
    for (int k = 0; k < v.size(); ++k) {
      while (j < rs[i].size() && sa[rs[i][j]] < v[k].first) j++;
      while (j < rs[i].size() &&
             (k == v.size() - 1 || sa[rs[i][j]] < v[k + 1].first)) {
        sbest[rs[i][j]] = max(sbest[rs[i][j]], v[k].second - sp[rs[i][j]]);
        j++;
      }
    }
  }
  long long res = 0;
  for (int i = 0; i < s; ++i)
    if (sbest[i] >= 0) res += sbest[i];
  Dinic dinic(s + 2);
  for (int i = 0; i < s; ++i) {
    if (sbest[i] >= 0)
      dinic.AddEdge(0, i + 2, sbest[i]);
    else
      dinic.AddEdge(i + 2, 1, -sbest[i]);
  }
  for (int i = 0; i < k; ++i) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    dinic.AddEdge(u + 2, v + 2, 1e18);
  }
  res -= dinic.GetMaxFlow(0, 1);
  cout << res << "\n";
}
