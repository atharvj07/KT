#include <bits/stdc++.h>
using namespace std;
struct edge {
  int u, v, w;
};
bool comp(edge a, edge b) { return a.w < b.w; }
int len[300010], tmp[300010];
edge ed[300010];
int main() {
  ios_base::sync_with_stdio(false);
  int n, m, x, y, z, l, j;
  cin >> n >> m;
  for (int i = 0; i < m; ++i) {
    cin >> x >> y >> z;
    ed[i].u = x, ed[i].v = y, ed[i].w = z;
  }
  sort(ed, ed + m, comp);
  int ans = 0;
  for (int i = 0; i < m; ++i) {
    j = i;
    while (j < m - 1 && ed[j].w == ed[j + 1].w) j++;
    for (int k = i; k <= j; ++k) {
      x = ed[k].u, y = ed[k].v;
      tmp[y] = max(tmp[y], len[x] + 1);
    }
    for (int k = i; k <= j; ++k) {
      y = ed[k].v;
      len[y] = max(len[y], tmp[y]);
      ans = max(len[y], ans);
    }
    i = j;
  }
  cout << ans;
  return 0;
}
