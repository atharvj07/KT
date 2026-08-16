#include <bits/stdc++.h>
using namespace std;
const long long linf = 1e18 + 5;
int mod = (int)1e9 + 7;
const int logN = 18;
const int inf = 1e9 + 9;
const int N = 3e5 + 5;
int n, m, x, y, z, t, c[N], p, sum[N], h[N];
double G[N];
vector<pair<int, int> > v[N];
vector<pair<double, int> > ans;
int prep(int node, int root) {
  sum[node] = 1;
  for (__typeof(v[node].begin()) it = v[node].begin(); it != v[node].end();
       it++)
    if (!h[it->first] && it->first != root) sum[node] += prep(it->first, node);
  return sum[node];
}
int find(int node, int root, int S) {
  for (__typeof(v[node].begin()) it = v[node].begin(); it != v[node].end();
       it++)
    if (it->first != root && !h[it->first] && sum[it->first] > S)
      return find(it->first, node, S);
  return node;
}
double dfs(int node, int root, int dist) {
  double ans = dist * sqrt(dist) * c[node];
  for (__typeof(v[node].begin()) it = v[node].begin(); it != v[node].end();
       it++)
    if (it->first != root) ans += dfs(it->first, node, dist + it->second);
  return ans;
}
double dfs2(int node, int root, int dist) {
  double ans = sqrt(dist) * c[node];
  for (__typeof(v[node].begin()) it = v[node].begin(); it != v[node].end();
       it++)
    if (it->first != root) ans += dfs2(it->first, node, dist + it->second);
  return ans;
}
void find(int node) {
  prep(node, 0);
  node = find(node, 0, sum[node] / 2);
  h[node] = 1;
  int S = 0;
  double all = 0;
  ans.push_back(make_pair(dfs(node, 0, 0), node));
  double d2 = 0, temp;
  for (__typeof(v[node].begin()) it = v[node].begin(); it != v[node].end();
       it++) {
    if (!h[it->first]) {
      d2 += dfs2(it->first, node, it->second);
    }
  }
  for (__typeof(v[node].begin()) it = v[node].begin(); it != v[node].end();
       it++) {
    if (!h[it->first] && d2 - 2 * dfs2(it->first, node, it->second) < 0) {
      find(it->first);
      return;
    }
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &c[i]);
  }
  for (int i = 2; i <= n; i++) {
    scanf("%d %d %d", &x, &y, &z);
    v[x].push_back(make_pair(y, z));
    v[y].push_back(make_pair(x, z));
  }
  find(1);
  sort(ans.begin(), ans.end());
  printf("%d %.12lf\n", ans.begin()->second, ans.begin()->first);
  return 0;
}
