#include <bits/stdc++.h>
bool flag[2000][2000];
struct node {
  int x;
  int y;
};
node point[3001];
int main() {
  int n;
  memset(flag, false, sizeof(flag));
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d %d", &point[i].x, &point[i].y);
    flag[point[i].x + 1000][point[i].y + 1000] = true;
  }
  int ans = 0;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++) {
      if (i != j && (point[i].x + point[j].x) % 2 == 0 &&
          (point[j].y + point[i].y) % 2 == 0) {
        int midx = (point[i].x + point[j].x) / 2;
        int midy = (point[i].y + point[j].y) / 2;
        if (flag[midx + 1000][midy + 1000]) ans++;
      }
    }
  printf("%d\n", ans / 2);
  return 0;
}
