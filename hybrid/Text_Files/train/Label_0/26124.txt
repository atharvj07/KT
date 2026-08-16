#include <bits/stdc++.h>
using namespace std;
const int inf = 1000 * 1000 * 1000 + 7;
struct MaxFlow {
  struct edge {
    int to, rev, cap, flow;
  };
  int n;
  vector<int> dst, pos;
  vector<vector<edge>> g;
  MaxFlow(int n) : n(n), dst(n), pos(n), g(n) {}
  void add(int a, int b, int c) {
    g[a].push_back({b, (int)g[b].size(), c, 0});
    g[b].push_back({a, (int)g[a].size() - 1, 0, 0});
  }
  int dfs(int f, int s, int cost = inf) {
    if (f == s) return cost;
    if (!cost) return 0;
    for (int& i = pos[f]; i < (int)g[f].size(); ++i) {
      auto& item = g[f][i];
      if (dst[item.to] == dst[f] + 1) {
        int val = dfs(item.to, s, min(cost, item.cap - item.flow));
        if (val > 0) {
          item.flow += val;
          g[item.to][item.rev].flow -= val;
          return val;
        }
      }
    }
    return 0;
  }
  bool bfs(int f, int s) {
    fill(dst.begin(), dst.end(), inf);
    dst[f] = 0;
    queue<int> q;
    q.push(f);
    while (!q.empty()) {
      int v = q.front();
      q.pop();
      for (auto& item : g[v]) {
        if (dst[item.to] > dst[v] + 1 && item.cap > item.flow) {
          dst[item.to] = dst[v] + 1;
          q.push(item.to);
        }
      }
    }
    return dst[s] < inf;
  }
  int computeFlow(int f, int s) {
    int result = 0, val;
    while (true) {
      if (!bfs(f, s)) break;
      fill(pos.begin(), pos.end(), 0);
      while ((val = dfs(f, s)) > 0) result += val;
    }
    return result;
  }
};
struct Task {
  int n, m;
  vector<vector<pair<int, int>>> g;
  vector<pair<int, int>> c;
  vector<int> tin, tout;
  vector<vector<int>> jump, num;
  int cur, timer;
  Task(int n, int m)
      : n(n),
        m(m),
        g(n),
        c(m),
        tin(n),
        tout(n),
        jump(n, vector<int>(15)),
        num(n, vector<int>(15)) {
    for (int i = 0; i < n - 1; ++i) {
      int x, y;
      cin >> x >> y;
      --x;
      --y;
      g[x].emplace_back(y, i + m);
      g[y].emplace_back(x, i + m);
    }
    for (auto& item : c) {
      cin >> item.first >> item.second;
      --item.first;
      --item.second;
    }
  }
  void dfs(int v, MaxFlow& flow, int id, int pr) {
    tin[v] = timer++;
    jump[v][0] = pr;
    num[v][0] = id;
    for (int i = 1; i < 15; ++i) {
      jump[v][i] = jump[jump[v][i - 1]][i - 1];
      num[v][i] = cur++;
      flow.add(num[v][i], num[v][i - 1], inf);
      flow.add(num[v][i], num[jump[v][i - 1]][i - 1], inf);
    }
    for (auto& item : g[v]) {
      int to = item.first, id = item.second;
      if (to != pr) {
        dfs(to, flow, id, v);
      }
    }
    tout[v] = timer++;
  }
  bool line(int x, int y) { return tin[x] <= tin[y] && tout[x] >= tout[y]; }
  int go(int x, int y) {
    if (line(x, y)) return x;
    if (line(y, x)) return y;
    for (int i = 14; i >= 0; --i) {
      if (!line(jump[x][i], y)) {
        x = jump[x][i];
      }
    }
    return jump[x][0];
  }
  void cut(int v, vector<int>& was, MaxFlow& flow) {
    was[v] = 1;
    for (auto& item : flow.g[v]) {
      int to = item.to;
      if (item.cap > item.flow && !was[to]) {
        cut(to, was, flow);
      }
    }
  }
  void run() {
    int size = 16 * n + m + 2;
    int source = size - 1;
    int sink = size - 2;
    MaxFlow flow(size);
    cur = n + m;
    dfs(0, flow, n + m - 1, 0);
    for (int i = 0; i < n - 1; ++i) {
      flow.add(i + m, sink, 1);
    }
    for (int i = 0; i < m; ++i) {
      flow.add(source, i, 1);
      int x = c[i].first, y = c[i].second;
      int lca = go(x, y);
      for (int _ = 0; _ < (2); ++_) {
        for (int j = 14; j >= 0; --j) {
          if (!line(jump[x][j], lca)) {
            flow.add(i, num[x][j], inf);
            x = jump[x][j];
          }
        }
        flow.add(i, num[x][0], inf);
        swap(x, y);
      }
    }
    cout << flow.computeFlow(source, sink) << '\n';
    vector<int> was(size);
    cut(source, was, flow);
    vector<int> a, b;
    for (int i = 0; i < (size); ++i) {
      if (!was[i] && i < m) {
        a.push_back(i);
      }
      if (was[i] && i >= m && i < m + n - 1) {
        b.push_back(i - m);
      }
    }
    cout << (int)a.size() << ' ';
    for (auto& item : a) {
      cout << item + 1 << ' ';
    }
    cout << '\n';
    cout << (int)b.size() << ' ';
    for (auto& item : b) {
      cout << item + 1 << ' ';
    }
    cout << '\n';
  }
};
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  Task task(n, m);
  task.run();
  return 0;
}
