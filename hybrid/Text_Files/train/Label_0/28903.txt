#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
bool done[N];
long long a[N];
map<long long, long long> cnt;
struct UnionFind {
  int sz[N], par[N];
  void initialize(int n) {
    for (int i = 0; i <= n; i++) {
      sz[i] = 1, par[i] = i;
    }
  }
  int root(int u) { return par[u] == u ? u : par[u] = root(par[u]); }
  bool merge(int u, int v) {
    u = root(u), v = root(v);
    if (u == v) return false;
    if (sz[u] > sz[v]) swap(u, v);
    par[v] = u, sz[u] += sz[v];
    return true;
  }
} helper;
int main() {
  helper.initialize(N - 2);
  int n, x;
  cin >> n >> x;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    cnt[a[i]]++;
  }
  long long ans = 0;
  for (int i = 0; i < n; i++) {
    long long need = a[i] ^ x;
    if (!cnt.count(need)) continue;
    if (a[i] == need and !done[need]) {
      ans += cnt[need] * (cnt[need] - 1) / 2;
      done[need] = 1;
      continue;
    }
    if (!helper.merge(a[i], need)) continue;
    ans += cnt[need] * cnt[a[i]];
  }
  cout << ans << endl;
}
