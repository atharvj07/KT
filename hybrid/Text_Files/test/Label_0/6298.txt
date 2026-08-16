#include <bits/stdc++.h>
using namespace std;
vector<int> months = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const int MAX = 1e5 + 55;
const int inf = 1e9 + 77;
const int MOD = 1e9 + 7;
const double PI = acos(-1.0);
const double eps = 1e-7;
int n, m, k;
vector<int> cycle;
int loop = -1;
int f = 0;
int dis[MAX];
vector<int> adj[MAX];
void dfs(int u, int depth) {
  dis[u] = depth;
  if (f) return;
  for (auto v : adj[u]) {
    if (f || loop != -1) break;
    if (!dis[v])
      dfs(v, depth + 1);
    else if (abs(dis[v] - dis[u]) >= k && loop == -1) {
      loop = v;
      break;
    }
  }
  if (loop != -1 && !f) {
    cycle.push_back(u);
    if (u == loop) f = true;
  }
}
int main() {
  scanf("%d", &n);
  scanf("%d", &m);
  scanf("%d", &k);
  memset(dis, 0, sizeof(dis));
  for (int i = 0; i < m; ++i) {
    int u, v;
    scanf("%d", &u);
    scanf("%d", &v);
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  for (int i = 1; i <= n; ++i) {
    if (loop == -1 && dis[i] == 0) {
      dfs(i, 1);
    } else if (loop != -1)
      break;
  }
  int res = cycle.size();
  printf("%d\n", res);
  for (auto i : cycle) printf("%d ", i);
  return 0;
}
