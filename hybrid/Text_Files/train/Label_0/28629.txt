#include <bits/stdc++.h>
using namespace std;
int main() {
  int room, type;
  int rooms[500 + 5][4];
  int types[500 + 5][4];
  int i, j;
  int best, ans;
  int len, width;
  int mod, pic, sum;
  while (scanf("%d", &room) != EOF) {
    for (i = 0; i < room; i++) {
      scanf("%d%d%d", &rooms[i][0], &rooms[i][1], &rooms[i][2]);
    }
    scanf("%d", &type);
    for (i = 0; i < type; i++) {
      scanf("%d%d%d", &types[i][0], &types[i][1], &types[i][2]);
    }
    best = 1000000000;
    ans = 0;
    for (i = 0; i < room; i++) {
      len = 2 * (rooms[i][1] + rooms[i][0]);
      width = rooms[i][2];
      best = 1000000000;
      for (j = 0; j < type; j++) {
        if (types[j][0] >= width) {
          pic = types[j][0] / rooms[i][2];
          sum = ceil((double)len / (pic * types[j][1]));
          sum = sum * types[j][2];
          if (best > sum) {
            best = sum;
          }
        }
      }
      ans += best;
    }
    printf("%d\n", ans);
  }
  return 0;
}
