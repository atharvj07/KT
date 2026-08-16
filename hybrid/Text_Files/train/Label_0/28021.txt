#include <bits/stdc++.h>
using namespace std;
inline int read() {
  int x = 0;
  bool f = 0;
  char ch = getchar();
  for (; !isdigit(ch); ch = getchar()) f = (ch == '-');
  for (; isdigit(ch); ch = getchar()) x = (x << 3) + (x << 1) + (ch ^ 48);
  return f ? -x : x;
}
const int maxn = 4e5 + 7;
int n, m, c[maxn], fa[maxn];
vector<pair<int, int> > v[maxn];
int head[maxn], to[maxn * 2], nx[maxn * 2], ec = 1;
inline void add(int a, int b) {
  nx[++ec] = head[a];
  head[a] = ec;
  to[ec] = b;
}
long long ans[maxn], cur;
struct node {
  int fa, c[2], sz;
  int isz, ro;
  long long ich2;
} a[maxn];
inline bool get(int x) { return a[a[x].fa].c[1] == x; }
inline bool isrt(int x) { return a[a[x].fa].c[0] ^ x && a[a[x].fa].c[1] ^ x; }
inline void rot(int x) {
  swap(a[x].c[0], a[x].c[1]);
  a[x].ro ^= 1;
}
inline void pushup(int x) {
  a[x].sz = 1 + a[x].isz + a[a[x].c[0]].sz + a[a[x].c[1]].sz;
}
inline void pushdn(int x) {
  if (a[x].ro) rot(a[x].c[0]), rot(a[x].c[1]), a[x].ro = 0;
}
inline void rotate(int x) {
  int f = a[x].fa, ff = a[f].fa, w = get(x), ch = a[x].c[!w];
  if (!isrt(f)) a[ff].c[get(f)] = x;
  a[x].c[!w] = f;
  a[f].c[w] = ch;
  if (ch) a[ch].fa = f;
  a[f].fa = x;
  a[x].fa = ff;
  pushup(f);
}
int sta[maxn], top;
inline void splay(int x) {
  for (int y = sta[top = 1] = x; !isrt(y); sta[++top] = y = a[y].fa)
    ;
  while (top) pushdn(sta[top--]);
  for (; !isrt(x); rotate(x))
    if (!isrt(a[x].fa)) rotate(get(x) == get(a[x].fa) ? a[x].fa : x);
  pushup(x);
}
inline void access(int x) {
  for (int y = 0; x; y = x, x = a[x].fa) {
    splay(x);
    a[x].isz += a[a[x].c[1]].sz;
    a[x].ich2 += (1ll * (a[a[x].c[1]].sz) * (a[a[x].c[1]].sz));
    a[x].c[1] = y;
    a[x].isz -= a[a[x].c[1]].sz;
    a[x].ich2 -= (1ll * (a[a[x].c[1]].sz) * (a[a[x].c[1]].sz));
    pushup(x);
  }
}
inline void makeroot(int x) {
  access(x);
  splay(x);
  rot(x);
}
inline int findroot(int x) {
  access(x);
  splay(x);
  pushdn(x);
  while (a[x].c[0]) x = a[x].c[0], pushdn(x);
  splay(x);
  return x;
}
inline void link(int x) {
  int y = fa[x];
  access(x);
  splay(x);
  cur -= a[x].ich2 + (1ll * (a[a[x].c[1]].sz) * (a[a[x].c[1]].sz));
  int z = findroot(y);
  access(y);
  splay(z);
  cur -= (1ll * (a[a[z].c[1]].sz) * (a[a[z].c[1]].sz));
  splay(y);
  a[x].fa = y;
  a[y].isz += a[x].sz;
  a[y].ich2 += (1ll * (a[x].sz) * (a[x].sz));
  pushup(y);
  access(x);
  splay(z);
  cur += (1ll * (a[a[z].c[1]].sz) * (a[a[z].c[1]].sz));
}
inline void cut(int x) {
  int y = fa[x];
  access(x);
  cur += a[x].ich2;
  int z = findroot(x);
  access(x);
  splay(z);
  cur -= (1ll * (a[a[z].c[1]].sz) * (a[a[z].c[1]].sz));
  splay(x);
  a[a[x].c[0]].fa = 0;
  a[x].c[0] = 0;
  pushup(x);
  access(y);
  splay(z);
  cur += (1ll * (a[a[z].c[1]].sz) * (a[a[z].c[1]].sz));
}
void dfs(int x, int ff) {
  fa[x] = ff;
  for (int i = head[x]; i; i = nx[i]) {
    int ver = to[i];
    if (ver == ff) continue;
    dfs(ver, x);
  }
  a[x].fa = ff;
  a[ff].isz += a[x].sz;
  a[ff].ich2 += (1ll * (a[x].sz) * (a[x].sz));
  pushup(ff);
}
int main() {
  n = read();
  m = read();
  for (int i = 1; i <= n; ++i) v[c[i] = read()].push_back(make_pair(0, i));
  for (int i = 1; i < n; ++i) {
    int u = read(), v = read();
    add(u, v);
    add(v, u);
  }
  for (int i = 1; i <= n + 1; ++i) a[i].sz = 1;
  dfs(1, n + 1);
  for (int i = 1; i <= m; ++i) {
    int x = read(), y = read();
    if (c[x] == y) continue;
    v[c[x]].push_back(make_pair(i, -x));
    v[c[x] = y].push_back(make_pair(i, x));
  }
  cur = (1ll * (n) * (n));
  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j < v[i].size(); ++j) {
      int x = v[i][j].second;
      if (x > 0)
        cut(x);
      else
        link(-x);
      ans[v[i][j].first] += (1ll * (n) * (n)) - cur;
      ans[j + 1 == v[i].size() ? m + 1 : v[i][j + 1].first] -=
          (1ll * (n) * (n)) - cur;
    }
    for (int j = (int)v[i].size() - 1; ~j; --j) {
      int x = v[i][j].second;
      if (x > 0)
        link(x);
      else
        cut(-x);
    }
  }
  for (int i = 1; i <= m; ++i) ans[i] += ans[i - 1];
  for (int i = 0; i <= m; ++i) printf("%lld\n", ans[i]);
  return 0;
}
