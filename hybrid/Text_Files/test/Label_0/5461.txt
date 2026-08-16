#include <bits/stdc++.h>
using namespace std;
int n, m, a, b, w, start = 0, k;
long long int MAX = 1e18;
vector<vector<int> > wait(100005);
vector<vector<pair<int, int> > > adj(100005);
void binarySearch(int v, long long int& d) {
  if (wait[v].size() == 0) {
    return;
  }
  int low = 0, high = wait[v].size() - 1, mid;
  while (low <= high) {
    mid = (low + high) >> 1;
    if (wait[v][mid] == d) {
      ++d;
      ++mid;
      while (mid <= wait[v].size() - 1 and
             wait[v][mid] == wait[v][mid - 1] + 1) {
        ++d;
        ++mid;
      }
      return;
    } else if (wait[v][mid] > d) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return;
}
int main(void) {
  ios ::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i <= m - 1; ++i) {
    cin >> a >> b >> w;
    --a;
    --b;
    adj[a].push_back({b, w});
    adj[b].push_back({a, w});
  }
  for (int i = 0; i <= n - 2; ++i) {
    cin >> k;
    for (int j = 1; j <= k; ++j) {
      cin >> w;
      wait[i].emplace_back(w);
    }
  }
  set<pair<long long int, int> > s;
  vector<long long int> dist(n, MAX);
  vector<int> present(n, 1);
  dist[start] = 0;
  for (int i = 0; i <= n - 1; ++i) {
    s.insert({dist[i], i});
  }
  while (!s.empty()) {
    auto c = *(s.begin());
    s.erase(c);
    int v = c.second;
    present[v] = 0;
    binarySearch(v, dist[v]);
    for (auto e : adj[v]) {
      int u = e.first;
      w = e.second;
      if (present[u] and dist[u] > dist[v] + 1LL * w) {
        s.erase({dist[u], u});
        dist[u] = dist[v] + 1LL * w;
        s.insert({dist[u], u});
      }
    }
  }
  if (dist[n - 1] == MAX) {
    cout << -1 << endl;
  } else {
    cout << dist[n - 1] << endl;
  }
  return 0;
}
