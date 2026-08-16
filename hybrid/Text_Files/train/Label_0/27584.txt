#include <bits/stdc++.h>
using namespace std;
const int N = 500007;
int n, m;
int fa[N];
struct node {
  int u, v, w;
  bool operator<(const node &t) const { return w < t.w; }
} G[N];
int Find(int x) { return x == fa[x] ? x : fa[x] = Find(fa[x]); }
void Merge(int x, int y) {
  x = Find(x), y = Find(y);
  if (x != y) fa[x] = y;
}
int main() {
  while (~scanf("%d%d", &n, &m)) {
    for (int i = 1; i <= n; ++i) fa[i] = i;
    for (int i = 1; i <= m; ++i) {
      scanf("%d%d%d", &G[i].u, &G[i].v, &G[i].w);
    }
    sort(G + 1, G + m + 1);
    int ans = 0;
    for (int i = 0; i < m;) {
      int num = 0;
      int j = i;
      while (G[i].w == G[j].w) j++;
      for (int k = i; k < j; k++) {
        int fx = Find(G[k].u), fy = Find(G[k].v);
        if (fx != fy) num++;
      }
      for (int k = i; k < j; k++) {
        int fx = Find(G[k].u), fy = Find(G[k].v);
        if (fx != fy) Merge(fx, fy), num--;
      }
      i = j;
      ans += num;
    }
    printf("%d\n", ans);
  }
  return 0;
}
