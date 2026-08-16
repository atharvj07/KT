#include <bits/stdc++.h>
using namespace std;
const int N = 100001;
int n;
vector<int> g[N];
int a[N];
int b[N];
vector<int> ans;
void dfs(int now, int fa, int depth, int k[2]) {
  a[now] ^= k[depth & 1];
  if (a[now] != b[now]) {
    ans.push_back(now);
    k[depth & 1] ^= 1;
  }
  for (int i = 0; i < g[now].size(); ++i)
    if (g[now][i] != fa) {
      int kk[2];
      kk[0] = k[0];
      kk[1] = k[1];
      dfs(g[now][i], now, depth + 1, kk);
    }
}
int main() {
  scanf("%d", &n);
  int u, v;
  for (int i = 0; i < n - 1; ++i) {
    scanf("%d%d", &u, &v);
    g[u].push_back(v);
    g[v].push_back(u);
  }
  for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
  for (int i = 1; i <= n; ++i) scanf("%d", &b[i]);
  int k[2] = {0, 0};
  dfs(1, 0, 0, k);
  printf("%d\n", ans.size());
  for (int i = 0; i < ans.size(); ++i) printf("%d\n", ans[i]);
  return 0;
}
