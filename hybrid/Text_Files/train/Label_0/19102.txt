#include <bits/stdc++.h>
using namespace std;
bool vis[2009];
int d[2009];
char s[2009][2009];
struct Edge {
  int v, next;
} edge[3000009];
int tot, n;
int head[2009];
inline void addedge(int u, int v) {
  edge[tot].v = v;
  edge[tot].next = head[u];
  head[u] = tot++;
}
void bfs(int s) {
  queue<int> q;
  vis[s] = 1;
  d[s] = 0;
  q.push(s);
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (int e = head[u]; e != -1; e = edge[e].next) {
      int v = edge[e].v;
      if (!vis[v]) {
        d[v] = d[u] + 1;
        vis[v] = 1;
        q.push(v);
      }
    }
  }
}
int main() {
  int N, M;
  memset(head, -1, sizeof(head));
  scanf("%d%d", &N, &M);
  n = N + M;
  for (int i = 0; i < N; i++) scanf("%s", s[i]);
  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++)
      if (s[i][j] == '#') {
        addedge(i, N + j);
        addedge(N + j, i);
      }
  bfs(N - 1);
  if (vis[0])
    printf("%d", d[0]);
  else
    printf("-1");
  return 0;
}
