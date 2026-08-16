#include <bits/stdc++.h>
using namespace std;
const int MAXN = 210, INF = 1e9;
int n, k, w[MAXN], f[MAXN][MAXN], tmp[MAXN], u, v, ans;
vector<int> e[MAXN];
void Merge(int* a, int* b) {
  for (long long j = (n); j >= (1); j--) {
    b[j] = b[j - 1];
  }
  b[0] = 0;
  for (long long j = (0); j <= (n); j++) {
    tmp[j] = a[j];
  }
  for (long long j = (0); j <= (n); j++) {
    a[j] = (a[j] > b[j] ? a[j] : b[j]);
  }
  for (long long j = (0); j <= (n); j++) {
    for (long long x = ((0 > k - j + 1 ? 0 : k - j + 1)); x <= (n); x++) {
      a[(j < x ? j : x)] =
          (a[(j < x ? j : x)] > tmp[j] + b[x] ? a[(j < x ? j : x)]
                                              : tmp[j] + b[x]);
    }
  }
}
void dp(int u, int fa) {
  f[u][0] = w[u];
  for (vector<int>::iterator it = e[u].begin(); it != e[u].end(); it++) {
    int v = *it;
    if (v == fa) continue;
    dp(v, u);
    Merge(f[u], f[v]);
  }
}
int main() {
  cin >> n >> k;
  for (long long i = (1); i <= (n); i++) cin >> w[i];
  for (long long i = (1); i <= (n - 1); i++) {
    cin >> u >> v;
    e[u].push_back(v);
    e[v].push_back(u);
  }
  dp(1, 0);
  for (long long i = (0); i <= (n); i++) ans = (ans > f[1][i] ? ans : f[1][i]);
  cout << ans << endl;
  return 0;
}
