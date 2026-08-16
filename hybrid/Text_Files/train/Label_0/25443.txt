#include <bits/stdc++.h>
using namespace std;
const long long mod = 1e9 + 7;
const long long N = 10012;
const long long inf = 2e9;
int n, x[N], y[N];
int ans;
int sdflksdfld[N], sdlfklsd[N];
vector<int> g[N], G[N][2];
int used[N], tmr;
map<int, vector<int>> gx, gy;
map<int, vector<pair<int, int>>> A, B;
inline bool dfs(int v) {
  if (used[v] == tmr) return false;
  used[v] = tmr;
  for (int to : g[v])
    if (sdlfklsd[to] == -1 || dfs(sdlfklsd[to])) {
      sdlfklsd[to] = v;
      sdflksdfld[v] = to;
      return true;
    }
  return false;
}
int was[N][2];
inline void go(int v, int is_l = 0) {
  if (was[v][is_l]) return;
  was[v][is_l] = 1;
  for (int to : G[v][is_l]) go(to, is_l ^ 1);
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  ans = 4 * n;
  vector<pair<int, pair<int, int>>> ver, hor;
  for (long long i = 1; i <= n; ++i) {
    cin >> x[i] >> y[i], gx[x[i]].push_back(y[i]), gy[y[i]].push_back(x[i]);
  }
  for (auto &v : gx) {
    sort(v.second.begin(), v.second.end());
    for (int i = 1; i < v.second.size(); ++i) {
      ver.push_back({v.first, {v.second[i - 1], v.second[i]}});
    }
    for (int i = 0; i < v.second.size(); ++i) {
      ver.push_back({v.first, {v.second[i], v.second[i]}});
    }
  }
  for (auto &v : gy) {
    sort(v.second.begin(), v.second.end());
    for (int i = 1; i < v.second.size(); ++i) {
      hor.push_back({v.first, {v.second[i - 1], v.second[i]}});
    }
    for (int i = 0; i < v.second.size(); ++i) {
      hor.push_back({v.first, {v.second[i], v.second[i]}});
    }
  }
  for (int i = 0; i < ver.size(); ++i)
    for (int j = 0; j < hor.size(); ++j) {
      auto &v = ver[i], h = hor[j];
      int vx = v.first, vl = v.second.first, vr = v.second.second;
      int hy = h.first, hl = h.second.first, hr = h.second.second;
      if (hl < vx && vx < hr && vl < hy && hy < vr) {
        g[i].push_back(j);
      }
    }
  for (int i = 0; i < ver.size(); ++i) sdflksdfld[i] = -1;
  for (int i = 0; i < hor.size(); ++i) sdlfklsd[i] = -1;
  for (int run = 1; run;) {
    run = 0;
    tmr++;
    for (int i = 0; i < ver.size(); ++i)
      if (sdflksdfld[i] == -1 && dfs(i)) run = 1;
  }
  int par = 0;
  for (int i = 0; i < ver.size(); ++i)
    if (sdflksdfld[i] != -1) {
      G[sdflksdfld[i]][1].push_back(i);
      ++par;
    }
  for (int i = 0; i < ver.size(); ++i) {
    for (int to : g[i])
      if (sdflksdfld[i] != to) {
        G[i][0].push_back(to);
      }
  }
  for (int i = 0; i < ver.size(); ++i)
    if (sdflksdfld[i] == -1) go(i);
  vector<pair<int, int>> ans;
  for (int i = 0; i < ver.size(); ++i)
    if (was[i][0]) ans.push_back({i, 0});
  for (int i = 0; i < hor.size(); ++i)
    if (was[i][1] == 0) ans.push_back({i, 1});
  for (int i = 0; i < ans.size(); ++i) {
    if (ans[i].second == 0) {
      int id = ans[i].first;
      int x = ver[id].first;
      int l = ver[id].second.first;
      int r = ver[id].second.second;
      A[x].push_back({l, r});
    } else {
      int id = ans[i].first;
      int y = hor[id].first;
      int l = hor[id].second.first;
      int r = hor[id].second.second;
      B[y].push_back({l, r});
    }
  }
  vector<pair<int, pair<int, int>>> ansx, ansy;
  for (auto &v : A) {
    sort(v.second.begin(), v.second.end());
    pair<int, int> cur = {-1, -1};
    int x = v.first;
    for (int i = 0; i < v.second.size(); ++i) {
      int l = v.second[i].first, r = v.second[i].second;
      if (l == cur.second) {
        cur = {cur.first, r};
      } else {
        if (cur.first > 0) ansx.push_back({x, cur});
        cur = {l, r};
      }
    }
    if (cur.first > 0) ansx.push_back({x, cur});
  }
  for (auto &v : B) {
    sort(v.second.begin(), v.second.end());
    pair<int, int> cur = {-1, -1};
    int y = v.first;
    for (int i = 0; i < v.second.size(); ++i) {
      int l = v.second[i].first, r = v.second[i].second;
      if (l == cur.second) {
        cur = {cur.first, r};
      } else {
        if (cur.first > 0) ansy.push_back({y, cur});
        cur = {l, r};
      }
    }
    if (cur.first > 0) ansy.push_back({y, cur});
  }
  cout << ansy.size() << '\n';
  for (auto &v : ansy) {
    cout << v.second.first << ' ' << v.first << ' ' << v.second.second << ' '
         << v.first << '\n';
  }
  cout << ansx.size() << '\n';
  for (auto &v : ansx) {
    cout << v.first << ' ' << v.second.first << ' ' << v.first << ' '
         << v.second.second << '\n';
  }
  return 0;
}
