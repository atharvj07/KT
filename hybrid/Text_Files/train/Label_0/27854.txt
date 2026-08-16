#include <bits/stdc++.h>
using namespace std;
const long long INF = 1e9, MOD = INF + 7;
const int N = 22, M = (1 << N);
int adj[N], neigh[M];
int main() {
  ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    int v, u;
    cin >> v >> u;
    v--, u--;
    adj[v] += 1 << u;
    adj[u] += 1 << v;
  }
  if (2 * m == n * n - n) return cout << 0 << "\n", 0;
  for (int i = 0; i < n; i++) adj[i] += 1 << i, neigh[1 << i] = adj[i];
  for (int mask = 0; mask < (1 << n); mask++)
    for (int i = 0; i < n; i++) {
      if (!(mask & (1 << i)) && (neigh[mask] & (1 << i))) {
        neigh[mask | (1 << i)] |= (neigh[mask] | adj[i]);
      }
    }
  int ans = (1 << n) - 1;
  for (int mask = 0; mask < (1 << n); mask++) {
    if (neigh[mask] == (1 << n) - 1 &&
        __builtin_popcount(mask) < __builtin_popcount(ans)) {
      ans = mask;
    }
  }
  cout << __builtin_popcount(ans) << "\n";
  for (int i = 0; i < n; i++)
    if (ans & (1 << i)) cout << i + 1 << ' ';
  cout << "\n";
  return 0;
}
