#include <bits/stdc++.h>
using namespace std;
vector<pair<long long, long long> > vec[300005];
long long d[300005], r[300005], cost[300005];
long long val = 300005, temp;
long long rev;
void dfs(int node, int parent, int dist, int inv) {
  d[node] = dist;
  r[node] = inv;
  for (int i = 0; i < vec[node].size(); i++) {
    pair<long long, long long> p = vec[node][i];
    long long u = p.first;
    if (u == parent) continue;
    dfs(u, node, dist + 1, inv + p.second);
    rev += p.second;
  }
}
int main() {
  long long n;
  cin >> n;
  for (int i = 0; i < n - 1; i++) {
    int x, y;
    cin >> x >> y;
    vec[x].push_back(make_pair(y, 0));
    vec[y].push_back(make_pair(x, 1));
  }
  dfs(1, 0, 0, 0);
  for (int i = 1; i <= n; i++) {
    cost[i] = rev - r[i] + (d[i] - r[i]);
    if (cost[i] < val) val = cost[i];
  }
  cout << val << endl;
  for (int i = 1; i <= n; i++)
    if (cost[i] == val) cout << i << " ";
  return 0;
}
