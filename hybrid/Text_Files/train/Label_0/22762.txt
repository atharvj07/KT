#include <bits/stdc++.h>
using namespace std;
long long solve(void) {
  int n;
  cin >> n;
  vector<int> p(n), c(n);
  for (auto &v : p) {
    cin >> v;
    v--;
  }
  for (int i(0); i < n; ++i) cin >> c[i];
  vector<bool> visited(n, false);
  vector<vector<int>> cycles;
  for (int i(0); i < n; ++i) {
    if (visited[i]) continue;
    vector<int> v;
    v.push_back(i);
    int j = p[i];
    visited[i] = true;
    while (i != j) {
      v.push_back(j);
      visited[j] = true;
      j = p[j];
    }
    cycles.push_back(v);
  }
  int ans(n);
  for (int i(0); i < ((int)(cycles).size()); ++i) {
    for (int d(1); d * d <= ((int)(cycles[i]).size()); ++d) {
      if (((int)(cycles[i]).size()) % d) continue;
      for (int j(0); j < ((int)(cycles[i]).size()); ++j) visited[j] = false;
      for (int s(0); s < ((int)(cycles[i]).size()); ++s) {
        if (visited[s]) continue;
        int j = (s + d) % ((int)(cycles[i]).size());
        visited[s] = true;
        bool found(true);
        while (j != s) {
          visited[j] = true;
          if (c[cycles[i][s]] != c[cycles[i][j]]) found = false;
          j = (j + d) % ((int)(cycles[i]).size());
        }
        if (found) {
          ans = min(ans, d);
          break;
        }
      }
      int dd = ((int)(cycles[i]).size()) / d;
      for (int j(0); j < ((int)(cycles[i]).size()); ++j) visited[j] = false;
      for (int s(0); s < ((int)(cycles[i]).size()); ++s) {
        if (visited[s]) continue;
        int j = (s + dd) % ((int)(cycles[i]).size());
        visited[s] = true;
        bool found(true);
        while (j != s) {
          visited[j] = true;
          if (c[cycles[i][s]] != c[cycles[i][j]]) found = false;
          j = (j + dd) % ((int)(cycles[i]).size());
        }
        if (found) {
          ans = min(ans, dd);
          break;
        }
      }
    }
  }
  return ans;
}
int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t;
  cin >> t;
  while (t--) cout << solve() << '\n';
}
