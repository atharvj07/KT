#include <bits/stdc++.h>
using namespace std;
const int N = 3e5 + 10, mod = 998244353;
vector<long long> vec[N];
long long n, f[N][3], g[3];
void dfs(long long u, long long fa) {
  long long v;
  f[u][0] = 1;
  for (int i = 0; i < vec[u].size(); i++) {
    if (vec[u][i] == fa) continue;
    dfs(vec[u][i], u);
    v = vec[u][i];
    g[0] = (f[u][0] * (f[v][0] + f[v][2])) % mod;
    g[1] = (f[u][0] * f[v][2] + f[u][1] * (f[v][0] + f[v][2] * 2)) % mod;
    g[2] = (f[u][0] * (f[v][0] + f[v][1]) + f[u][1] * (f[v][0] + f[v][1]) +
            f[u][2] * (f[v][0] + f[v][2] * 2)) %
           mod;
    swap(g, f[u]);
  }
}
int main() {
  scanf("%lld", &n);
  for (long long i = 1, u, v; i < n; i++) {
    scanf("%lld%lld", &u, &v);
    vec[u].push_back(v);
    vec[v].push_back(u);
  }
  dfs(1, 0);
  printf("%lld\n", (f[1][0] + f[1][2]) % mod);
  return 0;
}
