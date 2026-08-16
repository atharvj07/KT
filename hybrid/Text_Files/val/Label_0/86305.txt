#include <bits/stdc++.h>
using namespace std;
bool operator<(const pair<int, long long>& e1, const pair<int, long long>& e2) {
  if (e1.first != e2.first) return e1.first < e2.first;
  return e1.second < e2.second;
}
pair<int, long long> operator+(const pair<int, long long>& e1,
                               const pair<int, long long>& e2) {
  return {e1.first + e2.first, e1.second + e2.second};
}
int t, n, m;
vector<pair<int, long long> > DP[3010];
vector<int> e[3010];
vector<pair<int, long long> > step(const vector<pair<int, long long> >& fa,
                                   const vector<pair<int, long long> >& fb) {
  vector<pair<int, long long> > ret(fa.size() + fb.size(), {-1, 0});
  for (int a = 0; a < (int)fa.size(); ++a) {
    for (int b = 0; b < (int)fb.size(); ++b) {
      ret[a + b] = max(ret[a + b], fa[a] + fb[b]);
      pair<int, long long> bvar = fb[b];
      if (bvar.second > 0) ++bvar.first;
      bvar.second = 0;
      ret[a + b + 1] = max(ret[a + b + 1], fa[a] + bvar);
    }
  }
  return ret;
}
void dfs(int node, int p) {
  for (int ch : e[node]) {
    if (ch == p) continue;
    dfs(ch, node);
    DP[node] = step(DP[node], DP[ch]);
  }
}
void solve() {
  cin >> n >> m;
  for (int i = 0; i < n; ++i) {
    DP[i] = {{0, 0}};
    e[i].clear();
    int x;
    cin >> x;
    DP[i][0].second = -x;
  }
  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    DP[i][0].second += x;
  }
  for (int i = 1; i < n; ++i) {
    int x, y;
    cin >> x >> y;
    --x, --y;
    e[x].push_back(y), e[y].push_back(x);
  }
  dfs(0, -1);
  int ans = DP[0][m - 1].first;
  if (DP[0][m - 1].second > 0) ++ans;
  cout << ans << endl;
}
int main() {
  ios::sync_with_stdio(false);
  cin >> t;
  while (t--) solve();
  return 0;
}
