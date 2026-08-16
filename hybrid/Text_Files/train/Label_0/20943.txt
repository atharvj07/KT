#include <bits/stdc++.h>
using namespace std;
const int nax = 103;
const int mod = 1e9 + 7;
const int inf = (int)1e9;
const long long infll = (long long)1e18;
const long double PI = 3.1415926535897932384626433832795;
vector<int> gr[nax];
vector<bool> vis(nax), spoken(nax);
void Dfs(int node) {
  vis[node] = true;
  for (int& it : gr[node]) {
    if (!vis[it]) {
      Dfs(it);
    }
  }
}
void solve() {
  int n, m;
  cin >> n >> m;
  int ans = 0;
  for (int i = 0; i < n; ++i) {
    int nr;
    cin >> nr;
    if (!nr) {
      ++ans;
      continue;
    }
    int x, y;
    cin >> x;
    spoken[x] = true;
    while (--nr) {
      cin >> y;
      spoken[y] = true;
      gr[x].push_back(y);
      gr[y].push_back(x);
      x = y;
    }
  }
  int cnt = 0;
  for (int i = 1; i < m + 1; ++i) {
    if (!vis[i] && spoken[i]) {
      ++cnt;
      Dfs(i);
    }
  }
  ans += max(0, cnt - 1);
  cout << ans;
}
int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  int t = 1;
  while (t--) {
    solve();
  }
}
