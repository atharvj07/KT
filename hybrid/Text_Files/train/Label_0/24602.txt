#include <bits/stdc++.h>
using namespace std;
const int MAXN = 301010;
const int MAXM = 1010101;
vector<int> g[MAXN];
int n, m;
bool vis[MAXN];
vector<int> ans;
int tow;
int fa[MAXN], cnt[MAXN];
int getfa(int x) { return fa[x] == x ? x : fa[x] = getfa(fa[x]); }
int sz[MAXN];
int sze[MAXN];
void link(int u, int v) {
  u = getfa(u);
  v = getfa(v);
  sze[u]++;
  if (u == v) return;
  sz[u] += sz[v];
  sze[u] += sze[v];
  fa[v] = u;
}
bool lk1[MAXN];
int in[MAXN];
int eu[MAXM], ev[MAXM];
vector<int> p1;
queue<int> q;
int pre[MAXN];
vector<int> strai;
int dis[MAXN];
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i) fa[i] = i;
  int u, v;
  for (int i = 1; i <= m; ++i) {
    scanf("%d%d", &u, &v);
    g[u].push_back(v);
    g[v].push_back(u);
    link(u, v);
    eu[i] = u;
    ev[i] = v;
    if (u == 1) lk1[v] = 1;
    if (v == 1) lk1[u] = 1;
  }
  bool flag1 = 0;
  q.push(1);
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (auto v : g[u]) {
      if (!dis[v]) {
        dis[v] = dis[u] + 1;
        pre[v] = u;
        q.push(v);
      }
    }
  }
  if (getfa(n) == getfa(1)) {
    int tmp = n;
    while (tmp != 1) {
      strai.push_back(tmp);
      tmp = pre[tmp];
    }
    strai.push_back(1);
    if (strai.size() <= 5) {
      printf("%d\n", (int)strai.size() - 1);
      for (int i = strai.size() - 1; i >= 0; --i) {
        printf("%d ", strai[i]);
      }
      puts("");
      return 0;
    }
  }
  {
    for (int i = 2; i <= n; ++i) {
      if (dis[i] == 2) {
        printf("4\n1 %d %d 1 %d", pre[i], i, n);
        return 0;
      }
    }
    for (int i = 1; i <= n; ++i) fa[i] = i, sz[i] = 1, sze[i] = 0, dis[i] = 0;
    for (int i = 1; i <= m; ++i) {
      if (eu[i] != 1 && ev[i] != 1) {
        link(eu[i], ev[i]);
      }
    }
    for (auto v : g[1]) {
      int tv = getfa(v);
      if (sze[tv] != 1ll * sz[tv] * (sz[tv] - 1) / 2) {
        for (int i = 1; i <= n; ++i) {
          if (getfa(i) == tv) {
            p1.push_back(i);
          }
        }
        int cntt = 0;
        for (auto u : p1) {
          ++cntt;
          cnt[u]++;
          for (auto uu : g[u]) {
            cnt[uu]++;
          }
          for (auto uu : p1) {
            if (cntt != cnt[uu]) {
              int key1 = u;
              int key2 = -1, key3;
              dis[u] = 1;
              q.push(u);
              while (!q.empty()) {
                int tt = q.front();
                q.pop();
                for (auto to : g[tt]) {
                  if (to == 1) continue;
                  if (!dis[to]) {
                    dis[to] = dis[tt] + 1;
                    if (tt != u) {
                      key2 = to;
                      key3 = tt;
                      printf("5\n1 %d %d %d %d %d", key1, key3, key2, key1, n);
                      return 0;
                    }
                    q.push(to);
                  }
                }
              }
              assert(0);
            }
          }
        }
      }
    }
  }
  if (getfa(n) != getfa(1))
    puts("-1");
  else {
    printf("%d\n", (int)strai.size() - 1);
    for (int i = strai.size() - 1; i >= 0; --i) {
      printf("%d ", strai[i]);
    }
    puts("");
    return 0;
  }
  return 0;
}
