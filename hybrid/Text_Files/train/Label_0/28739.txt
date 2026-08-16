#include <bits/stdc++.h>
using namespace std;
template <typename T>
inline bool upmin(T &x, T y) {
  return y < x ? x = y, 1 : 0;
}
template <typename T>
inline bool upmax(T &x, T y) {
  return x < y ? x = y, 1 : 0;
}
const long double eps = 1e-9;
const long double pi = acos(-1);
const int oo = 1 << 30;
const long long loo = 1ll << 62;
const int mods = 998244353;
const int MAXN = 400005;
const int INF = 0x3f3f3f3f;
namespace FastIO {
constexpr int SIZE = (1 << 21) + 1;
int num = 0, f;
char ibuf[SIZE], obuf[SIZE], que[65], *iS, *iT, *oS = obuf,
                                                *oT = obuf + SIZE - 1, c;
inline void flush() {
  fwrite(obuf, 1, oS - obuf, stdout);
  oS = obuf;
}
inline void putc(char c) {
  *oS++ = c;
  if (oS == oT) flush();
}
template <class I>
inline void read(I &x) {
  for (f = 1, c = (iS == iT ? (iT = ((iS = ibuf) + fread(ibuf, 1, SIZE, stdin)),
                              (iS == iT ? EOF : *iS++))
                            : *iS++);
       c < '0' || c > '9';
       c = (iS == iT ? (iT = ((iS = ibuf) + fread(ibuf, 1, SIZE, stdin)),
                       (iS == iT ? EOF : *iS++))
                     : *iS++))
    if (c == '-') f = -1;
  for (x = 0; c >= '0' && c <= '9';
       c = (iS == iT ? (iT = ((iS = ibuf) + fread(ibuf, 1, SIZE, stdin)),
                       (iS == iT ? EOF : *iS++))
                     : *iS++))
    x = (x << 3) + (x << 1) + (c & 15);
  x *= f;
}
template <class I>
inline void print(I x) {
  if (x < 0) putc('-'), x = -x;
  if (!x) putc('0');
  while (x) que[++num] = x % 10 + 48, x /= 10;
  while (num) putc(que[num--]);
}
struct Flusher_ {
  ~Flusher_() { flush(); }
} io_Flusher_;
}  // namespace FastIO
using FastIO ::print;
using FastIO ::putc;
using FastIO ::read;
vector<int> cir, e[MAXN];
int vis[MAXN], fa[MAXN], rt[MAXN], sz[MAXN], flag[MAXN], g[MAXN], f[MAXN],
    tmp[MAXN], s[MAXN], h[MAXN][2], c[MAXN], sum, mx, n;
int upd(int x, int y) { return x + y >= mods ? x + y - mods : x + y; }
void dfs(int x, int father) {
  vis[x] = 1, fa[x] = father;
  for (auto v : e[x]) {
    if (v == father) continue;
    if (vis[v]) {
      if (cir.size()) continue;
      int nw = x;
      while (nw != fa[v]) cir.push_back(nw), flag[nw] = 1, nw = fa[nw];
    } else
      dfs(v, x);
  }
}
void tree_dp(int x, int father) {
  rt[x] = rt[father], sz[x] = 1;
  for (auto v : e[x]) {
    if (v == father) continue;
    tree_dp(v, x);
    sz[x] += sz[v];
    g[x] += g[v];
  }
  g[x] += sz[x];
}
void Tree_dp(int x, int father, int all) {
  upmax(mx, all);
  for (auto v : e[x]) {
    if (v == father) continue;
    Tree_dp(v, x, all + n - sz[v] - sz[v]);
  }
}
signed main() {
  read(n);
  for (int i = 1, u, v; i <= n; ++i)
    read(u), read(v), ++u, ++v, e[u].push_back(v), e[v].push_back(u);
  dfs(1, 0);
  for (auto u : cir) {
    rt[u] = u, sz[u] = 1, sum = 0;
    for (auto v : e[u])
      if (!flag[v]) tree_dp(v, u), sz[u] += sz[v], sum += g[v];
    mx = 0;
    for (auto v : e[u])
      if (!flag[v]) Tree_dp(v, u, n - sz[v] - sz[v]);
    h[u][0] = sum, h[u][1] = mx;
  }
  int len = (int)cir.size();
  for (int i = 1; i <= len; ++i) f[i] = n + h[cir[i - 1]][0] + h[cir[i - 1]][1];
  for (int i = 1; i <= len + len; ++i)
    s[i] = s[i - 1] + sz[cir[(i - 1) % len]], c[i] = h[cir[(i - 1) % len]][0];
  for (int i = 1; i < len; ++i) {
    for (int j = 1; j <= len; ++j) tmp[j] = f[j], f[j] = 0;
    for (int j = 1; j <= len; ++j)
      upmax(f[j], tmp[j] + n - (s[j + i - 1] - s[j - 1]) + c[j + i]),
          upmax(
              f[j == 1 ? len : j - 1],
              tmp[j] + n - (s[j + i - 1] - s[j - 1]) + c[j == 1 ? len : j - 1]);
  }
  int ans = 0;
  for (int i = 1; i <= len; ++i) upmax(ans, f[i]);
  print(ans);
  return 0;
}
