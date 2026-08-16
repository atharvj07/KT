#include <bits/stdc++.h>
using namespace std;
const int MAX = 200, dx[] = {0, 1, 0, -1}, dy[] = {1, 0, -1, 0};
int ans[MAX * 2 + 1][MAX * 2 + 1];
int main() {
  int n, t, x, y;
  scanf("%d%d", &n, &t);
  queue<int> Q;
  Q.push(MAX), Q.push(MAX);
  ans[MAX][MAX] = n;
  while (!Q.empty()) {
    x = Q.front(), Q.pop();
    y = Q.front(), Q.pop();
    if (ans[x][y] >= 4) {
      for (int i = 0; i < 4; ++i) {
        int tx = x + dx[i], ty = y + dy[i];
        ans[tx][ty] += ans[x][y] / 4;
        if (ans[tx][ty] > 3) Q.push(tx), Q.push(ty);
      }
      ans[x][y] %= 4;
    }
  }
  while (t--) {
    scanf("%d%d", &x, &y);
    if (abs(x) > MAX || abs(y) > MAX)
      puts("0");
    else {
      printf("%d\n", ans[x + MAX][y + MAX]);
    }
  }
  return 0;
}
