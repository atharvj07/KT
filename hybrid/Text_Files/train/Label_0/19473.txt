#include <bits/stdc++.h>
using namespace std;
const long long N = 5e5 + 9;
vector<long long> adj[N], vec[N];
long long h[N], up[N], ans[N];
pair<long long, long long> edge[N];
vector<pair<long long, long long> > a[N], b;
void DFS1(long long u, long long par) {
  h[u] = 1;
  for (long long v : adj[u])
    if (v != par) {
      DFS1(v, u);
      h[u] = max(h[u], h[v] + 1);
      vec[u].push_back(h[v]);
    }
}
void DFS2(long long u, long long par) {
  multiset<long long> s;
  for (long long v : adj[u])
    if (v != par) s.insert(-h[v]);
  for (long long v : adj[u])
    if (v != par) {
      s.erase(s.find(-h[v]));
      up[v] = up[u] + 1;
      if (!s.empty()) up[v] = max(up[v], -(*s.begin()) + 1);
      vec[v].push_back(up[v]);
      s.insert(-h[v]);
    }
  for (long long v : adj[u])
    if (v != par) DFS2(v, u);
}
void DFS3(long long u, long long par) {
  for (long long v : adj[u])
    if (v != par) {
      long long iu = 0, iv = 0;
      while (iu < a[u].size() && iv < a[v].size()) {
        if (a[u][iu].first < a[v][iv].first)
          b.push_back(a[u][iu++]);
        else if (a[u][iu].first > a[v][iv].first)
          b.push_back(a[v][iv++]);
        else if (a[u][iu].first == a[v][iv].first)
          b.push_back({a[v][iv].first, a[v][iv++].second + a[u][iu++].second});
      }
      while (iv < a[v].size()) b.push_back(a[v][iv++]);
      while (iu < a[u].size()) b.push_back(a[u][iu++]);
      for (long long i = 0; i < b.size(); i++) {
        if (b[i].first == up[v]) b[i].second--;
        if (b[i].first == h[v]) b[i].second--;
      }
      long long num = 0;
      while (b.size()) {
        ans[b.back().first * 2] =
            max(ans[b.back().first * 2], (num += b.back().second));
        b.pop_back();
      }
      DFS3(v, u);
    }
}
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  long long n;
  cin >> n;
  for (long long i = 1; i < n; i++) {
    long long u, v;
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  fill(ans, ans + N, 1);
  DFS1(1, 0);
  DFS2(1, 0);
  for (long long i = 1; i <= n; i++) {
    sort(vec[i].begin(), vec[i].end());
    for (long long j = 0; j < vec[i].size() - 1; j++)
      if (vec[i][j] != vec[i][j + 1])
        ans[vec[i][j] * 2 + 1] =
            max(ans[vec[i][j] * 2 + 1], (long long)vec[i].size() - j);
    for (long long j = 0; j < vec[i].size(); j++)
      ans[vec[i][j] * 2 - 1] =
          max(ans[vec[i][j] * 2 - 1], (long long)vec[i].size() - j),
                          ans[vec[i][j] * 2] = max(
                              ans[vec[i][j] * 2], (long long)vec[i].size() - j);
    for (long long j = 0, k = 0; max(j, k) < vec[i].size(); j = k) {
      while (k < vec[i].size() && vec[i][j] == vec[i][k]) k++;
      a[i].push_back({vec[i][j], k - j});
    }
  }
  DFS3(1, 0);
  for (long long i = n; i > 0; i--) ans[i] = max(ans[i], ans[i + 2]);
  for (long long i = 1; i <= n; i++)
    ans[1] = max(ans[1], (long long)adj[i].size() + 1);
  for (long long i = 1; i <= n; i++) cout << ans[i] << " ";
  return 0;
}
