#include <bits/stdc++.h>
using namespace std;
int n, m, q, p[300005], dfn[300005], low[300005], Time = 0, sta[300005],
                                                  top = 0, tag[300005];
long long sum[300005];
bool insta[300005];
struct Edge {
  int to, next;
};
struct Graph {
  Edge edge[600005];
  int first[300005], le;
  Graph() {
    le = 2;
    memset(first, 0, sizeof(first));
  }
  void in(int x, int y) {
    Edge &e = edge[le];
    e.to = y;
    e.next = first[x];
    first[x] = le++;
  }
  void insert(int x, int y) {
    in(x, y);
    in(y, x);
  }
} g, bg;
void tarjan(int x, int fa) {
  dfn[x] = ++Time;
  low[x] = Time;
  sta[++top] = x;
  insta[x] = 1;
  for (int i = g.first[x]; i; i = g.edge[i].next) {
    const Edge &e = g.edge[i];
    if (e.to == fa) continue;
    if (!dfn[e.to]) {
      tarjan(e.to, x);
      low[x] = min(low[x], low[e.to]);
    } else if (insta[e.to])
      low[x] = min(low[x], dfn[e.to]);
  }
  if (dfn[x] == low[x]) {
    int Min = 0x3f3f3f3f, Max = 0;
    while (sta[top] != x) {
      Min = min(Min, sta[top]);
      Max = max(Max, sta[top]);
      insta[sta[top]] = 0;
      top--;
    }
    Min = min(Min, x);
    Max = max(Max, x);
    top--;
    insta[x] = 0;
    if (Min != Max) tag[Max] = max(tag[Max], Min);
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin >> n >> m;
  for (int i = 1, x, y; i <= m; i++) {
    cin >> x >> y;
    g.insert(x, y);
  }
  for (int i = 1; i <= n; i++)
    if (!dfn[i]) tarjan(i, 0);
  int now = 0;
  for (int i = 1; i <= n; i++) {
    now = max(now, tag[i]);
    p[i] = now;
  }
  for (int i = 1; i <= n; i++) sum[i] = sum[i - 1] + p[i];
  cin >> q;
  while (q--) {
    int x, y;
    cin >> x >> y;
    int L = x, R = y + 1;
    while (L < R) {
      const int mid = (L + R) / 2;
      if (p[mid] >= x)
        R = mid;
      else
        L = mid + 1;
    }
    cout << -1ll * (x - 1) * (L - x) - (sum[y] - sum[L - 1]) +
                1ll * (x + y) * (y - x + 1) / 2
         << endl;
  }
  return 0;
}
