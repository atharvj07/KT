#include <bits/stdc++.h>
using namespace std;
int n, cnt = 0;
struct node {
  int to, nxt;
} e[400010];
long long siz[200010], dep[200010];
long long ans = 0, ji = 0;
int head[200010];
void add(int u, int v) {
  e[++cnt].to = v;
  e[cnt].nxt = head[u];
  head[u] = cnt;
  e[++cnt].to = u;
  e[cnt].nxt = head[v];
  head[v] = cnt;
}
void dfs(int x, int fa) {
  siz[x] = 1LL;
  int i;
  for (i = head[x]; i; i = e[i].nxt) {
    if (e[i].to == fa) continue;
    dep[e[i].to] = dep[x] + 1;
    dfs(e[i].to, x);
    siz[x] += siz[e[i].to];
  }
}
int main() {
  scanf("%d", &n);
  int i, j, x, y;
  for (i = 1; i < n; ++i) {
    scanf("%d%d", &x, &y);
    add(x, y);
  }
  dep[1] = 0;
  dfs(1, 0);
  for (i = 1; i <= n; ++i) {
    ans += siz[i] * (long long)(n - siz[i]);
    if (dep[i] % 2 == 1) ji++;
  }
  ans += ji * (long long)(n - ji);
  ans /= 2;
  printf("%I64d\n", ans);
  return 0;
}
