#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 10;
const int mod = 1e9 + 7;
long long val[maxn], res;
vector<int> g[maxn];
int n, m;
long long gcd(long long a, long long b) { return !b ? a : gcd(b, a % b); }
void dfs(int u, int fa, map<long long, long long> mp) {
  map<long long, long long> tp;
  for (auto it : mp) {
    long long g = gcd(it.first, val[u]);
    res = (res + g * it.second % mod) % mod;
    tp[g] += it.second;
  }
  mp.clear();
  tp[val[u]]++, res = (res + val[u]) % mod;
  for (auto it : g[u]) {
    if (it == fa) continue;
    dfs(it, u, tp);
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%lld", &val[i]);
  for (int i = 1; i < n; i++) {
    int u, v;
    scanf("%d%d", &u, &v);
    g[u].push_back(v);
    g[v].push_back(u);
  }
  map<long long, long long> mp;
  dfs(1, 0, mp);
  printf("%lld\n", res);
  return 0;
}
