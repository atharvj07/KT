#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
int dep[N], fa[N], tot[N];
bool dp[N], vis[N];
int find(int x) {
  if (x == fa[x])
    return x;
  else {
    int f = fa[x];
    fa[x] = find(f);
    dep[x] += dep[f];
    return fa[x];
  }
}
void make(int x, int y) {
  int fx = find(x);
  fa[y] = x;
  dep[y]++;
  tot[fx] += tot[y];
  tot[y] = 0;
}
int main() {
  int n, x;
  scanf("%d%d", &n, &x);
  for (int i = 1; i <= n; i++) {
    fa[i] = i;
    dep[i] = 0;
    tot[i] = 1;
  }
  int f;
  for (int i = 1; i <= n; i++) {
    scanf("%d", &f);
    if (f != 0) make(f, i);
  }
  vector<int> a;
  memset(vis, false, sizeof(vis));
  int fx = find(x), s = dep[x] + 1;
  vis[fx] = true;
  for (int i = 1; i <= n; i++) {
    int f = find(i);
    if (!vis[f]) {
      vis[f] = true;
      a.push_back(tot[f]);
    }
  }
  memset(dp, false, sizeof(dp));
  dp[0] = true;
  for (int i = 0; i < a.size(); i++) {
    int v = a[i];
    for (int i = n; i >= v; i--) {
      if (dp[i - v]) dp[i] = true;
    }
  }
  for (int i = 0; i + s <= n; i++) {
    if (dp[i]) printf("%d\n", i + s);
  }
  return 0;
}
