#include <bits/stdc++.h>
using namespace std;
inline void read(int &tar) {
  tar = 0;
  char ch = getchar();
  while ((ch < '0' || ch > '9') && (ch < 'a' || ch > 'z')) ch = getchar();
  while (ch >= 'a' && ch <= 'z') {
    if (ch == 'u') tar = 1;
    if (ch == 'w') tar = 2;
    if (ch == 'c') tar = 3;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    tar = tar * 10 + ch - '0';
    ch = getchar();
  }
}
namespace LarjaIX {
const int N = 200011;
struct sumireko {
  int to, ne;
} e[N << 1];
int he[N], ecnt;
void addline(int f, int t) {
  e[++ecnt].to = t, e[ecnt].ne = he[f], he[f] = ecnt;
}
int n, qaq, id[N], cnt;
int tr[N << 1];
void add(int x, int v) {
  for (int i = x; i <= n + qaq; i += i & -i) tr[i] += v;
}
int query(int x) {
  int ret = 0;
  for (int i = x; i; i -= i & -i) ret += tr[i];
  return ret;
}
int fa[N], son[N][2], size[N], rev[N];
void dfs(int x) {
  for (int i = he[x], t = e[i].to; i; i = e[i].ne, t = e[i].to)
    if (t != fa[x]) {
      fa[t] = x, dfs(t);
      if (id[t] > id[x]) id[x] = id[t], son[x][1] = t, size[x] = size[t] + 1;
    }
  add(id[x], 1);
}
int isroot(int x) { return son[fa[x]][0] != x && son[fa[x]][1] != x; }
void fuckup(int x) { size[x] = 1 + size[son[x][0]] + size[son[x][1]]; }
void fuckdown(int x) {
  if (rev[x])
    swap(son[x][0], son[x][1]), rev[son[x][0]] ^= 1, rev[son[x][1]] ^= 1,
        rev[x] = 0;
  id[son[x][0]] = son[x][0] ? id[x] : 0, id[son[x][1]] = son[x][1] ? id[x] : 0;
}
void fixup(int x) {
  if (!isroot(x)) fixup(fa[x]);
  fuckdown(x);
}
void rot(int x) {
  int y = fa[x], z = fa[y];
  int xis = son[y][1] == x, yis = son[z][1] == y;
  if (!isroot(y)) son[z][yis] = x;
  fa[son[x][xis ^ 1]] = y, fa[x] = z, fa[y] = x;
  son[y][xis] = son[x][xis ^ 1], son[x][xis ^ 1] = y;
  fuckup(y), fuckup(x);
}
void splay(int x) {
  fixup(x);
  while (!isroot(x)) {
    int y = fa[x], z = fa[y];
    int xis = son[y][1] == x, yis = son[z][1] == y;
    if (!isroot(y)) rot(xis ^ yis ? x : y);
    rot(x);
  }
}
void access(int x) {
  int lst = 0;
  while (x)
    splay(x), son[x][1] = 0, fuckup(x), add(id[x], -size[x]), add(cnt, size[x]),
              son[x][1] = lst, fuckup(x), lst = x, x = fa[x];
}
void makeroot(int x) { cnt++, access(x), splay(x), rev[x] ^= 1, id[x] = cnt; }
int getans(int x) {
  splay(x);
  return query(id[x]) - size[son[x][0]];
}
int maid() {
  read(n), read(qaq), cnt = n;
  for (int i = 1; i <= n; i++) id[i] = i, size[i] = 1;
  for (int i = 1, x, y; i < n; i++)
    read(x), read(y), addline(x, y), addline(y, x);
  dfs(n);
  for (int rkk = 1, op, x, y; rkk <= qaq; rkk++) {
    read(op);
    switch (op) {
      case 1:
        read(x), makeroot(x);
        break;
      case 2:
        read(x), printf("%d\n", getans(x));
        break;
      case 3:
        read(x), read(y), printf("%d\n", getans(x) < getans(y) ? x : y);
        break;
    }
  }
  return 0;
}
}  // namespace LarjaIX
int main() { return LarjaIX::maid(); }
