#include <bits/stdc++.h>
using namespace std;
int n, cnt;
int f[3000005];
bool tpy[3000005];
long long rk1[3000005], rk2[3000005], ans;
map<long long, int> h;
int find(int x) {
  if (f[x] != x) f[x] = find(f[x]);
  return f[x];
}
int main() {
  scanf("%d", &n);
  cnt = 0;
  for (int i = 1; i <= n; ++i) {
    long long x, y;
    scanf("%lld %lld", &x, &y);
    if (h.count(x) == 0) {
      h[x] = ++cnt;
      f[cnt] = cnt;
      rk1[cnt] = x;
    }
    if (h.count(y) == 0) {
      h[y] = ++cnt;
      f[cnt] = cnt;
      rk1[cnt] = y;
    }
    int u = find(h[x]), v = find(h[y]);
    if (u == v) {
      if (tpy[u] || tpy[v]) {
        printf("-1\n");
        return 0;
      }
      tpy[u] = true;
    }
    if (tpy[v]) tpy[u] = true;
    f[v] = u;
    if (rk1[v] > rk1[u]) {
      rk2[u] = rk1[u];
      rk1[u] = rk1[v];
    } else if (rk1[v] > rk2[u])
      rk2[u] = rk1[v];
    if (rk2[v] > rk1[u]) {
      rk2[u] = rk1[u];
      rk1[u] = rk2[v];
    } else if (rk2[v] > rk2[u])
      rk2[u] = rk2[v];
  }
  for (int i = 1; i <= cnt; ++i)
    if (f[i] == i) {
      if (tpy[i])
        ans = max(ans, rk1[i]);
      else
        ans = max(ans, rk2[i]);
    }
  printf("%lld", ans);
  return 0;
}
