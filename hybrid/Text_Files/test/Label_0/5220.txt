#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 7;
const int INF = 2e9 + 7;
const int MOD = 1e9 + 7;
const long long LINF = 1e17 + 7;
const double Pi = acos(-1.);
const double EPS = 1e-8;
int n, m, k, c[N], ans[N];
vector<int> e[N], s[2];
queue<int> que;
void bfs(int u) {
  c[u] = 0, que.push(u);
  while (!que.empty()) {
    u = que.front();
    que.pop();
    for (int i = 0; i < ((int)(e[u].size())); ++i) {
      int v = e[u][i];
      if (!~c[v]) {
        c[v] = c[u] ^ 1;
        que.push(v);
      }
    }
  }
}
bool calc() {
  int p = -1;
  for (int i = 0; i < ((int)(s[0].size())); ++i) {
    int x = s[0][i];
    if (((int)(e[x].size())) + 2 <= ((int)(s[1].size())) && !~ans[x]) {
      p = x;
      break;
    }
  }
  if (!~p) return false;
  ans[p] = ++k;
  for (int i = 0, j = 0; j < 2 && i < ((int)(s[1].size())); ++i) {
    int q = s[1][i];
    if (binary_search((e[p]).begin(), (e[p]).end(), q)) continue;
    ++j;
    ans[q] = k;
  }
  return true;
}
bool solve() {
  for (int i = 0; i < n; ++i) sort((e[i]).begin(), (e[i]).end());
  for (int i = 0; i < n; ++i)
    if (!~c[i]) bfs(i);
  for (int i = 0; i < n; ++i) s[c[i]].push_back(i);
  if (((int)(s[0].size())) % 3 == 0) return true;
  if (((int)(s[0].size())) % 3 == 2) swap(s[0], s[1]);
  if (calc()) return true;
  swap(s[0], s[1]);
  if (calc() && calc()) return true;
  return false;
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; ++i) {
    c[i] = ans[i] = -1;
  }
  for (int i = 0; i < m; ++i) {
    int u, v;
    scanf("%d%d", &u, &v);
    e[u - 1].push_back(v - 1), e[v - 1].push_back(u - 1);
  }
  if (!solve()) {
    puts("NO");
  } else {
    for (int d = 0; d < 2; ++d)
      for (int i = 0, j = 0; i < ((int)(s[d].size())); ++i) {
        int x = s[d][i];
        if (!~ans[x]) {
          ans[x] = (!j ? ++k : k);
          j = (j + 1) % 3;
        }
      }
    puts("YES");
    for (int i = 0; i < n; ++i) {
      if (i) putchar(' ');
      printf("%d", ans[i]);
    }
  }
  return 0;
}
