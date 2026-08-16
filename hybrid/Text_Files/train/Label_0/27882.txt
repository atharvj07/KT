#include <bits/stdc++.h>
using namespace std;
const int N = 5e5 + 5;
int n, m;
vector<pair<int, int> > v[N];
int color[N], h[N], d[N];
int main() {
  scanf("%d %d", &n, &m);
  for (int i = 1; i <= m; i++) {
    int x, y, t;
    scanf("%d %d %d", &x, &y, &t);
    v[y].push_back({x, t});
  }
  queue<int> q;
  q.push(n);
  memset(color, -1, sizeof(color));
  d[1] = -1;
  d[n] = 0;
  h[n] = 1;
  while (!q.empty()) {
    int x = q.front();
    q.pop();
    for (auto e : v[x]) {
      int u, t;
      tie(u, t) = e;
      if (color[u] == -1) {
        color[u] = !t;
      }
      if (color[u] != t) {
        continue;
      }
      if (!h[u]) {
        h[u] = 1;
        d[u] = d[x] + 1;
        q.push(u);
      }
    }
  }
  printf("%d\n", d[1]);
  for (int i = 1; i <= n; i++) {
    printf("%d", max(0, color[i]));
  }
  puts("");
  return 0;
}
