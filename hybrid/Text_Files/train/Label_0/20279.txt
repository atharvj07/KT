#include <bits/stdc++.h>
using namespace std;
int n, m, k, w;
int diff(string &a, string &b) {
  int ans = 0;
  for (int i = 0; i < a.size(); ++i) {
    if (a[i] != b[i]) ans += w;
  }
  return ans;
}
vector<string> arr;
int master[1001];
int dist[1001];
bool visited[1001];
int ans;
vector<pair<int, int> > levels;
int main() {
  ios_base::sync_with_stdio(false);
  cin >> n >> m >> k >> w;
  arr.resize(k + 1);
  for (int i = 1; i <= k; ++i) {
    char t;
    for (int j = 0; j < n * m; ++j) {
      cin >> t;
      arr[i].push_back(t);
    }
  }
  for (int i = 1; i <= 1000; ++i) {
    dist[i] = n * m;
    master[i] = 0;
  }
  visited[0] = true;
  for (int ii = 1; ii <= k; ++ii) {
    int pos = 0;
    for (int i = 1; i <= k; ++i) {
      if (visited[i]) continue;
      if (visited[pos] || dist[i] < dist[pos]) pos = i;
    }
    visited[pos] = true;
    ans += (dist[pos]);
    levels.push_back(make_pair(pos, master[pos]));
    for (int i = 1; i <= k; ++i) {
      int d = diff(arr[i], arr[pos]);
      if (dist[i] > d) {
        master[i] = pos;
        dist[i] = d;
      }
    }
  }
  cout << ans << endl;
  for (int i = 0; i < levels.size(); ++i) {
    cout << levels[i].first << ' ' << levels[i].second << endl;
  }
}
