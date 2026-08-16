#include <bits/stdc++.h>
using namespace std;
int l[51], r[51], a[51], c[51], dp[51][51][51];
void inline FilterRestrictions(int i, int j, int h, vector<int> &v) {
  vector<int> u;
  for (int x : v) {
    if (r[x] < i || j < l[x] || a[x] >= h) {
      continue;
    }
    u.push_back(x);
  }
  v = u;
  u.clear();
  sort(v.begin(), v.end(), [](int i, int j) { return l[i] > l[j]; });
}
int Solve(int i, int j, int h, vector<int> v) {
  if (j < i) {
    return 0;
  }
  if (dp[i][j][h] != -1) {
    return dp[i][j][h];
  }
  FilterRestrictions(i, j, h, v);
  int ans = Solve(i, j, h - 1, v), cost = h * h;
  vector<vector<int> > V(51 + 1);
  vector<int> v1;
  for (int x = i; x <= j; ++x) {
    for (; !v.empty() && l[v.back()] == x; v.pop_back()) {
      int k = v.back();
      cost -= c[k];
      V[r[k] + 1].push_back(k);
    }
    for (auto k : V[x]) {
      cost += c[k];
      v1.push_back(k);
    }
    int ansx = cost + Solve(i, x - 1, h, v1) + Solve(x + 1, j, h, v);
    ans = max(ans, ansx);
  }
  dp[i][j][h] = ans;
  return ans;
}
int main() {
  int n, h, m;
  cin >> n >> h >> m;
  for (int i = 1; i <= m; ++i) {
    cin >> l[i] >> r[i] >> a[i] >> c[i];
  }
  vector<int> v;
  for (int i = 1; i <= m; ++i) {
    v.push_back(i);
  }
  for (int i = 1; i <= n; ++i) {
    for (int j = i; j <= n; ++j) {
      for (int x = 1; x <= h; ++x) {
        dp[i][j][x] = -1;
      }
    }
  }
  cout << Solve(1, n, h, v) << '\n';
  return 0;
}
