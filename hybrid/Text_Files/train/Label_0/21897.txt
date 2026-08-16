#include <bits/stdc++.h>
using namespace std;
int SET(int n, int pos) { return n = n | (1 << pos); }
int RESET(int n, int pos) { return n = n & ~(1 << pos); }
int CHECK(int n, int pos) { return (bool)(n & (1 << pos)); }
int bigMod(int n, int power, int MOD) {
  if (power == 0) return 1;
  if (power % 2 == 0) {
    int ret = bigMod(n, power / 2, MOD);
    return ((ret % MOD) * (ret % MOD)) % MOD;
  } else
    return ((n % MOD) * (bigMod(n, power - 1, MOD) % MOD)) % MOD;
}
int modInverse(int n, int MOD) { return bigMod(n, MOD - 2, MOD); }
int POW(int x, int y) {
  int res = 1;
  for (; y;) {
    if ((y & 1)) {
      res *= x;
    }
    x *= x;
    y >>= 1;
  }
  return res;
}
int inverse(int x) {
  double p = ((double)1.0) / x;
  return (p) + 1e-9;
}
int gcd(int a, int b) {
  while (b) b ^= a ^= b ^= a %= b;
  return a;
}
int nC2(int n) { return n * (n - 1) / 2; }
int MOD(int n, int mod) {
  if (n >= 0)
    return n % mod;
  else if (-n == mod)
    return 0;
  else
    return mod + (n % mod);
}
vector<int> vec[1000001], ans[1000001];
int vis[1000001];
int ara[1000001];
int ind[1000001];
int n, m;
bool ok = true;
void foo(int u, int num) {
  vis[u] = 1;
  for (int i = 0; i < vec[u].size(); i++) {
    int v = vec[u][i];
    if (!vis[v]) {
      ans[num].push_back(ara[v]);
      ind[v] = num;
      foo(v, num);
    }
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    cin >> ara[i];
  }
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    vec[a].push_back(b);
    vec[b].push_back(a);
  }
  int level = 1;
  for (int i = 1; i <= n; i++) {
    if (!vis[i]) {
      ans[level].push_back(ara[i]);
      ind[i] = level;
      foo(i, level);
      level++;
    }
  }
  for (int i = 1; i <= n; i++) {
    sort(ans[i].begin(), ans[i].end());
  }
  for (int i = 1; i <= n; i++) {
    cout << ans[ind[i]].back() << " ";
    ans[ind[i]].pop_back();
  }
  return 0;
}
