#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:1024000000,1024000000")
using namespace std;
const int mxn = 400005, maxnn = 100005;
const int mod = 1e9 + 7;
long long ans;
int n, m, num, cir, r, cnt;
int head[maxnn], que[maxnn];
struct edge {
  int to, next;
  long long w;
} f[mxn << 2];
long long p[70], circle[mxn], dis[maxnn], dig[2], pw[105];
inline void add(int u, int v, long long w) {
  f[++cnt].to = v, f[cnt].w = w, f[cnt].next = head[u], head[u] = cnt;
}
inline void dfs(int u, int fa, long long now) {
  dis[u] = now, que[++num] = u;
  for (int i = head[u]; i; i = f[i].next) {
    int v = f[i].to;
    if (v == fa) continue;
    if (dis[v] == -1)
      dfs(v, u, dis[u] ^ f[i].w);
    else
      circle[++cir] = dis[u] ^ dis[v] ^ f[i].w;
  }
}
inline void init() {
  int i, j;
  r = 0;
  memset(p, 0, sizeof p);
  for (i = 1; i <= cir; i++) {
    long long x = circle[i];
    for (j = 62; j >= 0; j--) {
      if (!(x >> j)) continue;
      if (!p[j]) {
        p[j] = x;
        break;
      }
      x ^= p[j];
    }
  }
  for (j = 0; j <= 62; j++)
    if (p[j]) r++;
}
inline void calc() {
  init();
  int i, j;
  for (j = 0; j <= 62; j++) {
    bool flag = 0;
    dig[0] = dig[1] = 0;
    for (i = 1; i <= num; i++) dig[(dis[que[i]] >> j) & 1]++;
    for (i = 0; i <= 62; i++)
      if ((p[i] >> j) & 1) {
        flag = 1;
        break;
      }
    long long now =
        (dig[0] * (dig[0] - 1) / 2 + dig[1] * (dig[1] - 1) / 2) % mod;
    if (flag) {
      if (r) now = now * pw[r - 1] % mod;
      now = now * pw[j] % mod;
      ans = (ans + now) % mod;
    }
    now = dig[0] * dig[1] % mod;
    if (flag) {
      if (r) now = now * pw[r - 1] % mod;
    } else
      now = now * pw[r] % mod;
    now = now * pw[j] % mod;
    ans = (ans + now) % mod;
  }
}
int main() {
  int i, j, u, v;
  long long w;
  memset(dis, -1, sizeof dis);
  pw[0] = 1;
  for (j = 1; j <= 100; j++) pw[j] = pw[j - 1] * 2 % mod;
  scanf("%d%d", &n, &m);
  for (i = 1; i <= m; i++) {
    scanf("%d%d%lld", &u, &v, &w);
    add(u, v, w), add(v, u, w);
  }
  for (i = 1; i <= n; i++)
    if (dis[i] == -1) {
      num = cir = 0;
      dfs(i, 0, 0);
      calc();
    }
  printf("%lld", ans);
  return 0;
}
