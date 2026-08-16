#include <bits/stdc++.h>
using namespace std;
const int N = 1e2 + 10;
const int maxs = 1e5 + 10;
const int maxn = 2e3 + 10;
const int maxm = 6e3 + 10;
const long long INF = 1e14 + 10;
const long long INF_CAP = INF;
struct spaceship {
  int x, a, f, p;
} sp[maxs];
struct base {
  int d, g;
  bool operator<(const base& b) const { return d < b.d; }
};
long long best_goal[maxs];
vector<base> ba[N];
vector<int> pre[N];
vector<int> g[maxs];
bool used[maxs];
int w[N][N], id[maxs];
struct Dinic {
  int n, m, s, t, pos;
  int d[maxn], head[maxn], que[maxn], ptr[maxn];
  int to[maxm], nxt[maxm];
  long long cap[maxm];
  void init() { memset(head, -1, sizeof head); }
  void addedge(int a, int b, long long c) {
    cap[m] = c;
    to[m] = b;
    nxt[m] = head[a];
    head[a] = m++;
    cap[m] = 0;
    to[m] = a;
    nxt[m] = head[b];
    head[b] = m++;
  }
  bool bfs() {
    pos = 0;
    memset(d, -1, sizeof d);
    que[pos++] = s;
    d[s] = 0;
    for (int i = 0; i < pos; i++) {
      int x = que[i];
      for (int u = head[x]; ~u; u = nxt[u]) {
        if (d[to[u]] == -1 && cap[u]) {
          d[to[u]] = d[x] + 1;
          que[pos++] = to[u];
          if (d[t] != -1) return true;
        }
      }
    }
    return d[t] != -1;
  }
  long long dfs(int o, long long mi) {
    if (o == t || mi == 0) return mi;
    long long res = 0;
    for (int& x = ptr[o]; ~x; x = nxt[x])
      if (d[to[x]] == d[o] + 1 && cap[x]) {
        long long tmp = dfs(to[x], min(mi, cap[x]));
        cap[x] -= tmp;
        cap[x ^ 1] += tmp;
        if (tmp > 0) return tmp;
      }
    return res;
  }
  long long maxflow(int s, int t) {
    this->s = s;
    this->t = t;
    long long res = 0;
    while (bfs()) {
      memcpy(ptr, head, sizeof head);
      res += dfs(s, INF_CAP);
    }
    return res;
  }
} D;
int main() {
  D.init();
  int n, m, s, b, k;
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) fill(w[i] + 1, w[i] + 1 + n, n), w[i][i] = 0;
  for (int i = 0; i < m; i++) {
    int a, b;
    scanf("%d%d", &a, &b);
    w[b][a] = w[a][b] = min(w[a][b], 1);
  }
  for (int d = 1; d <= n; d++) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        w[i][j] = min(w[i][j], w[i][d] + w[d][j]);
      }
    }
  }
  scanf("%d%d%d", &s, &b, &k);
  for (int i = 1; i <= s; i++) {
    scanf("%d%d%d%d", &sp[i].x, &sp[i].a, &sp[i].f, &sp[i].p);
  }
  for (int i = 0; i < b; i++) {
    int x, d, g;
    scanf("%d%d%d", &x, &d, &g);
    ba[x].push_back(base{d, g});
  }
  for (int i = 1; i <= n; i++)
    if (ba[i].size()) {
      int sz = (int)ba[i].size();
      sort(ba[i].begin(), ba[i].end());
      pre[i].resize(sz);
      pre[i][0] = ba[i][0].g;
      for (int j = 1; j < sz; j++) pre[i][j] = max(pre[i][j - 1], ba[i][j].g);
    }
  for (int i = 1; i <= s; i++) {
    best_goal[i] = -INF_CAP;
    int x = sp[i].x;
    for (int j = 1; j <= n; j++) {
      if (w[x][j] <= sp[i].f) {
        int pos = upper_bound(ba[j].begin(), ba[j].end(), base{sp[i].a, 0}) -
                  ba[j].begin();
        --pos;
        if (pos >= 0) {
          best_goal[i] = max(best_goal[i], (long long)pre[j][pos] - sp[i].p);
        }
      }
    }
  }
  for (int i = 0; i < k; i++) {
    int a, b;
    scanf("%d%d", &a, &b);
    g[a].push_back(b);
    used[a] = used[b] = 1;
  }
  long long ans = 0;
  int cnt = 0;
  for (int i = 1; i <= s; i++) {
    if (!used[i]) {
      if (best_goal[i] > 0) ans += best_goal[i];
    } else {
      id[i] = ++cnt;
    }
  }
  int st = 0, ed = cnt + 1;
  cnt = 0;
  for (int i = 1; i <= s; i++) {
    if (used[i]) {
      if (best_goal[i] >= 0)
        ans += best_goal[i], D.addedge(st, id[i], best_goal[i]);
      else
        D.addedge(id[i], ed, -best_goal[i]);
      for (auto& u : g[i]) D.addedge(id[i], id[u], INF_CAP);
    }
  }
  ans -= D.maxflow(st, ed);
  printf("%lld\n", ans);
  return 0;
}
