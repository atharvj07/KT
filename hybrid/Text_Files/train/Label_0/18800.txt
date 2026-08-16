#include <bits/stdc++.h>
using namespace std;
struct Edge {
  int a, b, c;
  bool operator<(const Edge &r) const { return c < r.c; }
};
int N, x[3000], bl[3000];
vector<pair<int, int> > edges[3000];
Edge e[3000];
pair<int, int> dfs(int n, int p) {
  if (bl[n]) return pair<int, int>(0, 0);
  pair<int, int> ret = pair<int, int>(1, x[n]);
  for (int i = int(0); i < int(edges[n].size()); i++) {
    int next = edges[n][i].first;
    if (next == p) continue;
    pair<int, int> t = dfs(next, n);
    ret.first += t.first;
    ret.second += t.second;
  }
  return ret;
}
void block(int n) {
  if (bl[n]) return;
  bl[n] = 1;
  for (int i = int(0); i < int(edges[n].size()); i++) block(edges[n][i].first);
}
int main() {
  int a, b, c;
  while (scanf("%d", &N) != EOF) {
    for (int i = int(0); i < int(N); i++) edges[i].clear(), bl[i] = 0;
    for (int i = int(1); i < int(N); i++) {
      scanf("%d %d %d", &a, &b, &c);
      a--, b--;
      e[i] = Edge{a, b, c};
      edges[a].push_back(pair<int, int>(b, c));
      edges[b].push_back(pair<int, int>(a, c));
    }
    sort(e + 1, e + N);
    for (int i = int(0); i < int(N); i++) {
      scanf("%d", x + i);
    }
    int ac = 0, ans = 0;
    for (int i = N - 1; i; i--) {
      if (bl[e[i].a] || bl[e[i].b]) continue;
      pair<int, int> t1 = dfs(e[i].a, e[i].b);
      pair<int, int> t2 = dfs(e[i].b, e[i].a);
      if (t1.first < t2.first) swap(t1, t2), swap(e[i].b, e[i].a);
      if (t1.first > t2.second + ac) {
        ac += t2.second;
        bl[e[i].b] = 1;
        for (int j = int(0); j < int(edges[e[i].b].size()); j++) {
          int next = edges[e[i].b][j].first;
          if (next == e[i].a) continue;
          block(next);
        }
      } else {
        ans = e[i].c;
        break;
      }
    }
    printf("%d\n", ans);
  }
  return 0;
}
