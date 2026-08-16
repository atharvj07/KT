#include <bits/stdc++.h>
using namespace std;
const int N = 14;
const int Q = 111;
long long memo[N][N][1 << N];
int most[1 << N];
int adj[N];
int eu[N], ev[N];
int qu[Q], qv[Q], qp[Q];
int n, q, m;
long long dp(int u, int p, int mask) {
  long long &ans = memo[u][p][mask];
  if (ans != -1) return ans;
  if (mask == (1 << u)) return ans = 1;
  ans = 0;
  int child = adj[u];
  if (child & (1 << p)) child ^= 1 << p;
  for (int rem = mask ^ (1 << u), first = rem; first;
       first = (first - 1) & rem) {
    if (first & most[rem]) {
      for (int v = 0; v < n; ++v)
        if (first & (1 << v)) {
          if ((first ^ (1 << v)) & child) continue;
          bool checkEdge = 1;
          for (int i = 0; i < m; ++i)
            if (eu[i] != u && ev[i] != u &&
                (first >> eu[i] & 1) != (first >> ev[i] & 1)) {
              checkEdge = 0;
              break;
            }
          if (checkEdge) {
            bool checkLCA = 1;
            for (int i = 0; i < q; ++i)
              if ((mask & (1 << qu[i])) && (mask & (1 << qv[i]))) {
                if (!(mask & (1 << qp[i]))) {
                  checkLCA = 0;
                  break;
                }
                bool uIn = first & (1 << qu[i]);
                bool vIn = first & (1 << qv[i]);
                if ((uIn && vIn && !(first & (1 << qp[i]))) ||
                    (uIn != vIn && qp[i] != u)) {
                  checkLCA = 0;
                  break;
                }
              }
            if (checkLCA) {
              ans += dp(v, u, first) * dp(u, p, mask ^ first);
            }
          }
        }
    }
  }
  return ans;
}
int main() {
  ios::sync_with_stdio(0);
  cin >> n >> m >> q;
  for (int i = 1; i < (1 << n); ++i)
    for (int j = 0; j < n; ++j)
      if (i & (1 << j)) most[i] = 1 << j;
  for (int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    --u, --v;
    adj[u] |= 1 << v;
    adj[v] |= 1 << u;
    eu[i] = u;
    ev[i] = v;
  }
  for (int i = 0; i < q; ++i) {
    int u, v, p;
    cin >> u >> v >> p;
    --u;
    --v;
    --p;
    qu[i] = u;
    qv[i] = v;
    qp[i] = p;
    if (u == v && u != p) {
      cout << 0 << endl;
      return 0;
    }
  }
  memset(memo, -1, sizeof(memo));
  cout << dp(0, N - 1, (1 << n) - 1) << endl;
  return 0;
}
