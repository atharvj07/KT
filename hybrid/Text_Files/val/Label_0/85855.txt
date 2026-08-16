#include <bits/stdc++.h>
using namespace std;
const int maxn = 2000 + 10;
const int maxE = 2000000 + 10;
const int DEBUG = 0;
int n, m;
bitset<maxn> val[maxn];
char S[maxn];
struct anode {
  int u, v, w;
  anode() {}
  anode(int _u, int _v, int _w) : u(_u), v(_v), w(_w) {}
} a[maxE];
int h[maxn], ecnt, sfa[maxn];
struct enode {
  int v, n;
  enode() {}
  enode(int _v, int _n) : v(_v), n(_n) {}
} e[maxE << 1];
inline void addedge(int u, int v) {
  ecnt++;
  e[ecnt] = enode(v, h[u]);
  h[u] = ecnt;
}
int findfa(int u) { return (sfa[u] == u) ? (u) : (sfa[u] = findfa(sfa[u])); }
inline bool cmp(anode a, anode b) { return a.w > b.w; }
int flag, vis[maxn][maxn], all;
void dfs(int u, int fa, int k) {
  if (vis[k][u]) all++;
  vis[k][u] = 0;
  for (int i = h[u]; ~i; i = e[i].n) {
    int v = e[i].v;
    if (v == fa) continue;
    if (!vis[k][v]) continue;
    dfs(v, u, k);
  }
}
void dfs_ans(int u, int fa) {
  for (int i = h[u]; ~i; i = e[i].n) {
    int v = e[i].v;
    if (v == fa) continue;
    printf("%d %d\n", u, v);
    dfs_ans(v, u);
  }
}
inline void solve() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) val[i].reset();
  for (int i = 1; i <= m; i++) {
    scanf("%s", S + 1);
    int cnt = 0;
    for (int j = 1; j <= n; j++)
      if (S[j] == '1') cnt++;
    for (int j = 1; j <= n; j++) vis[i][j] = 0;
    if (cnt <= 1) continue;
    for (int j = 1; j <= n; j++)
      if (S[j] == '1') {
        val[j][i] = 1;
        vis[i][j] = 1;
      }
  }
  int tot = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {
      int w = (val[i] & val[j]).count();
      a[++tot] = anode(i, j, w);
    }
  }
  sort(a + 1, a + tot + 1, cmp);
  for (int i = 1; i <= n; i++) sfa[i] = i, h[i] = -1;
  ecnt = 0;
  for (int i = 1; i <= tot; i++) {
    int u = a[i].u, v = a[i].v;
    int f1 = findfa(u), f2 = findfa(v);
    if (f1 == f2) continue;
    if (DEBUG) printf("%d %d %d\n", u, v, a[i].w);
    addedge(u, v);
    addedge(v, u);
    sfa[f1] = f2;
  }
  flag = 1;
  for (int i = 1; i <= m; i++) {
    all = 0;
    int now = 0;
    for (int j = 1; j <= n; j++)
      if (vis[i][j]) now++;
    for (int j = 1; j <= n; j++)
      if (vis[i][j]) {
        dfs(j, 0, i);
        break;
      }
    if (now != all) flag = 0;
  }
  if (flag) {
    puts("YES");
    dfs_ans(1, 0);
    return;
  }
  puts("NO");
}
int main() {
  int cas;
  scanf("%d", &cas);
  while (cas--) {
    solve();
  }
  return 0;
}
