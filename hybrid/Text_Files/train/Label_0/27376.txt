#include <bits/stdc++.h>
using namespace std;
const int inf = 1e9 + 5;
const long long linf = 1e18 + 5;
const int N = 5e5 + 5;
int n, m, c, x, y, s[N], f[N], emit;
vector<int> v[N];
class segment_tree1 {
 public:
  int kd[4 * N];
  int update(int root, int bas, int son, int x, int emit) {
    if (son < x or x < bas) return kd[root];
    if (x <= bas and son <= x) return kd[root] = emit;
    return kd[root] = max(
               update((root << 1), bas, ((bas + son) >> 1), x, emit),
               update(((root << 1) | 1), ((bas + son) >> 1) + 1, son, x, emit));
  }
  int query(int root, int bas, int son, int x, int y) {
    if (son < x or y < bas) return -inf;
    if (x <= bas and son <= y) return kd[root];
    return max(query((root << 1), bas, ((bas + son) >> 1), x, y),
               query(((root << 1) | 1), ((bas + son) >> 1) + 1, son, x, y));
  }
};
class segment_tree2 {
 public:
  int kd[4 * N];
  void update(int root, int bas, int son, int x, int y, int emit) {
    if (son < x or y < bas) return;
    if (x <= bas and son <= y) {
      kd[root] = emit;
      return;
    }
    update((root << 1), bas, ((bas + son) >> 1), x, y, emit);
    update(((root << 1) | 1), ((bas + son) >> 1) + 1, son, x, y, emit);
  }
  int query(int root, int bas, int son, int x) {
    if (son < x or x < bas) return -inf;
    if (x <= bas and son <= x) return kd[root];
    return max(kd[root],
               max(query((root << 1), bas, ((bas + son) >> 1), x),
                   query(((root << 1) | 1), ((bas + son) >> 1) + 1, son, x)));
  }
};
void dfs(int root, int node) {
  s[node] = ++emit;
  for (__typeof(v[node].begin()) it = v[node].begin(); it != v[node].end();
       it++)
    if (*it != root) dfs(node, *it);
  f[node] = emit;
}
segment_tree1 tree1;
segment_tree2 tree2;
int main() {
  ios ::sync_with_stdio(0);
  cin >> n;
  for (int i = 1; i <= n - 1; i++) {
    cin >> x >> y;
    v[x].push_back(y);
    v[y].push_back(x);
  }
  dfs(-1, 1);
  cin >> m;
  emit = 0;
  for (int i = 1; i <= m; i++) {
    cin >> c >> x;
    if (c == 1)
      tree2.update(1, 1, n, s[x], f[x], ++emit);
    else if (c == 2)
      tree1.update(1, 1, n, s[x], ++emit);
    else
      cout << (tree1.query(1, 1, n, s[x], f[x]) < tree2.query(1, 1, n, s[x]))
           << '\n';
  }
  cerr << "Tooks " << (double)clock() / CLOCKS_PER_SEC << " seconds." << '\n';
  return 0;
}
