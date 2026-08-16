#include <bits/stdc++.h>
using namespace std;
vector<pair<int, int> > xy;
bool used[103] = {false};
int n = 0, ans = -1;
void dfs(int v) {
  used[v] = true;
  for (int i = 0; i < n; i++) {
    if (used[i]) continue;
    if (xy[i].first == xy[v].first || xy[i].second == xy[v].second) dfs(i);
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n;
  xy.resize(n);
  for (int i = 0; i < n; i++) cin >> xy[i].first >> xy[i].second;
  for (int i = 0; i < n; i++)
    if (!used[i]) {
      ans++;
      dfs(i);
    }
  cout << ans;
  return 0;
}
