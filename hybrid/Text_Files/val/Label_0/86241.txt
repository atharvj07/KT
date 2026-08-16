#include <bits/stdc++.h>
using namespace std;
const int maxn = 300;
int arr[maxn][maxn], ans[maxn][maxn];
int n, m;
queue<pair<int, int> > que;
int h[maxn * maxn], v[maxn * maxn];
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) scanf("%d", &arr[i][j]);
  }
  for (int i = 1; i <= n; i++) {
    int mx = 0;
    for (int j = 1; j <= m; j++) mx = max(mx, arr[i][j]);
    h[mx] = 1;
  }
  for (int i = 1; i <= m; i++) {
    int mx = 0;
    for (int j = 1; j <= n; j++) mx = max(mx, arr[j][i]);
    v[mx] = 1;
  }
  int x = 0, y = 0;
  for (int u = n * m; u >= 1; u--) {
    x += h[u];
    y += v[u];
    if (h[u] || v[u]) {
      ans[x][y] = u;
    } else {
      auto tmp = que.front();
      que.pop();
      ans[tmp.first][tmp.second] = u;
    }
    if (h[u]) {
      for (int i = y - 1; i >= 1; i--) que.emplace(x, i);
    }
    if (v[u]) {
      for (int i = x - 1; i >= 1; i--) que.emplace(i, y);
    }
  }
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      printf("%d%c", ans[i][j], j == m ? '\n' : ' ');
    }
  }
  return 0;
}
