#include <bits/stdc++.h>
using namespace std;
struct Edge {
  int a, b;
} edges[101];
vector<int> adj[101];
int n, m, a, b;
bool res = true;
short int mark[101] = {0};
void DFS(int node) {
  int size = adj[node].size();
  if (mark[node] == 0) mark[node] = 1;
  for (__typeof(size) i = 0; i < size; i++) {
    if (!res) return;
    if (mark[adj[node][i]] == mark[node]) {
      res = false;
      return;
    } else if (mark[adj[node][i]] == 0) {
      mark[adj[node][i]] = mark[node] == 1 ? 2 : 1;
      DFS(adj[node][i]);
    }
  }
}
bool intersect(const int &i, const int &j) {
  if (edges[i].a >= edges[j].a && edges[i].b <= edges[j].b) {
    return false;
  }
  if (edges[j].a >= edges[i].a && edges[j].b <= edges[i].b) {
    return false;
  }
  if ((edges[i].a > edges[j].a && edges[i].a < edges[j].b) ||
      (edges[i].b > edges[j].a && edges[i].b < edges[j].b))
    return true;
  return false;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin >> n >> m;
  for (__typeof(m) i = 0; i < m; i++) {
    cin >> a >> b;
    edges[i].a = min(a, b), edges[i].b = max(a, b);
    for (__typeof(i) j = 0; j < i; j++) {
      if (intersect(i, j)) {
        adj[i].push_back(j), adj[j].push_back(i);
      }
    }
  }
  for (__typeof(m) i = 0; i < m; i++) {
    if (mark[i] == 0) {
      DFS(i);
    }
    if (!res) {
      return cout << "Impossible\n", 0;
    }
  }
  for (__typeof(m) i = 0; i < m; i++) {
    if (mark[i] == 1)
      cout << 'i';
    else
      cout << 'o';
  }
  cout << '\n';
  return 0;
}
