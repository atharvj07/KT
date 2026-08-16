#include <bits/stdc++.h>
using namespace std;
int n, a[100005];
vector<int> g[100005];
long long x, sum = 0, lcm = 1;
long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
void dfs(int cur = 1, long long div = 1LL, int fa = -1) {
  if (div > x) {
    cout << sum;
    exit(0);
    return;
  }
  if (a[cur] || g[cur].size() <= 1 && cur != 1) {
    x = min(x, a[cur] * div);
    lcm = div * lcm / gcd(lcm, div);
    return;
  }
  for (int i = 0; i < g[cur].size(); i++) {
    if (g[cur][i] != fa)
      dfs(g[cur][i], div * (long long)(g[cur].size() - 1 * (cur != 1)), cur);
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &a[i]);
    sum += a[i];
  }
  x = sum;
  int u, v;
  for (int i = 1; i < n; i++) {
    scanf("%d%d", &u, &v);
    g[u].push_back(v);
    g[v].push_back(u);
  }
  dfs(1, 1, -1);
  cout << sum - x + x % lcm;
  return 0;
}
