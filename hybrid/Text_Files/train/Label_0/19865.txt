#include <bits/stdc++.h>
const long long mod = 1e9 + 7, N = 1e5 + 5;
long long n, m, head[N], S, sta[N], tp, nxt[N << 2], dot[N << 2], cnt;
long long val[N << 2], d[65], s[N], ans;
bool vis[N];
long long read() {
  long long x = 0, f = 1;
  char s;
  while ((s = getchar()) < '0' || s > '9')
    if (s == '-') f = -1;
  while (s >= '0' && s <= '9') {
    x = (x << 1) + (x << 3) + (s ^ 48);
    s = getchar();
  }
  return x * f;
}
void addEdge(const long long u, const long long v, const long long w) {
  dot[++cnt] = v, nxt[cnt] = head[u], val[cnt] = w, head[u] = cnt;
}
void ins(long long x) {
  for (long long i = 59; ~i; --i)
    if (x >> i & 1)
      if (!d[i]) {
        d[i] = x;
        ++S;
        return;
      } else
        x ^= d[i];
}
void dfs(const long long u, const long long Val) {
  vis[u] = 1;
  s[u] = Val;
  sta[++tp] = u;
  for (long long i = head[u]; i; i = nxt[i]) {
    long long v = dot[i];
    if (vis[v])
      ins(s[v] ^ Val ^ val[i]);
    else
      dfs(v, val[i] ^ s[u]);
  }
}
signed main() {
  long long u, v, num;
  long long w;
  bool ok;
  n = read(), m = read();
  for (long long i = 1; i <= m; ++i) {
    u = read(), v = read(), w = read();
    addEdge(u, v, w), addEdge(v, u, w);
  }
  for (long long i = 1; i <= n; ++i)
    if (!vis[i]) {
      memset(d, 0, sizeof d);
      S = tp = 0;
      dfs(i, 0);
      for (long long j = 0; j < 60; ++j) {
        w = (1ll << j) % mod;
        ok = 0;
        for (long long k = 0; k < 60; ++k)
          if (d[k] >> j & 1) {
            ok = 1;
            break;
          }
        if (ok)
          ans = (ans +
                 tp * (tp - 1) / 2 % mod * ((1ll << S - 1) % mod) % mod * w) %
                mod;
        else {
          long long x = 0;
          for (long long k = 1; k <= tp; ++k)
            if (s[sta[k]] >> j & 1) ++x;
          ans = (ans + x * (tp - x) % mod * ((1ll << S) % mod) % mod * w) % mod;
        }
      }
    }
  printf("%lld\n", ans);
  return 0;
}
