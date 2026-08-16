#include <bits/stdc++.h>
using namespace std;
const int tinf = (int)1e9 + 7;
const long long inf = (long long)1e18 + 7;
const int N = 4e5 + 5;
vector<vector<long long> > g(N);
long long used[N], tin[N], tout[N], up[N][40], l, timer, n, q, cnt[N];
void dfs(long long v, long long p = 0) {
  used[v] = 1;
  up[v][0] = p;
  tin[v] = timer++;
  cnt[v] = (v != p) * (cnt[p] + 1);
  for (int i = 1; i <= l; i++) up[v][i] = up[up[v][i - 1]][i - 1];
  for (auto i : g[v]) {
    if (i != p) dfs(i, v);
  }
  tout[v] = timer++;
}
bool upper(long long a, long long b) {
  return tin[a] <= tin[b] && tout[a] >= tout[b];
}
long long lca(long long a, long long b) {
  if (upper(a, b)) return a;
  if (upper(b, a)) return b;
  for (int i = l; i >= 0; i--) {
    if (!upper(up[a][i], b)) {
      a = up[a][i];
    }
  }
  return up[a][0];
}
long long solver(long long second, long long t, long long first) {
  long long ans = 0;
  bool is1 = lca(first, second) == first, is2 = lca(first, t) == first;
  if (is1 != is2) return 1;
  if (is1)
    ans = max(ans, cnt[lca(second, t)] - cnt[first]);
  else if (lca(first, second) != lca(first, t))
    ans =
        max(ans, cnt[first] - max(cnt[lca(first, second)], cnt[lca(first, t)]));
  else
    ans = max(ans, cnt[first] + cnt[lca(second, t)] - 2 * cnt[lca(first, t)]);
  return ans + 1;
}
void solve() {
  long long a[3], ans = -inf;
  cin >> a[0] >> a[1] >> a[2];
  a[0]--, a[1]--, a[2]--;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      for (int z = 0; z < 3; z++) {
        if (i != j && i != z && j != z) {
          ans = max(ans, solver(a[i], a[j], a[z]));
        }
      }
    }
  }
  cout << ans << endl;
}
int main() {
  {
    ios ::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
  }
  cin >> n >> q;
  while ((1 << l) <= n) l++;
  for (int i = 1; i < n; i++) {
    long long p;
    cin >> p;
    p--;
    g[i].push_back(p);
    g[p].push_back(i);
  }
  dfs(0);
  for (int i = 0; i < q; i++) {
    solve();
  }
}
