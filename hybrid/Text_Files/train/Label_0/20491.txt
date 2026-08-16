#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const long long inf = 0x3f3f3f3f3f3f3f3f;
const long long mod = 1e9 + 7;
const int N = 4e5 + 10;
int n, m;
int a[N], p[N];
vector<int> G[N];
int vis[N], cnt, ok[N];
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]), p[a[i]] = i;
  for (int i = 0; i < m; i++) {
    int u, v;
    scanf("%d%d", &u, &v);
    G[u].push_back(v);
    if (v == a[n]) vis[u] = 1;
  }
  ok[a[n]] = 1;
  for (int i = n - 1; i >= 1; i--) {
    if (vis[a[i]]) {
      int su = 0;
      for (int v : G[a[i]]) {
        if (p[v] > i) {
          if (!ok[v]) su++;
        }
      }
      if (cnt + su >= n - i - 1) {
        ok[a[i]] = 1;
        cnt++;
      }
    }
  }
  printf("%d\n", cnt);
  return 0;
}
