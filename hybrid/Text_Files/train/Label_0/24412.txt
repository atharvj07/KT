#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10;
vector<int> e[N];
int n, m, h[N], sg[N], sum[N], dg[N], q[N], vis[N];
void topsort() {
  int h = 1, t = 0;
  for (int i = 1; i <= n; i++)
    if (!dg[i]) q[++t] = i;
  while (h <= t) {
    int u = q[h++];
    for (int v : e[u])
      if (!--dg[v]) q[++t] = v;
  }
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) scanf("%d", &h[i]);
  for (int i = 1; i <= m; i++) {
    int u, v;
    scanf("%d%d", &u, &v);
    e[u].push_back(v);
    dg[v]++;
  }
  topsort();
  for (int i = n; i; i--) {
    int u = q[i];
    for (int v : e[u]) vis[sg[v]] = i;
    while (vis[sg[u]] == i) sg[u]++;
    sum[sg[u]] ^= h[u];
  }
  for (int i = n; ~i; i--)
    if (sum[i]) {
      int pos;
      for (int j = 1; j <= n; j++)
        if (sg[j] == i && h[j] > (sum[i] ^ h[j])) pos = j;
      h[pos] ^= sum[i];
      for (int v : e[pos]) h[v] ^= sum[sg[v]], sum[sg[v]] = 0;
      printf("WIN\n");
      for (int j = 1; j <= n; j++) printf("%d ", h[j]);
      printf("\n");
      return 0;
    }
  printf("LOSE");
}
