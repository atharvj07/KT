#include <bits/stdc++.h>
using namespace std;
int n, flag = 0;
int matrix[2505][2505];
int parent[2505];
vector<int> graph[2505];
int vis[2505], num[2505];
struct Edge {
  int u, v, w;
  Edge() {}
  Edge(int u, int v, int w) : u(u), v(v), w(w) {}
};
vector<Edge> edge;
bool cmp(const Edge &a, const Edge &b) { return a.w < b.w; }
void init() {
  for (int i = 1; i <= 2505; i++) parent[i] = i;
}
void input() {
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      scanf("%d", &matrix[i][j]);
      if (i == j && matrix[i][j] != 0) flag = 1;
      if (i > j && matrix[i][j] != matrix[j][i]) flag = 1;
      if (i < j) edge.push_back(Edge(i, j, matrix[i][j]));
    }
  }
}
int findfather(int x) {
  if (x == parent[x]) return x;
  return parent[x] = findfather(parent[x]);
}
void Union(int x, int y) {
  int rx = findfather(x);
  int ry = findfather(y);
  if (rx > ry) swap(rx, ry);
  if (rx != ry) parent[ry] = rx;
}
void Krukal() {
  sort(edge.begin(), edge.end(), cmp);
  int cnt = 0;
  for (int i = 0; i < edge.size(); i++) {
    int u = edge[i].u;
    int v = edge[i].v;
    int ru = findfather(u);
    int rv = findfather(v);
    if (ru != rv) {
      graph[u].push_back(v);
      graph[v].push_back(u);
      cnt++;
      Union(u, v);
    }
    if (cnt == n - 1) break;
  }
}
void dfs(int u, int fa, int tmp) {
  vis[u] = 1;
  for (int i = 0; i < graph[u].size(); i++) {
    int k = graph[u][i];
    if (vis[k]) continue;
    if (k == fa) continue;
    num[k] = max(tmp, matrix[u][k]);
    dfs(k, u, num[k]);
  }
}
int main() {
  scanf("%d", &n);
  init();
  input();
  if (flag) {
    printf("NOT MAGIC\n");
    return 0;
  }
  Krukal();
  for (int i = 1; i <= n; i++) {
    memset(vis, 0, sizeof(vis));
    dfs(i, -1, 0);
    for (int j = i + 1; j <= n; j++) {
      if (num[j] != matrix[i][j]) {
        flag = 1;
        break;
      }
    }
    if (flag) break;
  }
  if (flag)
    printf("NOT MAGIC\n");
  else
    printf("MAGIC\n");
  return 0;
}
