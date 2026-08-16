#include <bits/stdc++.h>
using namespace std;
const long long MAXN = 2222, INF = 1e9;
vector<pair<long long, long long> > adj[MAXN];
long long val[MAXN];
long long dis[MAXN], dis2[MAXN], dp[MAXN][MAXN][2], su[MAXN][MAXN],
    ti[MAXN][MAXN], second[MAXN][MAXN], T[MAXN][MAXN];
long long n, m, s, t;
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  cin >> s >> t;
  for (long long i = 1; i <= n; i++) cin >> val[i];
  for (long long i = 0; i < m; i++) {
    long long x, y, z;
    cin >> x >> y >> z;
    adj[x].push_back({y, z});
    adj[y].push_back({x, z});
  }
  set<pair<long long, long long> > ss;
  memset(dis, 63, sizeof dis);
  dis[s] = 0;
  ss.insert({0, s});
  while (ss.size()) {
    long long x = ss.begin()->second;
    ss.erase(ss.begin());
    for (auto v : adj[x]) {
      if (dis[v.first] > dis[x] + v.second) {
        ss.erase({dis[v.first], v.first});
        dis[v.first] = dis[x] + v.second;
        ss.insert({dis[v.first], v.first});
      }
    }
  }
  memset(dis2, 63, sizeof dis2);
  dis2[t] = 0;
  ss.insert({0, t});
  while (ss.size()) {
    long long x = ss.begin()->second;
    ss.erase(ss.begin());
    for (auto v : adj[x]) {
      if (dis2[v.first] > dis2[x] + v.second) {
        ss.erase({dis2[v.first], v.first});
        dis2[v.first] = dis2[x] + v.second;
        ss.insert({dis2[v.first], v.first});
      }
    }
  }
  {
    vector<long long> v;
    for (long long i = 1; i <= n; i++) v.push_back(dis[i]);
    sort(v.begin(), v.end());
    v.resize(unique(v.begin(), v.end()) - v.begin());
    for (long long i = 1; i <= n; i++)
      dis[i] = lower_bound(v.begin(), v.end(), dis[i]) - v.begin();
  }
  {
    vector<long long> v;
    for (long long i = 1; i <= n; i++) v.push_back(dis2[i]);
    sort(v.begin(), v.end());
    v.resize(unique(v.begin(), v.end()) - v.begin());
    for (long long i = 1; i <= n; i++)
      dis2[i] = lower_bound(v.begin(), v.end(), dis2[i]) - v.begin();
  }
  for (long long i = 1; i <= n; i++)
    su[dis[i]][dis2[i]] += val[i], ti[dis[i]][dis2[i]]++;
  for (long long i = n + 2; i >= 0; i--) {
    for (long long j = n + 2; j >= 0; j--) {
      second[i][j] =
          su[i][j] + second[i + 1][j] + second[i][j + 1] - second[i + 1][j + 1];
      T[i][j] = ti[i][j] + T[i + 1][j] + T[i][j + 1] - T[i + 1][j + 1];
    }
  }
  for (long long i = n; i >= 0; i--) {
    for (long long j = n; j >= 0; j--) {
      if (!T[i][j]) continue;
      dp[i][j][0] = -1e18;
      long long sum = (second[i][j] - second[i + 1][j]);
      long long ted = (T[i][j] - T[i + 1][j]);
      if (ted) dp[i][j][0] = sum + dp[i + 1][j][1];
      dp[i][j][0] = max(dp[i][j][0], sum + dp[i + 1][j][0]);
      sum = (second[i][j] - second[i][j + 1]);
      ted = (T[i][j] - T[i][j + 1]);
      dp[i][j][1] = 1e18;
      if (ted) dp[i][j][1] = -sum + dp[i][j + 1][0];
      dp[i][j][1] = min(dp[i][j][1], -sum + dp[i][j + 1][1]);
    }
  }
  if (dp[0][0][0] > 0) cout << "Break a heart";
  if (dp[0][0][0] == 0) cout << "Flowers";
  if (dp[0][0][0] < 0) cout << "Cry";
}
