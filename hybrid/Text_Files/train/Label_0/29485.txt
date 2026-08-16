#include <bits/stdc++.h>
using namespace std;
const int MAXN = 401, MODM = 1e9 + 7;
vector<int> g[MAXN];
int main() {
  int n, m;
  cin >> n >> m;
  bool fl = 0;
  set<pair<int, int>> qq;
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    if ((a == 1 && b == n) || (a == n && b == 1)) fl = 1;
    a--;
    b--;
    if (a > b) swap(a, b);
    qq.insert({a, b});
  }
  if (fl) {
    for (int i = 0; i < n; i++)
      for (int j = i + 1; j < n; j++)
        if (i != j) {
          if (!qq.count({i, j})) {
            g[i].push_back(j);
            g[j].push_back(i);
          }
        }
  } else {
    for (auto i : qq) {
      g[i.first].push_back(i.second);
      g[i.second].push_back(i.first);
    }
  }
  int s = 0, to = n - 1;
  queue<int> q;
  q.push(s);
  vector<bool> used(n);
  vector<int> d(n), p(n);
  used[s] = true;
  p[s] = -1;
  while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (size_t i = 0; i < g[v].size(); ++i) {
      int to = g[v][i];
      if (!used[to]) {
        used[to] = true;
        q.push(to);
        d[to] = d[v] + 1;
        p[to] = v;
      }
    }
  }
  if (!used[n - 1])
    cout << -1;
  else
    cout << d[n - 1];
  return 0;
}
