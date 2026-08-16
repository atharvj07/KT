#include <bits/stdc++.h>
using namespace std;
inline long long read() {
  char ch = getchar();
  long long res = 0, pd = 1;
  while (ch < '0' || ch > '9') {
    if (ch == '-') pd = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    res = (res << 1) + (res << 3) + ch - '0';
    ch = getchar();
  }
  return res * pd;
}
inline void write(long long x) {
  if (x < 0) putchar('-');
  if (x >= 10) write(x / 10);
  putchar(x % 10 | '0');
}
inline void wlk(long long x) {
  write(x);
  putchar(32);
}
inline void wln(long long x) {
  write(x);
  putchar(10);
}
const long long maxn = 200003;
long long edge[maxn << 1], nxt[maxn << 1], son[maxn];
long long val[maxn << 1], head[maxn], cnt, ans1, ans2, n;
inline void add(long long u, long long v, long long w) {
  edge[++cnt] = v;
  nxt[cnt] = head[u];
  head[u] = cnt;
  val[cnt] = w;
}
inline void dfs(long long now, long long fa) {
  son[now] = 1;
  for (long long i = head[now]; i; i = nxt[i])
    if (edge[i] != fa) {
      dfs(edge[i], now);
      son[now] += son[edge[i]];
      if (son[edge[i]] & 1) ans1 += val[i];
    }
}
inline void Dfs(long long now, long long fa) {
  for (long long i = head[now]; i; i = nxt[i])
    if (edge[i] != fa) {
      Dfs(edge[i], now);
      ans2 += min(son[edge[i]], n - son[edge[i]]) * val[i];
    }
}
signed main() {
  long long T = read();
  while (T--) {
    cnt = ans1 = ans2 = 0, n = read() * 2;
    for (long long i = 1; i < n; ++i) {
      long long x = read(), y = read(), z = read();
      add(x, y, z);
      add(y, x, z);
    }
    dfs(1, 0);
    wlk(ans1);
    Dfs(1, 0);
    wln(ans2);
    for (long long i = 1; i <= n; ++i) head[i] = son[i] = 0;
  }
  return 0;
}
