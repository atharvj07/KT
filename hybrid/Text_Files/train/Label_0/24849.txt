#include <bits/stdc++.h>
using namespace std;
const int N = 100010;
const long long inf = 1ll << 60;
int n, tot;
int to[N << 1], nex[N << 1], head[N];
long long ans = 0, p[N], sum[N];
bool flag;
void SE(int u, int v) {
  to[++tot] = v;
  nex[tot] = head[u];
  head[u] = tot;
  return;
}
long long _GCD(long long x, long long y) {
  long long r = x % y;
  while (r) x = y, y = r, r = x % y;
  return y;
}
void DFS(int x, int fa) {
  long long mi = inf, cnt = 0;
  for (int i = head[x]; i; i = nex[i]) {
    if (to[i] == fa) continue;
    DFS(to[i], x);
    if (flag) return;
    if (p[to[i]] < mi) mi = p[to[i]];
    cnt++;
  }
  if (cnt == 0) {
    sum[x] = 1;
    return;
  }
  long long lcm = 1ll;
  for (int i = head[x]; i; i = nex[i]) {
    if (to[i] == fa) continue;
    if ((double)lcm / _GCD(lcm, sum[to[i]]) * sum[to[i]] > (double)mi) {
      flag = 1;
      return;
    }
    lcm = lcm / _GCD(lcm, sum[to[i]]) * sum[to[i]];
  }
  p[x] = mi / lcm * lcm * cnt;
  sum[x] = lcm * cnt;
  return;
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%I64d", &p[i]);
    ans += p[i];
  }
  for (int u, v, i = 1; i < n; i++) {
    scanf("%d%d", &u, &v);
    SE(u, v), SE(v, u);
  }
  DFS(1, 0);
  if (!flag) ans -= p[1];
  printf("%I64d\n", ans);
  return 0;
}
