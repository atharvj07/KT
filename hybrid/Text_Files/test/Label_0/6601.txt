#include <bits/stdc++.h>
int n, m, len[1010], visited[1010], adj[1010][1010];
void dfs(int i) {
  int j, x;
  visited[i] = 1;
  for (j = 0; j < len[i]; j++) {
    x = adj[i][j];
    if (!visited[x]) dfs(x);
  }
}
int main() {
  int i, j, k, a, b, res;
  while (scanf("%d %d", &n, &m) != EOF) {
    memset(len, 0, sizeof(len));
    for (i = 0; i < m; i++) {
      scanf("%d %d", &a, &b);
      adj[a][len[a]++] = b;
      adj[b][len[b]++] = a;
    }
    if ((n - 1) == m) {
      memset(visited, 0, sizeof(visited));
      for (i = 1, res = 0; i <= n; i++) {
        if (!visited[i]) {
          res++;
          dfs(i);
        }
      }
      if (res == 1)
        puts("yes");
      else
        puts("no");
    } else
      puts("no");
  }
  return 0;
}
