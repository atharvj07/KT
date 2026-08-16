#include <bits/stdc++.h>
using namespace std;
struct Node {
  int x1, y1, x2, y2;
};
struct Node line[110], node[210];
int n, m, w, h;
int isgo[110];
int ans[110];
int judge(int u, int v) {
  if (line[u].x1 == line[u].x2) {
    int a = line[u].y1;
    int b = line[u].y2;
    if (a == node[v].y1 && b == node[v].y2 && line[u].x1 > node[v].x1 &&
        line[u].x1 < node[v].x2)
      return 1;
  } else {
    int a = line[u].x1;
    int b = line[u].x2;
    if (a == node[v].x1 && b == node[v].x2 && line[u].y1 > node[v].y1 &&
        line[u].y1 < node[v].y2)
      return 1;
  }
  return 0;
}
void add(int u, int a, int b, int c, int d) {
  node[u].x1 = a, node[u].y1 = b;
  node[u].x2 = c, node[u].y2 = d;
}
int main() {
  while (scanf("%d %d %d", &w, &h, &n) != EOF) {
    for (int i = 1; i <= n; i++)
      scanf("%d %d %d %d", &line[i].x1, &line[i].y1, &line[i].x2, &line[i].y2);
    m = 1;
    node[1].x1 = node[1].y1 = 0;
    node[1].x2 = w, node[1].y2 = h;
    memset(isgo, 0, sizeof(isgo));
    for (int k = 1; k <= n; k++) {
      for (int i = 1; i <= n; i++)
        if (isgo[i] == 0) {
          int found = 0;
          for (int j = 1; j <= m; j++) {
            int test = judge(i, j);
            if (test == 0)
              continue;
            else {
              isgo[i] = 1;
              m++;
              int a = node[j].x1, b = node[j].y1;
              int c = node[j].x2, d = node[j].y2;
              add(j, a, b, line[i].x2, line[i].y2);
              add(m, line[i].x1, line[i].y1, c, d);
              found = 1;
              break;
            }
          }
          if (found == 1) break;
        }
    }
    for (int i = 1; i <= m; i++)
      ans[i] = (node[i].x2 - node[i].x1) * (node[i].y2 - node[i].y1);
    sort(ans + 1, ans + 1 + m);
    for (int i = 1; i <= m; i++) {
      printf("%d", ans[i]);
      if (i == m)
        printf("\n");
      else
        printf(" ");
    }
  }
  return 0;
}
