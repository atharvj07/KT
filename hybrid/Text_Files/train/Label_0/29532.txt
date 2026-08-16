#include <bits/stdc++.h>
using namespace std;
const int N = 5e3 + 5;
vector<int> G[N];
struct node {
  int id, num, cost;
} a[N], b[N], c[N];
struct nod {
  int num, cost;
};
vector<nod> op[N];
int dis[N], sum, w;
bool can[N], vis[N];
int n, m, Q, p;
void bfs(int s) {
  memset(dis, 63, sizeof dis);
  memset(vis, 0, sizeof vis);
  vis[s] = 1;
  dis[s] = 0;
  queue<int> q;
  q.push(s);
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (int v : G[u]) {
      if (!vis[v]) {
        vis[v] = 1;
        dis[v] = dis[u] + 1;
        q.push(v);
      }
    }
  }
}
bool cmp(node a, node b) { return a.cost < b.cost; }
bool judge(int mid, int cnt, int w, int sumc) {
  int nums = 0, costs = 0;
  for (int i = 1; i <= cnt; i++) {
    if (dis[b[i].id] <= mid) {
      int res = w / b[i].cost;
      res = min(res, b[i].num);
      nums += res;
      w = w - res * b[i].cost;
    }
  }
  return nums >= sum;
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1, u, v; i <= m; i++) {
    scanf("%d%d", &u, &v);
    G[u].push_back(v);
    G[v].push_back(u);
  }
  scanf("%d", &p);
  for (int i = 1; i <= p; i++) {
    scanf("%d%d%d", &a[i].id, &a[i].num, &a[i].cost);
    op[a[i].id].push_back({a[i].num, a[i].cost});
  }
  scanf("%d", &Q);
  while (Q--) {
    int p;
    scanf("%d%d%d", &p, &sum, &w);
    bfs(p);
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
      if (dis[i] > 1e9) continue;
      for (auto it : op[i]) {
        b[++cnt].id = i;
        b[cnt].num = it.num;
        b[cnt].cost = it.cost;
      }
    }
    sort(b + 1, b + cnt + 1, cmp);
    int l = 0, r = n, ans = -1;
    while (l <= r) {
      int mid = (l + r) / 2;
      if (judge(mid, cnt, w, sum))
        ans = mid, r = mid - 1;
      else
        l = mid + 1;
    }
    printf("%d\n", ans);
  }
}
