#include <bits/stdc++.h>
using namespace std;
const int N = 3e5 + 400, M = (1 << 20), MX = 1e9;
int n, q, a[N], ojciec[N], kraw[N], dist[N], poz[N], rozmEuler;
vector<pair<int, int> > G[N];
pair<int, int> tree[2 * M + 400];
long long dp[N], dp2[N], odl[N], pom[N], sumek[N];
pair<int, int> query(int a, int b) {
  a += M;
  b += M;
  if (a > b) swap(a, b);
  pair<int, int> wyn = min(tree[a], tree[b]);
  while (a + 1 < b) {
    if (!(a & 1)) wyn = min(wyn, tree[a + 1]);
    if (b & 1) wyn = min(wyn, tree[b - 1]);
    a >>= 1;
    b >>= 1;
  }
  return wyn;
}
void preDFS(int u) {
  dp[u] = a[u];
  tree[M + rozmEuler] = make_pair(dist[u], u);
  poz[u] = rozmEuler++;
  for (auto v : G[u]) {
    if (v.first != ojciec[u]) {
      ojciec[v.first] = u;
      dist[v.first] = dist[u] + 1;
      odl[v.first] = odl[u] + v.second;
      kraw[v.first] = v.second;
      preDFS(v.first);
      tree[M + rozmEuler++] = make_pair(dist[u], u);
      pom[v.first] = max(0LL, dp[v.first] - 2 * v.second);
      dp[u] += pom[v.first];
    }
  }
}
void preDP(int u) {
  dp2[u] = dp[u] + (u != 1 ? max(0LL, dp[ojciec[u]] - 2 * kraw[u]) : 0);
  for (auto v : G[u]) {
    if (v.first != ojciec[u]) {
      long long pomek = dp[u];
      dp[u] = dp2[u] - pom[v.first];
      sumek[v.first] = sumek[u] + dp[v.first] - pom[v.first];
      preDP(v.first);
      dp[u] = pomek;
    }
  }
}
int32_t main() {
  scanf("%d%d", &n, &q);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  for (int i = 1; i < n; i++) {
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    G[a].push_back({b, c});
    G[b].push_back({a, c});
  }
  dist[1] = 1;
  preDFS(1);
  for (int i = M + rozmEuler; i <= 2 * M - 1; i++) tree[i] = make_pair(MX, MX);
  for (int i = M - 1; i >= 1; i--)
    tree[i] = min(tree[i << 1], tree[i << 1 | 1]);
  sumek[1] = dp[1];
  preDP(1);
  while (q--) {
    int a, b;
    scanf("%d%d", &a, &b);
    int u = query(poz[a], poz[b]).second;
    long long wynik = sumek[a] + sumek[b] - 2 * sumek[u] - odl[a] - odl[b] +
                      2 * odl[u] + dp[u];
    if (u != 1) wynik += max(0LL, dp2[ojciec[u]] - pom[u] - 2 * kraw[u]);
    printf("%lld\n", wynik);
  }
  getchar();
  getchar();
  return 0;
}
