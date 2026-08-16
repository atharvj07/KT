#include <bits/stdc++.h>
using namespace std;
int first[100005], vv[200005], nxt[200005], e, w[100005];
int sz[100005];
long long sum[100005], cnt[100005];
long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
void add(int u, int v) {
  vv[e] = v;
  nxt[e] = first[u];
  first[u] = e++;
}
void dfs(int u, int p) {
  for (int i = first[u]; i != -1; i = nxt[i]) {
    int v = vv[i];
    if (v == p) continue;
    dfs(v, u);
    sz[u]++;
    sum[u] += sum[v];
  }
  sum[u] += w[u];
}
void solve(int u, int p) {
  long long k = 1LL << 60;
  cnt[u] = 1;
  for (int i = first[u]; i != -1; i = nxt[i]) {
    int v = vv[i];
    if (v == p) continue;
    solve(v, u);
    k = min(k, sum[v]);
    long long g = gcd(cnt[u], cnt[v]);
    if (cnt[u] / g > k / cnt[v] + 1LL) {
      sum[u] = 0;
      return;
    }
    cnt[u] = cnt[u] / gcd(cnt[u], cnt[v]) * cnt[v];
    if (cnt[u] > k) {
      sum[u] = 0;
      return;
    }
  }
  if (cnt[u] > k)
    sum[u] = 0;
  else if (k != (1LL << 60)) {
    k = k - k % cnt[u];
    sum[u] = k * sz[u];
    cnt[u] = cnt[u] * sz[u];
  } else
    sum[u] = w[u];
}
int main() {
  int n, u, v;
  memset(first, -1, sizeof(first));
  cin >> n;
  for (int i = 1; i <= n; ++i) scanf("%d", w + i);
  for (int i = 1; i < n; ++i) {
    scanf("%d%d", &u, &v);
    add(u, v);
    add(v, u);
  }
  dfs(1, -1);
  long long ans = sum[1];
  solve(1, -1);
  ans -= sum[1];
  cout << ans << endl;
  return 0;
}
