#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
void read(int &val) {
  int x = 0;
  int bz = 1;
  char c;
  for (c = getchar(); (c < '0' || c > '9') && c != '-'; c = getchar())
    ;
  if (c == '-') {
    bz = -1;
    c = getchar();
  }
  for (; c >= '0' && c <= '9'; c = getchar()) x = x * 10 + c - 48;
  val = x * bz;
}
const int maxn = 1e5 + 101;
const int mod = 1e9 + 7;
struct Edge {
  int from, to, cap, flow;
  long long cost;
};
int a[maxn], b[maxn];
bool cmp(int x, int y) { return b[x] < b[y]; }
int n, k;
int N;
struct MCMF {
  int n, m;
  vector<Edge> edge;
  vector<int> G[maxn];
  int inq[maxn], p[maxn], a[maxn], To[maxn];
  long long d[maxn];
  int tag[maxn];
  void init(int _n) {
    n = _n;
    for (int i = 0; i <= n; i++) G[i].clear();
    edge.clear();
  }
  void add(int from, int to, int cap, long long cost, int flag) {
    edge.push_back(Edge{from, to, cap, 0, cost});
    edge.push_back(Edge{to, from, 0, 0, -cost});
    m = edge.size();
    G[from].push_back(m - 2);
    G[to].push_back(m - 1);
    tag[m - 2] = tag[m - 1] = flag;
    To[m - 1] = To[m - 2] = to - N;
  }
  bool BellFord(int s, int t, int &flow, long long &cost) {
    for (int i = 0; i <= n; i++) d[i] = INF, inq[i] = 0;
    d[s] = 0;
    inq[s] = 1;
    p[s] = 0;
    a[s] = INF;
    queue<int> q;
    q.push(s);
    while (!q.empty()) {
      int u = q.front();
      q.pop();
      inq[u] = 0;
      for (auto to : G[u]) {
        Edge &e = edge[to];
        if (e.cap > e.flow && d[e.to] > d[u] + e.cost) {
          d[e.to] = d[u] + e.cost;
          p[e.to] = to;
          a[e.to] = min(a[u], e.cap - e.flow);
          if (!inq[e.to]) {
            q.push(e.to);
            inq[e.to] = 1;
          }
        }
      }
    }
    if (d[t] == INF) return false;
    flow += a[t];
    cost += 1LL * d[t] * a[t];
    for (int u = t; u != s; u = edge[p[u]].from) {
      edge[p[u]].flow += a[t];
      edge[p[u] ^ 1].flow -= a[t];
    }
    return true;
  }
  void MincostMaxflow(int s, int t, long long &cost) {
    int flow = 0;
    cost = 0;
    while (BellFord(s, t, flow, cost))
      ;
    vector<int> ans1, ans2;
    n = (n - 4) / 3;
    for (int i = 1; i <= n; i++) {
      for (auto to : G[i]) {
        if (edge[to].flow == false) continue;
        if (tag[to] == 1) {
          ans1.push_back(To[to]);
        } else if (tag[to] == 2) {
          ans2.push_back(To[to]);
        }
      }
    }
    sort(ans1.begin(), ans1.end(), cmp);
    int sz = ans1.size();
    for (int i = 0; i <= sz - 2; i++) {
      printf("%d ", ans1[i]);
    }
    for (auto to : ans2) {
      printf("%d %d ", to, -to);
    }
    printf("%d\n", ans1[sz - 1]);
  }
} M;
int main() {
  int t;
  read(t);
  while (t--) {
    read(n);
    read(k);
    N = n;
    M.init(3 * n + 4);
    int mx = 0, j = 0;
    for (int i = 1; i <= n; i++) {
      read(a[i]);
      read(b[i]);
      if (mx < a[i]) j = i;
      mx = max(mx, a[i]);
    }
    if (k == 1) {
      printf("%d\n%d\n", 1, j);
      continue;
    }
    printf("%d\n", k + 2 * (n - k));
    int s = 0, t = 3 * n + 3;
    for (int i = 1; i <= n; i++) {
      M.add(s, i, 1, 0, -1);
    }
    for (int i = 1; i <= k - 1; i++) {
      for (int j = 1; j <= n; j++) {
        M.add(i, j + n, 1, -(1LL * (i - 1) * b[j] + a[j]), 1);
      }
    }
    for (int i = k; i <= n - 1; i++) {
      for (int j = 1; j <= n; j++) {
        M.add(i, j + n, 1, -(1LL * (k - 1) * b[j]), 2);
      }
    }
    for (int j = 1; j <= n; j++) {
      M.add(n, j + n, 1, -(1LL * (k - 1) * b[j] + a[j]), 1);
    }
    for (int i = n + 1; i <= n + n; i++) {
      M.add(i, t, 1, 0, -1);
    }
    long long cost = 0;
    M.MincostMaxflow(s, t, cost);
  }
  return 0;
}
