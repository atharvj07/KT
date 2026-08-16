#include <bits/stdc++.h>
using namespace std;
const int N = 300005;
struct edge {
  int to, next;
} e[N << 1];
int h[N], xb, dfn[N], low[N], n, m, i, j, x, y, w, stx[N], sty[N], ste[N];
vector<int> ans;
bool b[N], cant[N];
inline void addedge(int x, int y) {
  e[++xb] = (edge){y, h[x]};
  h[x] = xb;
  e[++xb] = (edge){x, h[y]};
  h[y] = xb;
}
void dfs(int x, int fa) {
  dfn[x] = low[x] = ++xb;
  int i = h[x], j;
  for (; i; i = e[i].next)
    if (e[i].to != fa) {
      if (!dfn[e[i].to]) {
        stx[++w] = x, sty[w] = e[i].to;
        ste[w] = i;
        dfs(e[i].to, x);
        if (low[e[i].to] < low[x]) low[x] = low[e[i].to];
        if (low[e[i].to] >= dfn[x]) {
          int cnt = 0, ow = w;
          for (; stx[w] != x || sty[w] != e[i].to; --w) {
            if (!b[stx[w]]) ++cnt, b[stx[w]] = 1;
            if (!b[sty[w]]) ++cnt, b[sty[w]] = 1;
          }
          if (!b[stx[w]]) ++cnt, b[stx[w]] = 1;
          if (!b[sty[w]]) ++cnt, b[sty[w]] = 1;
          if (ow - w + 1 > cnt || cnt == 2) {
            for (j = w; j <= ow; ++j) cant[ste[j] >> 1] = 1;
          }
          for (j = w; j <= ow; ++j) b[stx[j]] = b[sty[j]] = 0;
          --w;
        }
      } else {
        if (dfn[e[i].to] < dfn[x]) stx[++w] = x, sty[w] = e[i].to, ste[w] = i;
        if (dfn[e[i].to] < low[x]) low[x] = dfn[e[i].to];
      }
    }
}
int main() {
  cin >> n >> m;
  xb = 1;
  for (i = 1; i <= m; ++i) {
    cin >> x >> y;
    addedge(x, y);
  }
  xb = 0;
  for (i = 1; i <= n; ++i)
    if (!dfn[i]) dfs(i, 0);
  for (i = 1; i <= m; ++i)
    if (!cant[i]) ans.push_back(i);
  cout << ans.size() << '\n';
  for (i = 0; i < int(ans.size()); ++i) cout << ans[i] << ' ';
  return 0;
}
