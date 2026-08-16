#include <bits/stdc++.h>
using namespace std;
const int MAX = 2e5 + 7;
vector<int> tree[MAX];
int idx[MAX];
int child[MAX];
int parity[MAX];
bool vst[MAX];
vector<int> euler;
void dfs(int node, int h = 0) {
  vst[node] = true;
  parity[node] = h & 1;
  idx[node] = euler.size();
  euler.push_back(node);
  child[node] = 1;
  for (int to : tree[node]) {
    if (!vst[to]) {
      dfs(to, h + 1);
      child[node] += child[to];
    }
  }
}
long long bit[2][MAX];
inline void add(int p, int x, long long val) {
  for (int i = x; i < MAX; i += (i & -i)) bit[p][i] += val;
}
inline long long sum(int p, int x) {
  long long res = 0;
  for (int i = x; i > 0; i -= (i & -i)) res += bit[p][i];
  return res;
}
int ar[MAX];
int main() {
  ios ::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n, q;
  cin >> n >> q;
  for (int i = 1; i <= n; ++i) cin >> ar[i];
  for (int i = 1; i <= n - 1; ++i) {
    int u, v;
    cin >> u >> v;
    tree[u].push_back(v);
    tree[v].push_back(u);
  }
  euler.push_back(-1);
  dfs(1);
  while (q--) {
    int t;
    cin >> t;
    if (t == 1) {
      int x, val;
      cin >> x >> val;
      add(parity[x], idx[x], val);
      add(parity[x], idx[x] + child[x], -val);
      add(1 ^ parity[x], idx[x], -val);
      add(1 ^ parity[x], idx[x] + child[x], val);
    } else {
      int x;
      cin >> x;
      cout << ar[x] + sum(parity[x], idx[x]) << '\n';
    }
  }
  return 0;
}
