#include <bits/stdc++.h>
using namespace std;
const int maxn = 200005;
int n, m, dp[maxn], pre[maxn], ed;
bool vis[maxn];
vector<int> fac[maxn], ans, py, G[maxn];
int gcd(int a, int b) { return !b ? a : gcd(b, a % b); }
long long extgcd(long long a, long long b, long long &x, long long &y) {
  if (!b) {
    x = 1;
    y = 0;
    return a;
  }
  long long g = extgcd(b, a % b, y, x);
  y -= a / b * x;
  return g;
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; ++i) {
    int t;
    scanf("%d", &t);
    vis[t] = 1;
  }
  for (int i = 1; i < m; ++i)
    if (!vis[i]) fac[gcd(i, m)].push_back(i);
  for (int i = 1; i < m; ++i)
    for (int j = i + i; j < m; j += i) G[i].push_back(j);
  for (int u = 1; u < m; ++u) {
    dp[u] = max(dp[u], (int)fac[u].size());
    for (auto j : G[u]) {
      int v = j, w = fac[j].size();
      if (dp[v] < dp[u] + w) {
        dp[v] = dp[u] + w;
        pre[v] = u;
      }
    }
    if (dp[u] > dp[ed]) ed = u;
  }
  while (ed) {
    for (int i : fac[ed]) ans.push_back(i);
    ed = pre[ed];
  }
  reverse(ans.begin(), ans.end());
  if (ans.size()) {
    py.push_back(ans[0]);
    long long u = ans[0], v, x, y, g;
    for (int i = 1; i < (int)ans.size(); ++i) {
      v = m;
      g = extgcd(u, v, x, y);
      x = (x * (ans[i] / g) % m + m) % m;
      u = u * x % m;
      py.push_back(x);
    }
  }
  if (!vis[0]) py.push_back(0);
  printf("%d\n", py.size());
  for (int i = 0; i < (int)py.size(); ++i)
    printf("%d%c", py[i], i + 1 == (int)py.size() ? '\n' : ' ');
  return 0;
}
