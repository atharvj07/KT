#include <bits/stdc++.h>
using namespace std;
vector<vector<pair<int, int> > > graph;
vector<pair<int, int> > val;
vector<int> visited;
int ov2 = 1e9;
vector<int> component;
void dfs(int cur) {
  component.push_back(cur);
  visited[cur] = true;
  for (auto a : graph[cur]) {
    int newSign = -val[cur].first;
    int newC = a.second - val[cur].second;
    if (visited[a.first]) {
      if (val[a.first].first == newSign) {
        if (val[a.first].second != newC) {
          cout << "NO\n";
          exit(0);
        }
      } else {
        int ovv2 = (val[a.first].second - newC) * newSign;
        if (ov2 != 1e9 && ovv2 != ov2) {
          cout << "NO\n";
          exit(0);
        }
        ov2 = ovv2;
      }
    } else {
      val[a.first] = {newSign, newC};
      dfs(a.first);
    }
  }
}
vector<long double> ans;
void fillComponent(long long x, long double dv = 1.0) {
  for (auto a : component) ans[a] = x * val[a].first / dv + val[a].second;
}
int32_t main() {
  ios::sync_with_stdio(false);
  int n, m;
  cin >> n >> m;
  graph.resize(n);
  val.resize(n);
  visited.resize(n);
  ans.resize(n);
  for (int i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    graph[a - 1].push_back({b - 1, c});
    graph[b - 1].push_back({a - 1, c});
  }
  for (int i = 0; i < n; i++) {
    if (!visited[i]) {
      component.clear();
      ov2 = 1e9;
      val[i] = {1, 0};
      dfs(i);
      if (ov2 != 1e9) {
        fillComponent(ov2, 2.0);
        continue;
      }
      int SIZ = 2 * component.size() + 4;
      vector<int> cnt(2 * SIZ + 1);
      long long cv = -SIZ;
      long long sumL = 0, sumR = 0;
      for (auto a : component) {
        cnt[val[a].second * val[a].first * -1 + SIZ]++;
        sumR += abs(cv + val[a].second * val[a].first);
      }
      int cntL = 0, cntR = component.size();
      pair<long long, int> res = {sumL + sumR, cv};
      for (; cv <= SIZ; cv++) {
        res = min(res, {sumL + sumR, cv});
        cntL += cnt[cv + SIZ];
        cntR -= cnt[cv + SIZ];
        sumL += cntL;
        sumR -= cntR;
      }
      fillComponent(res.second);
    }
  }
  cout << "YES\n";
  for (auto a : ans) cout << a << " ";
  cout << "\n";
}
