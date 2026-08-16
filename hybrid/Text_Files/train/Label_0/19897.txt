#include <bits/stdc++.h>
using namespace std;
long long n, m, q;
long long dp[15][1 << 15];
pair<long long, long long> con[15];
pair<pair<long long, long long>, long long> lca[105];
void myinit() {
  cin >> n >> m >> q;
  for (long long i = 1; i <= m; i++) {
    long long u, v;
    cin >> u >> v;
    u--, v--;
    con[i] = make_pair(u, v);
  }
  for (long long i = 1; i <= q; i++) {
    long long u, v, w;
    cin >> u >> v >> w;
    u--, v--, w--;
    lca[i] = make_pair(make_pair(u, v), w);
  }
}
void dfs(long long root, long long mask) {
  if (dp[root][mask]) return;
  long long maskll = mask;
  mask -= 1 << root;
  if (mask == 0) {
    dp[root][maskll] = 1;
    return;
  }
  long long least = (mask) - ((mask) & ((mask)-1));
  long long newmask = mask, newroot;
  for (newmask = mask; newmask != 0; newmask = (newmask - 1) & mask) {
    if (!(newmask & least)) continue;
    bool was = true;
    long long cnt = 0;
    for (long long i = 1; i <= m; i++) {
      long long u, v;
      u = con[i].first;
      v = con[i].second;
      if (!((maskll) & (1 << u)) || !((maskll) & (1 << v))) continue;
      if (u == root) swap(u, v);
      if (newmask & (1 << u) && newmask & (1 << v) ||
          (maskll - newmask) & (1 << u) && (maskll - newmask) & (1 << v))
        continue;
      if (v == root && newmask & (1 << u)) {
        cnt++;
        newroot = u;
        continue;
      }
      was = false;
    }
    if (cnt > 1 || !was) {
      continue;
    }
    for (long long i = 1; i <= q; i++) {
      long long u, v, w;
      u = lca[i].first.first;
      v = lca[i].first.second;
      w = lca[i].second;
      if (!((maskll) & (1 << u)) || !((maskll) & (1 << v)) ||
          !((maskll) & (1 << w)))
        continue;
      if (w == root) {
        if (u == root || v == root) continue;
        if (newmask & (1 << u) && newmask & (1 << v)) {
          was = false;
          break;
        }
      } else {
        long long t = 0;
        if (newmask & (1 << u)) t++;
        if (newmask & (1 << v)) t++;
        if (newmask & (1 << w)) t++;
        if (t != 0 && t != 3) was = false;
      }
    }
    if (was) {
      if (cnt == 1) {
        dfs(newroot, newmask);
        dfs(root, maskll - newmask);
        dp[root][maskll] += dp[newroot][newmask] * dp[root][maskll - newmask];
      } else {
        for (long long i = 0; i < n; i++) {
          if (newmask & (1 << i)) {
            newroot = i;
            dfs(newroot, newmask);
            dfs(root, maskll - newmask);
            dp[root][maskll] +=
                dp[newroot][newmask] * dp[root][maskll - newmask];
          }
        }
      }
    }
  }
}
int main() {
  myinit();
  dfs(0, (1 << n) - 1);
  cout << dp[0][(1 << n) - 1];
  return 0;
}
