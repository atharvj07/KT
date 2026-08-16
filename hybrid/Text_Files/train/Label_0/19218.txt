#include <bits/stdc++.h>
using namespace std;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
char dir[] = {'R', 'L', 'D', 'U'};
const int MOD = 1e9 + 7;
const long long INF = 1e9;
void setIO(string filename) {
  if (fopen((filename + ".in").c_str(), "r")) {
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
  }
}
template <class T>
void printvec(vector<T> a) {
  for (T i : a) cout << i << " ";
  cout << "\n";
}
int dia(vector<vector<int>> adj) {
  int startnode = 0;
  for (int i = 0; i < adj.size(); i++)
    if (!adj[i].empty()) {
      startnode = i;
      break;
    }
  int longnode = -1, longdist = -1;
  queue<pair<int, int>> q;
  q.push(make_pair(startnode, 0));
  vector<bool> v(adj.size());
  v[startnode] = 1;
  while (!q.empty()) {
    pair<int, int> curr = q.front();
    q.pop();
    if (curr.second > longdist) {
      longdist = curr.second;
      longnode = curr.first;
    }
    for (int adjnode : adj[curr.first]) {
      if (v[adjnode]) continue;
      v[adjnode] = 1;
      q.push(make_pair(adjnode, curr.second + 1));
    }
  }
  fill((v).begin(), (v).end(), 0);
  q.push(make_pair(longnode, 0));
  int ans = 0;
  v[longnode] = 1;
  while (!q.empty()) {
    pair<int, int> curr = q.front();
    q.pop();
    ans = max(ans, curr.second);
    for (int adjnode : adj[curr.first]) {
      if (v[adjnode]) continue;
      v[adjnode] = 1;
      q.push(make_pair(adjnode, curr.second + 1));
    }
  }
  return ans;
}
void solve() {
  if (fopen("input.txt", "r")) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  }
  int n;
  cin >> n;
  vector<vector<vector<int>>> adj(n);
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    adj[i].resize(x);
    for (int j = 0; j < x - 1; j++) {
      int u, v;
      cin >> u >> v;
      u--;
      v--;
      adj[i][u].push_back(v);
      adj[i][v].push_back(u);
    }
  }
  int ans = 0;
  for (auto i : adj) {
    ans += dia(i);
  }
  cout << ans << "\n";
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int t = 1;
  for (int i = 1; i <= t; i++) solve();
}
