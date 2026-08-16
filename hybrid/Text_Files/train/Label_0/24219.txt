#include <bits/stdc++.h>
using namespace std;
namespace Dinic {
const int MAXV = 30000;
const int MAXE = 500005;
const long long int oo = 1e18;
int V, E;
int last[MAXV], dist[MAXV], curr[MAXV];
int next[MAXE], adj[MAXE];
long long int cap[MAXE];
long long int iniCap[MAXE];
void init(int n) {
  V = n;
  E = 0;
  for (long long int i = 1; i <= V; ++i) last[i] = -1;
}
void edge(int x, int y, long long int c1, long long int c2) {
  adj[E] = y;
  cap[E] = iniCap[E] = c1;
  next[E] = last[x];
  last[x] = E++;
  adj[E] = x;
  cap[E] = iniCap[E] = c2;
  next[E] = last[y];
  last[y] = E++;
}
long long int push(int x, int sink, long long int flow) {
  if (x == sink) return flow;
  for (int &e = curr[x]; e != -1; e = next[e]) {
    int y = adj[e];
    if (cap[e] && dist[x] + 1 == dist[y])
      if (long long int f = push(y, sink, min(flow, cap[e])))
        return cap[e] -= f, cap[e ^ 1] += f, f;
  }
  return 0;
}
long long int run(int src, int sink) {
  long long int ret = 0;
  for (;;) {
    for (long long int i = 1; i <= V; ++i) curr[i] = last[i];
    for (long long int i = 1; i <= V; ++i) dist[i] = -1;
    queue<int> Q;
    Q.push(src), dist[src] = 0;
    while (!Q.empty()) {
      int x = Q.front();
      Q.pop();
      for (int e = last[x]; e != -1; e = next[e]) {
        int y = adj[e];
        if (cap[e] && dist[y] == -1) Q.push(y), dist[y] = dist[x] + 1;
      }
    }
    if (dist[sink] == -1) break;
    while (long long int f = push(src, sink, oo)) ret += f;
  }
  return ret;
}
int getDest(int st) {
  for (int e = last[st]; e != -1; e = next[e]) {
    if (cap[e] < iniCap[e]) {
      cap[e]++;
      if (adj[e] == V) {
        return st;
      } else {
        return getDest(adj[e]);
      }
    }
  }
  return -1;
}
vector<int> getFlows(int st) {
  vector<int> ret;
  for (int e = last[st]; e != -1; e = next[e]) {
    if (cap[e] < iniCap[e]) {
      ret.push_back(adj[e]);
    }
  }
  return ret;
}
}  // namespace Dinic
using namespace Dinic;
const int N = 5005;
const long long int inf = 1e16;
int n, m;
int loc[N], inv[4 * N], locs[4 * N], leaf[4 * N], rtNodes;
int typ[N], ans[N];
vector<int> vals[N];
void buildseg(int idx, int l, int r) {
  locs[idx] = idx + n + 1;
  rtNodes = max(rtNodes, idx);
  if (l == r) {
    leaf[idx] = 1;
    loc[l] = idx;
    inv[idx] = l;
    return;
  }
  int mid = (l + r) / 2;
  buildseg(2 * idx, l, mid);
  buildseg(2 * idx + 1, mid + 1, r);
}
void query(int idx, int l, int r, int st, int en, int i) {
  if (st > en || st > r || en < l) return;
  if (st <= l && en >= r) {
    edge(i, locs[idx], 1, 0);
    return;
  }
  int mid = (l + r) / 2;
  query(2 * idx, l, mid, st, en, i);
  query(2 * idx + 1, mid + 1, r, st, en, i);
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n >> m;
  buildseg(1, 1, m);
  int src = 1, sink = rtNodes + n + 2;
  init(sink);
  for (long long int i = 1; i <= rtNodes; ++i) {
    if (!leaf[i]) {
      edge(locs[i], locs[2 * i], inf, 0);
      edge(locs[i], locs[2 * i + 1], inf, 0);
    } else {
      edge(locs[i], sink, 1, 0);
    }
  }
  for (long long int i = 1; i <= n; ++i) {
    long long int ty;
    cin >> ty;
    typ[i] = ty;
    if (ty == 0 || ty == 1)
      edge(src, i + 1, 1, 0);
    else
      edge(src, i + 1, 2, 0);
    if (ty == 0) {
      long long int k;
      cin >> k;
      while (k--) {
        long long int v;
        cin >> v;
        edge(i + 1, locs[loc[v]], 1, 0);
      }
    } else if (ty == 1) {
      long long int l, r;
      cin >> l >> r;
      query(1, 1, m, l, r, i + 1);
    } else {
      int a, b, c;
      cin >> a >> b >> c;
      edge(i + 1, locs[loc[a]], 1, 0);
      edge(i + 1, locs[loc[b]], 1, 0);
      edge(i + 1, locs[loc[c]], 1, 0);
      vals[i].push_back(a);
      vals[i].push_back(b);
      vals[i].push_back(c);
    }
  }
  cout << run(src, sink) << '\n';
  for (long long int i = 2; i <= n + 1; ++i) {
    if (typ[i - 1] < 2) {
      int v = getDest(i);
      v -= (n + 1);
      if (v != -1) ans[inv[v]] = i - 1;
    }
  }
  for (long long int i = 2; i <= n + 1; ++i)
    if (typ[i - 1] == 2) {
      vector<int> fl = getFlows(i);
      for (int v : fl) {
        v -= (n + 1);
        v = inv[v];
        ans[v] = i - 1;
      }
      if (fl.size() == 1) {
        int v = inv[fl[0] - n - 1];
        for (long long int u : vals[i - 1])
          if (u != v) {
            ans[u] = i - 1;
            break;
          }
      }
    }
  for (long long int i = 1; i <= m; ++i)
    if (ans[i]) {
      cout << ans[i] << " " << i << '\n';
    }
}
